import re

class URLFinder():
    INLINE_URL_PATTERN = re.compile(r'\[[^\[\]]+\]\([^\(\)]+\)')
    ANCHOR_TEXT_PATTERN = re.compile(r'\[[^\[\]]+\]')
    URL_PATTERN = re.compile(r'\([^\(\)]+\)')

        
    def find_all_inline_urls(self, text: str) -> str:
        """
        Given a text with the format:
        'hello [this is a link](some-url.com) [and other](some-other-url.com) relevant'
        returns all the urls on it
        [
            '[this is a link](some-url.com)',
            '[and other](some-other-url.com)',
        ]
        """
        return self.INLINE_URL_PATTERN.findall(text)

    def split_inline_url(self, text: str) -> str:
        """
        Given a text with the format [some text](some-url.com)
        returns both texts ('some text', 'some-url.com')
        """
        split_text = text.split("](")

        anchor_text = split_text[0][1:]
        url = split_text[1][:-1]

        return anchor_text, url
