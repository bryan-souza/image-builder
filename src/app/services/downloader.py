import shutil
from abc import ABC, abstractmethod
from pathlib import Path

import requests


class DownloaderService(ABC):
    @abstractmethod
    def download(self, url: str, storage_path: Path) -> Path:
        """Downloads a file from the internet

        Parameters
        ----------
        url : str
            The URL to download from
        storage_path : Path
            The path where to download the file

        Returns
        -------
        Path
            Complete path of the downloaded file. Consists of `storage_path`/`filename`

        Raises
        ------
        HTTPError
            If the request failed
        """
        ...


class DownloaderServiceImpl(DownloaderService):
    def download(self, url: str, storage_path: Path) -> Path:
        filename = url.split("/")[-1]
        filepath = Path(storage_path, filename)

        with requests.get(url, stream=True) as response:
            response.raise_for_status()

            with open(filepath, "wb") as file:
                shutil.copyfileobj(response.raw, file)

        return filepath
