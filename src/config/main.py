from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    YamlConfigSettingsSource,
    PydanticBaseSettingsSource,
)

from config.env_config import EnvConfig
from config.yaml_config import YamlConfig
from utils.singleton import singleton
from utils.try_except import try_except
from utils.logger import log


def verify_path(path: Path, mandatory: bool = False) -> Optional[str]:
    if not path.exists():
        if mandatory:
            raise FileNotFoundError(f"Path {path} does not exist.")
        else:
            log.warning(f"Path {path} does not exist. Returning empty string.")
        return ""
    return str(path)


@singleton
class MainConfig(BaseSettings):
    config_files_dir_path: Path = Path(__file__).parent / "config_files"

    env_file: str = verify_path(config_files_dir_path / ".env")
    yaml_file: str = verify_path(config_files_dir_path / "config.yaml")

    env: EnvConfig = Field(default_factory=EnvConfig)
    yaml: YamlConfig = Field(default_factory=YamlConfig)

    model_config = SettingsConfigDict(
        env_file=env_file,
        yaml_file=yaml_file,
        env_nested_delimiter="__",
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            YamlConfigSettingsSource(settings_cls),
            file_secret_settings,
        )


@try_except(error_callable=exit)
def _get_config() -> MainConfig:
    config = MainConfig()
    log.debug(f"_get_config: {config.model_dump()}")
    return config
