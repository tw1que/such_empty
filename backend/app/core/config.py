from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    oidc_enabled: bool = False
    oidc_issuer_url: str | None = None
    oidc_audience: str | None = None

    model_config = SettingsConfigDict(env_file="../../.env", env_file_encoding="utf-8")


settings = Settings()
