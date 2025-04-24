from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # model_config = SettingsConfigDict(env_file="backend/app/.env")  # вы создаете объект model_config, который
    # загружает настройки из файла .env или выполняет какие-то действия с этим файлом


settings = Settings()
