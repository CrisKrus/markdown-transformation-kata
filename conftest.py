import os

from src.file_manager import READ_ONLY


def clean_up_fixtures(elements_to_remove: list):
    for element in elements_to_remove:
        os.remove(element)

def content_equals(file_path: str, expected_output: str):
    with open(file_path, READ_ONLY) as output:
        output_file_content = output.read()
        output.close()
        return output_file_content == expected_output
