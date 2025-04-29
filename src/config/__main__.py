from pathlib import Path
from typing import Optional

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    YamlConfigSettingsSource,
    PydanticBaseSettingsSource,
)

from utils.singleton import singleton
from utils.try_except import try_except
from utils.logger import log


def verify_path(path: Path, mandatory: bool = False) -> Optional[str]:
    if not path.exists():
        if mandatory:
            raise FileNotFoundError(f"Path {path} does not exist.")
        else:
            log.warning(f"Path {path} does not exist. Returning None.")
        return None
    return str(path)


class MainConfig(BaseSettings):
    pass


@singleton
class AppConfig(BaseSettings):
    env_dir_path = Path("env")
    yaml_dir_path = Path("yaml")

    env_file = verify_path(env_dir_path / ".env")
    yaml_file = verify_path(yaml_dir_path / "config.yaml")

    model_config = SettingsConfigDict(env_file=env_file, yaml_file=yaml_file)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (YamlConfigSettingsSource(settings_cls),)


@try_except(error_callable=exit)
def get_config() -> AppConfig:
    return AppConfig()
