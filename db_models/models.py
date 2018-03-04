
from .config import Config as conf

if conf.SCHEMA_TYPE == "consulting":
    # from .schemas.general import *
    from .schemas.consulting import Base
elif conf.SCHEMA_TYPE == "engineering":
    # from .schemas.general import *
    from .schemas.engineering import Base
else:
    from .schemas.general import Base

