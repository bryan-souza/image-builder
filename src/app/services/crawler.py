from abc import ABC, abstractmethod
from typing import List

from playwright.sync_api import sync_playwright
from loguru import logger

from src.app.services.exceptions import DownloadButtonNotFoundError


class CrawlerService(ABC):
    @abstractmethod
    def run(self, url: str) -> List[str]:
        """
        Runs the web crawler

        Params:
        url: str

        Returns:
        List[str]
            A list of dedicated server binary download links

        Raises:
        DownloadButtonNotFoundError
            If no compatible download button was found in the provided page
        """
        ...


class CrawlerServiceImpl(CrawlerService):
    def run(self, url):
        # TODO: Refactor
        with sync_playwright() as p:
            browser = p.firefox.launch()
            page = browser.new_page(user_agent='Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0')
            page.goto(url)
            page.wait_for_load_state(state='networkidle')
            logger.debug(f"Loaded page {url}")

            download_button_locator = page.locator(".downloadlink")
            elements = download_button_locator.all()
            if not elements:
                logger.error("Download button not found")
                raise DownloadButtonNotFoundError(url)
            logger.debug(f"Found {len(elements)} download links")

            download_links = []
            for element in elements:
                download_links.append(element.get_attribute("href"))

            return download_links
