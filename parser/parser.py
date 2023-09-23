"""Module with Parcer class for parsing sites."""

import requests
import re


class Parser:
    def __init__(self, title_name: str):
        """Initializing method.

        Args:
            title_name: title or series name
        """
        self.__title_name = title_name

    @property
    def title_name(self) -> str:
        """Returns title or series name.

        Returns: title or series name
        """
        return self.__title_name

    def parse_site(self):
        """Site parsing method."""
        response = requests.get(
            f'https://www.toramp.com/ru/search/?q={self.title_name}'
        ).text
        pattern = r'class="title" title="(.*?)">.*?</a>'
        return re.findall(pattern, response)
