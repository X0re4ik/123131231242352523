import json
from typing import Any, Tuple
import uuid

import urllib3
import requests


class GigaChatAuth:

    def __init__(self, auth_token) -> None:
        self._auth_token = auth_token

    @property
    def url(self):
        return "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    @property
    def header(self):
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid.uuid4()),
            "Authorization": f"Basic {self._auth_token}",
        }

    @property
    def payload(self):
        return {"scope": "GIGACHAT_API_PERS"}

    def get_access_token(self) -> str | None:
        with urllib3.warnings.catch_warnings():
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.request(
                "POST",
                self.url,
                headers=self.header,
                data=self.payload,
                verify=False,
            )

            return (
                None if response.status_code != 200 else response.json()["access_token"]
            )
