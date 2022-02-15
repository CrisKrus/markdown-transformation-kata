import click

from src.file_manager import READ_ONLY, WRITE_ONLY
from src.url_finder import URLFinder
from src.url_manager import URLManager

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
            url_finder = URLFinder()
            url_manager = URLManager()

            for line in input_file:
                inline_urls = url_finder.find_all_inline_urls(line)
                for inline_url in inline_urls:
                    anchor_text, url = url_finder.split_inline_url(inline_url)
                    url_manager.addUrl(url)

                    url_index = url_manager.getAliasFor(url)
                    url_placeholder = f"{anchor_text} [^{url_index}]"
                    line = line.replace(inline_url, url_placeholder)

                output_file.write(line)

            if url_manager.hasUrls():
                output_file.write("\n\n")

                for url in url_manager.allUrls():
                    url_index = url_manager.getAliasFor(url)
                    output_file.write(f"[^{url_index}]: {url}\n")
            output_file.close()
        input_file.close()

if __name__ == '__main__':
    markdown_formatter(prog_name='mdf')