class YandexGPT:
    def __init__(self, token: str, model: str):
        self.token = token
        self.model = model

    async def generate_text(self, messages: list) -> str:
        return "Yandex GPT временно не работает..."
