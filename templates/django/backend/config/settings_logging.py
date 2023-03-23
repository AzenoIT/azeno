import os
from pathlib import Path


def get_logger_config(base_dir: Path) -> dict:
    """Return logger config.

    :param base_dir: Base directory of the project.
    :type base_dir: Path
    :returns: Logger configuration.
    :rtype: dict
    """

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "debug": {
                "level": "DEBUG",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(base_dir, "logs/debug.log"),
                "maxBytes": 5242880,
                "backupCount": 5,
                "formatter": "verbose",
                "delay": True,
            },
            "info": {
                "level": "INFO",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(base_dir, "logs/info.log"),
                "maxBytes": 5242880,
                "backupCount": 5,
                "formatter": "verbose",
                "delay": True,
            },
            "error": {
                "level": "ERROR",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(base_dir, "logs/error.log"),
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
