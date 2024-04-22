import os
import dotenv
from dataclasses import dataclass

dotenv.load_dotenv()

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    # admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot


def load_config() -> Config:
    bot_token = os.getenv('BOT_TOKEN')
    return Config(tg_bot=TgBot(token=bot_token))
