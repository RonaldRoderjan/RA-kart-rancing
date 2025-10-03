# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    SUPABASE_URL: str
    SUPABASE_KEY: str

# Cria o objeto de configurações que será usado em toda a aplicação
settings = Settings() # <-- ESTA É A LINHA QUE FALTAVA