from dotenv import find_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str
    cohere_key: str = ""

    class Config:
        env_file = find_dotenv()
