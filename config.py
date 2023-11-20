import os
from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

load_dotenv()


class AllSettings(BaseSettings):
    my_chat_id: SecretStr = os.getenv('MY_CHAT_ID', None)
    tg_channels: list = os.getenv('TG_CHANNELS', None)
    bot_token: SecretStr = os.getenv('BOT_TOKEN', None)
