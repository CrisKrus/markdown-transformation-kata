from click.testing import CliRunner
from src.file_manager import READ_ONLY, WRITE_ONLY
from src.main import url_to_footnote

SUCCESS_EXIT_CODE = 0

# TODO crear un setup que borre todos los fixtures antes de cada test
# TODO tener en cuenta la asincronia de los tests 
# TODO tener en cuenta que pasa si crearmos un fichero y el siguiente test intenta crear uno nuevo pero ya existe

# TODO crear un modulo para lectura/escritura de ficheros en el sistema

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

def test_format_a_url_as_footnote():
    runner = CliRunner()
    input_file_path = 'test/fixtures/input_file2.md'
    output_file_path = 'test/fixtures/output_file2.md'
    
    with open(input_file_path, WRITE_ONLY) as input_file:
        input_file.write("[visible text](url-to-domain.com)")
        input_file.close()

    result = runner.invoke(url_to_footnote, ["-i", input_file_path, "-o", output_file_path])
    
    assert result.exit_code == SUCCESS_EXIT_CODE
    with open(output_file_path, READ_ONLY) as output:
        assert output.read() == """visible text [^placeholder]

[^placeholder]: url-to-domain.com"""
        output.close()
    
