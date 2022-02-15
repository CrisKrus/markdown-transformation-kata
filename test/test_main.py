from click.testing import CliRunner
from conftest import clean_up_fixtures
from src.file_manager import READ_ONLY, WRITE_ONLY
from src.main import url_to_footnote

SUCCESS_EXIT_CODE = 0

# TODO crear un setup que borre todos los fixtures antes de cada test
# TODO tener en cuenta la asincronia de los tests 

# TODO crear un modulo para lectura/escritura de ficheros en el sistema para desacoplar la lectura que siempre es local

def test_create_an_output_file():
    runner = CliRunner()
    input_file_path = 'test/fixtures/input_file.md'
    output_file_path = 'test/fixtures/output_file.md'

    with open(input_file_path, WRITE_ONLY) as input_file:
        input_file.write("some text")
        input_file.close()

    result = runner.invoke(url_to_footnote, ["-i", input_file_path, "-o", output_file_path])

    assert result.exit_code == SUCCESS_EXIT_CODE
    with open(output_file_path, READ_ONLY) as output:
        assert output.read() == "some text"
        output.close()
    clean_up_fixtures([input_file_path, output_file_path])


def test_format_a_url_as_footnote():
    runner = CliRunner()
    input_file_path = 'test/fixtures/input_file.md'
    output_file_path = 'test/fixtures/output_file.md'
    
    with open(input_file_path, WRITE_ONLY) as input_file:
        input_file.write("previous text [visible text](url-to-domain.com)")
        input_file.close()

    result = runner.invoke(url_to_footnote, ["-i", input_file_path, "-o", output_file_path])
    
    assert result.exit_code == SUCCESS_EXIT_CODE
    with open(output_file_path, READ_ONLY) as output:
        assert output.read() == """previous text visible text [^1]

[^1]: url-to-domain.com
"""
        output.close()
    clean_up_fixtures([input_file_path, output_file_path])

    
def test_format_multiple_inlineurl_as_footnote():
    runner = CliRunner()
    input_file_path = 'test/fixtures/input_file.md'
    output_file_path = 'test/fixtures/output_file.md'
    
    with open(input_file_path, WRITE_ONLY) as input_file:
        input_file.write("""[visible text](url-to-domain.com)
some text [here link](other-url.com)
more text here""")
        input_file.close()

    result = runner.invoke(url_to_footnote, ["-i", input_file_path, "-o", output_file_path])
    
    assert result.exit_code == SUCCESS_EXIT_CODE
    with open(output_file_path, READ_ONLY) as output:
        assert output.read() == """visible text [^1]
some text here link [^2]
more text here

[^1]: url-to-domain.com
[^2]: other-url.com
"""
        output.close()
    clean_up_fixtures([input_file_path, output_file_path])

    
def test_format_multiple_urls_in_one_line_as_footnote():
    runner = CliRunner()
    input_file_path = 'test/fixtures/input_file.md'
    output_file_path = 'test/fixtures/output_file.md'
    
    with open(input_file_path, WRITE_ONLY) as input_file:
        input_file.write("previous text [visible text](url-to-domain.com) more text [other link](foo.bar)")
        input_file.close()

    result = runner.invoke(url_to_footnote, ["-i", input_file_path, "-o", output_file_path])
    
    assert result.exit_code == SUCCESS_EXIT_CODE
    with open(output_file_path, READ_ONLY) as output:
        assert output.read() == """previous text visible text [^1] more text other link [^2]

[^1]: url-to-domain.com
[^2]: foo.bar
"""
        output.close()
    clean_up_fixtures([input_file_path, output_file_path])

    
def test_format_same_url_multiple_times_as_footnote():
    runner = CliRunner()
    input_file_path = 'test/fixtures/input_file.md'
    output_file_path = 'test/fixtures/output_file.md'
    
    with open(input_file_path, WRITE_ONLY) as input_file:
        input_file.write("previous text [visible text](some-url.com) more text [same link](some-url.com)")
        input_file.close()

    result = runner.invoke(url_to_footnote, ["-i", input_file_path, "-o", output_file_path])
    
    assert result.exit_code == SUCCESS_EXIT_CODE
    with open(output_file_path, READ_ONLY) as output:
        assert output.read() == """previous text visible text [^1] more text same link [^1]

[^1]: some-url.com
"""
        output.close()
    clean_up_fixtures([input_file_path, output_file_path])
    
