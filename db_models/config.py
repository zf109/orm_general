
from os import getenv

class Config(object):
    SCHEMA_TYPE = getenv("SCHEMA_TYPE", "general")
    DATABASE_URI = getenv("DATABASE_URI", "postgresql://postgres:wizardrules@localhost:5432/core")
