import logging
from typing import List, Dict

import aiohttp


class YandexGPT:
    def __init__(self, token: str, model_uri: str):
        self.token = token
        self.model_uri = model_uri
        self.url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        self.system_prompt = (
            "Ты информационный гид по мероприятию в Москве, которое называется «Театральный бульвар». "
            "«Театральный бульвар» – это первый открытый уличный театральный фестиваль в Москве, "
            "который пройдет с 1 июня по 31 августа 2025 года."
        )

    async def generate_text(self, messages: List[Dict]) -> str:
        messages = [
            {"role": "system", "text": self.system_prompt},
            *messages
        ]

        payload = {
            "modelUri": self.model_uri,
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": "2000",
                "reasoningOptions": {
                    "mode": "DISABLED"
                }
            },
            "messages": messages
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url, json=payload, headers=self.headers) as response:
                    if response.status == 200:
                        result = await response.json()
                        return result['result']['alternatives'][0]['message']['text']

        except Exception as ex:
            logging.error(ex)
            raise ex
