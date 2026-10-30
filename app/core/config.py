
import os


class Settings:
    APP_NAME: str = "CloudPulse AI"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv(
        "APP_ENV",
        "development"
    )
    API_PREFIX: str = "/api/v1"


settings = Settings()
