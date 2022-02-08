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
            urls = []
            for line in input_file:
                inline_urls = finder.find_all_inline_urls(line)
                for inline_url in inline_urls:
                    anchor_text, url = finder.split_inline_url(inline_url)
                    if url not in urls:
                        urls.append(url)
                    url_index = urls.index(url) + 1
                    url_placeholder = f"{anchor_text} [^{url_index}]"
                    line = line.replace(inline_url, url_placeholder)

                output_file.write(line)

            if len(urls) > 0:
                output_file.write("\n\n")

                for url in urls:
                    url_index = urls.index(url) + 1 # to avoid start in 0
                    output_file.write(f"[^{url_index}]: {url}\n")
            output_file.close()
        input_file.close()

if __name__ == '__main__':
    markdown_formatter(prog_name='mdf')