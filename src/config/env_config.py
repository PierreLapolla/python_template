from pydantic import BaseModel, Field


class EnvConfig(BaseModel):
    API_KEY: str = Field(description="API key for the application")

    model_config = {
        "env_prefix": "ENV__",
    }
