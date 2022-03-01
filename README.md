# Markdown transformation kata

The goal is to implement a command line tool that takes a markdown file and returns another markdown file, applying certain transformations to the text.

The first transformation is to turn links into footnotes. The syntax of a link is this:

```md
[visible text link](url)
```

The syntax of a footnote is the following:

```md
visible text [^word]

[^word]: url or text 
```

The goal is to make conversions like the following:

Source:

```md
[this book](https://codigosostenible.com) and some other text
and some other text line.
```

Transformation:

```md
this book [^book1] and some other text 
and some other text line.

[^book1]: https://codigosostenible.com
```

## [YouTube video explainig the kata (in spanish)](https://youtu.be/yaRsAoPSvx0)

## How to use this repo

### Install dependencies

```cmd
pipenv shell
pipenv install
```

### Run the tests

```cmd
pipenv shell
pipenv install

pytest
```

### Launch the CLI

```cmd
python src/main.py url-to-footnote -i input_file.md -o output_file.md
```
