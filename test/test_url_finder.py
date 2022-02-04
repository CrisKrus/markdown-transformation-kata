from src.url_finder import URLFinder


def test_finds_an_url():
    result = URLFinder().find_all_inline_urls("[anchor](url.com)")

    assert result[0] == "[anchor](url.com)"

def test_finds_multiple_urls():
    result = URLFinder().find_all_inline_urls("[anchor](url.com) other stuff [new link](other-url.com)")

    assert result[0] == "[anchor](url.com)"
    assert result[1] == "[new link](other-url.com)"

def test_split_anchor_and_url():
    anchor, url = URLFinder().split_inline_url("[anchor](url.com)")

    assert anchor == "anchor"
    assert url == "url.com"

def test_split_complex_urls():
    anchor, url = URLFinder().split_inline_url("[some text](subdomain.my-url_to.com/somethig?query=foo.bar)")

    assert anchor == "some text"
    assert url == "subdomain.my-url_to.com/somethig?query=foo.bar"
