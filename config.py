import os
from dotenv import load_dotenv
# from pydantic import BaseSettings, SecretStr
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
load_dotenv()


class AllSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    my_chat_id: SecretStr = os.getenv('MY_CHAT_ID', None)
    tg_channels: list = os.getenv('TG_CHANNELS', None)
    bot_token: SecretStr = os.getenv('BOT_TOKEN', None)


# class AllSettings(BaseSettings):
#     my_chat_id: SecretStr = os.getenv('MY_CHAT_ID', None)
#     tg_channels: list = os.getenv('TG_CHANNELS', None)
#     bot_token: SecretStr = os.getenv('BOT_TOKEN', None)


# settings = AllSettings()

# print(settings.bot_token)
