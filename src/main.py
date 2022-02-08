import click

from src.file_manager import READ_ONLY, WRITE_ONLY
from src.url_finder import URLFinder

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
            finder = URLFinder()
            text = input_file.read()

            inline_url = finder.find_all_inline_urls(text)
            if inline_url:
                anchor_text, url = finder.split_inline_url(inline_url[0])
                text = f"{anchor_text} [^placeholder]"

            output_file.write(text)
            if inline_url:
                output_file.write("\n\n")
                output_file.write(f"[^placeholder]: {url}")
            output_file.close()
        input_file.close()

if __name__ == '__main__':
    markdown_formatter(prog_name='mdf')