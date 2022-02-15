class URLManager():
    def __init__(self) -> None:
        self.urls = []
    
    def addUrl(self, url: str) -> None:
        if url not in self.urls:
            self.urls.append(url)
    
    def getAliasFor(self, url: str) -> str:
        return self.urls.index(url) + 1
    
    def hasUrls(self) -> bool:
        return len(self.urls) > 0

    def allUrls(self) -> list:
        return self.urls.copy()
