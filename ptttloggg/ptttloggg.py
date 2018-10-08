import logging
import logging.config
import os


def genLogDict():
    '''
    配置日志格式的字典
    '''
    logDict = {
        "version": 1,
        # "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
            'standard': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
            },

            "access": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "when": "midnight",
                "filename": "log/io_log.log",
                # 'mode': 'a',
                # "maxBytes": 1024*1024*10,  # 5 MB
                "interval": 1,
                "backupCount": 180,
                "encoding": "utf-8"
            },
            "log": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": "ERROR",
                "formatter": "standard",
                "filename": "log/error_log.log",
                "when": "midnight",
                "interval": 1,
                "backupCount": 180,
                "encoding": "utf-8",
            },
        },
        "loggers": {
            "root": {
                'handlers': ['console'],
                'level': "INFO",
                'propagate': False
            },
            "tornado.access": {
                "level": "DEBUG",
                "handlers": ["console", "access"],
                "propagate": False
            },

            "tornado.application": {
                "level": "ERROR",
                "handlers": ["console", "log"],
                "propagate": False,
            },
        },
    }
    return logDict


def initLogConf():
    """
    配置日志
    """
    if not os.path.exists("log"):
        os.mkdir("log")
    logDict = genLogDict()
    logging.config.dictConfig(logDict)


