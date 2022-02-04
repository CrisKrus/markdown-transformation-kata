import re

INLINE_URL_PATTERN = re.compile(r'\[[^\[\]]+\]\([^\(\)]+\)')
ANCHOR_TEXT_PATTERN = re.compile(r'\[[^\[\]]+\]')
URL_PATTERN = re.compile(r'\([^\(\)]+\)')

def url_finder(text: str) -> str:
    return INLINE_URL_PATTERN.findall(text)

def split_inline_url(text: str) -> str:
    """
    Given a text with the format [some text](some-url.com)
    returns both texts ('some text', 'some-url.com')
    """
    split_text = text.split("](")

    anchor_text = split_text[0][1:]
    url = split_text[1][:-1]

    return anchor_text, url

def test_finds_an_url():
    result = url_finder("[anchor](url.com)")

    assert result[0] == "[anchor](url.com)"

def test_split_anchor_and_url():
    anchor, url = split_inline_url("[anchor](url.com)")

    assert anchor == "anchor"
    assert url == "url.com"