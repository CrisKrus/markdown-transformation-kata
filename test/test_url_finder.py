import re

INLINE_URL_PATTERN = re.compile(r'\[[^\[\]]+\]\([^\(\)]+\)')

def url_finder(text: str) -> str:
    return INLINE_URL_PATTERN.findall(text)

def test_finds_an_url():

    result = url_finder("[anchor](url.com)")

    assert result[0] == "[anchor](url.com)"

    
