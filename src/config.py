import os
from pathlib import Path

from src.config_schema import Settings

settings_path = "./setting.yaml"
settings: Settings = Settings.from_yaml(Path(settings_path))
