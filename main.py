import click

@click.group()
def markdown_formatter():
    """
    A CLI command that formats markdown files
    """

@markdown_formatter.command()
def foo():
    """
    Create a new markdown file replacing the in-line URL
    to footnote format.
    """
    print("I am doing something")

if __name__ == '__main__':
    markdown_formatter(prog_name='mdf')