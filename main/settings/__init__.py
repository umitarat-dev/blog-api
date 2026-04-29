# main/settings/__init__.py
from decouple import config

env_name = config("ENV_NAME", default="dev")

if env_name == "prod":
    from .prod import *
else:
    from .dev import *