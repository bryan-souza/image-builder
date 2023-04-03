import pytest

from src.app.services.crawler import CrawlerServiceImpl
from src.app.services.exceptions import DownloadButtonNotFoundError


class TestCrawlerServiceImpl:

    @staticmethod
    def test_run():
        service = CrawlerServiceImpl()
        url = 'https://www.minecraft.net/en-us/download/server/bedrock'
        results = service.run(url)

        assert isinstance(results, list)
        assert len(results) > 0
        for result in results:
            assert isinstance(result, str)

    @staticmethod
    def test_run__DownloadButtonNotFoundError():
        service = CrawlerServiceImpl()
        url = 'https://www.minecraft.net'

        with pytest.raises(DownloadButtonNotFoundError):
            _ = service.run(url)