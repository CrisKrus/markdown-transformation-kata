import re
import click

from src.filesystem import READ_ONLY, WRITE_ONLY

INLINE_URL_PATTERN = re.compile(r'\[[^\[\]]+\]\([^\(\)]+\)')
VISIBLE_TEXT_URL_PATTERN = re.compile(r'\([^\(\)]+\)')
URL_PATTERN = re.compile(r'\[[^\[\]]+\]')

@click.group()
def markdown_formatter():
    """
    A CLI command that formats markdown files
    """

@click.option('-i', '--input-file-path', help='Path to input file to process')
@click.option('-o', '--output-file-path', help='Path to store output file')
@markdown_formatter.command()
def url_to_footnote(input_file_path: str, output_file_path: str):
    """
    Create a new markdown file replacing the in-line URL
    to footnote format.
    """
    with open(input_file_path, READ_ONLY) as input_file:
        with open(output_file_path, WRITE_ONLY) as output_file:
            text = input_file.read()

            inline_url = INLINE_URL_PATTERN.match(text)
            if inline_url:
                visible_text = VISIBLE_TEXT_URL_PATTERN.match(inline_url)
                url = URL_PATTERN.match(inline_url)
                text = f"[{visible_text}] [^placeholder]"

            output_file.write(text)
            if inline_url:
                output_file.write("\n")
                output_file.write(f"[^placeholder]: {url}")
            output_file.close()
        input_file.close()

if __name__ == '__main__':
    markdown_formatter(prog_name='mdf')