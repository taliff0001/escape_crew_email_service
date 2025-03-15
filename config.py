# In config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API settings
    APP_NAME: str = "Order Confirmation Service"

    # Email settings
    MAILTRAP_API_TOKEN: str = "32be2c7f7e6a6c1cc2ecf1918c40b36c"
    EMAIL_SENDER: str
    COMPANY_NAME: str = "Escape Crew"
    SUPPORT_EMAIL: str = "support@example.com"

    class Config:
        env_file = ".env"


settings = Settings()