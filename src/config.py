import os
import json

from dotenv import load_dotenv

load_dotenv()

local_config = json.load(
    open(os.path.join(os.getenv("CONFIG_FOLDER"), "local/config.json"))
)

shared_config = json.load(
    open(os.path.join(os.getenv("CONFIG_FOLDER"), "shared/config.json"))
)

project_root = os.getenv("PROJECT_ROOT")
