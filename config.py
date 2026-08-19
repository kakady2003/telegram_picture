from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("TOKEN_TELEGRAM_BOT")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    def get_db_url(self) -> str:
        db_url = (f"postgresql+asyncpg://"
                  f"{self.DB_USER}:"
                  f"{self.DB_PASSWORD}@"
                  f"{self.DB_HOST}:"
                  f"{self.DB_PORT}/"
                  f"{self.DB_NAME}")

        return db_url


config = Config()
