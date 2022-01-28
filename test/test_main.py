from click.testing import CliRunner
from src.filesystem import READ_ONLY, WRITE_ONLY
from src.main import url_to_footnote

SUCCESS_EXIT_CODE = 0

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
    
