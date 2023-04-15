import pytest

from src.app.services.crawler import CrawlerServiceImpl
from src.app.services.exceptions import DownloadButtonNotFoundError


@pytest.fixture
def crawler_service():
    service = CrawlerServiceImpl()
    return service


class TestCrawlerServiceImpl:
    @staticmethod
    def test_run(crawler_service):
        url = "https://www.minecraft.net/en-us/download/server/bedrock"
        results = crawler_service.run(url)

        assert isinstance(results, list)
        assert len(results) > 0
        for result in results:
            assert isinstance(result, str)

    @staticmethod
    def test_run__DownloadButtonNotFoundError(crawler_service):
        url = "https://www.minecraft.net"

        with pytest.raises(DownloadButtonNotFoundError):
            _ = crawler_service.run(url)
