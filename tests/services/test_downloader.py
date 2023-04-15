from pathlib import Path

import pytest

from src.app.services.downloader import DownloaderServiceImpl


@pytest.fixture
def downloader_service():
    service = DownloaderServiceImpl()
    return service


class TestDownloaderServiceImpl:
    @staticmethod
    def test_constructor(downloader_service):
        assert hasattr(downloader_service, "download")

    @staticmethod
    def test_download(downloader_service, tmp_path):
        url = "http://knowyourmeme.com/photos/377946-rickroll"
        result = downloader_service.download(url, tmp_path)

        assert isinstance(result, Path)
        assert result.is_file()
        assert result.exists()
