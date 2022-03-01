FROM python:3.8-slim

RUN pip install pipenv

WORKDIR /opt/markdown-parser

COPY Pipfile .
RUN pipenv install --deploy --ignore-pipfile

COPY . .

CMD [ "pipenv", "run", "python", "src/main.py", "url-to-footnote-std"]
