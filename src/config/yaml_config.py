from pydantic import BaseModel, Field


class Database(BaseModel):
    name: str = Field(default="default_name", description="Name of the database")
    url: str = Field(
        default="sqlite:///database.db", description="Database connection URL"
    )


class YamlConfig(BaseModel):
    database: Database = Field(
        default_factory=Database, description="Database configuration"
    )

    model_config = {"extra": "ignore"}
