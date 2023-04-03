

class DownloadButtonNotFoundError(Exception):

    def __init__(self, url: str):
        return super().__init__(f'Download button could not be found at page {url}')
