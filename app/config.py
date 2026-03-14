from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[0].parent


class Settings(BaseSettings):
    database_url: str = Field(..., description="database url")
    algorithm: str = Field(description="", default="HS256")
    secret_key: str = Field(..., min_length=32)
    access_token_expires: int = Field(default=15)
    debug: bool = Field(default=False)
    api_version: str = Field(default="v1")

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()  # type: ignore

print(f"Database: {settings.database_url}")
print(f"Debug mode: {settings.debug}")
