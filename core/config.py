from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    PROJECT_NAME: str = 'PIUS2'
    PROJECT_VERSION: str = '1.0.0'

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    POSTGRES_DB_TEST: str = os.getenv("POSTGRES_DB_TEST")
    DATABASE_URL: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                        f"@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    DATABASE_TEST_URL: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                             f"@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB_TEST}"


settings = Settings()
