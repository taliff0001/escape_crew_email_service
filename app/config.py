from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API settings
    APP_NAME: str = "Order Confirmation Service"

    # Email settings
    MAILTRAP_API_TOKEN: str = "79e53f34f765b56b398051c45524a776"
    EMAIL_SENDER: str = "hello@demomailtrap.co"
    COMPANY_NAME: str = "Mailtrap Test"
    SUPPORT_EMAIL: str = "tmaliff@outlook.com"

    class Config:
        env_file = ".env"


settings = Settings()