import requests
import urllib3

import json


from http import HTTPStatus


class GigaChatDriver:

    def __init__(self, access_token: str) -> None:
        self._access_token = access_token

    @property
    def url(self):
        return "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    @property
    def payload(self):
        return {
            "model": "GigaChat",
            "messages": [
                {
                    "role": "user",
                    "content": "",
                }
            ],
            "temperature": 1,
            "top_p": 0.1,
            "n": 1,
            "stream": False,
            "max_tokens": 512,
            "repetition_penalty": 1,
        }

    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self._access_token}",
        }

    def get_answer(self, message: str) -> str:
        with urllib3.warnings.catch_warnings():
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            payload = self.payload
            payload["messages"][0]["content"] = message

            response = requests.request(
                "POST",
                self.url,
                headers=self.headers,
                data=json.dumps(self.payload),
                verify=False,
            )
            return (
                None
                if response.status_code != HTTPStatus.OK
                else response.json()["choices"][0]["message"]["content"]
            )
