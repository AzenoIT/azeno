import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "debug": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/debug.log"),
            "maxBytes": 5242880,
            "backupCount": 5,
            "formatter": "verbose",
            "delay": True,
        },
        "info": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/info.log"),
            "maxBytes": 5242880,
            "backupCount": 5,
            "formatter": "verbose",
            "delay": True,
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/error.log"),
            "maxBytes": 5242880,
            "backupCount": 5,
            "formatter": "verbose",
            "delay": True,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["debug", "info", "error"],
            "level": os.environ.get("LOGGING_LVL", "DEBUG"),
            "propagate": True,
        }
    },
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s"
        },
    },
}
