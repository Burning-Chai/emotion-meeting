# -*- coding: utf-8 -*-
import ConfigParser
import os


class ConfigUtil:
    config_instance = None

    def __init__(self):
        pass

    @staticmethod
    def init_config():
        if not ConfigUtil.config_instance:
            ConfigUtil.config_instance = ConfigParser.SafeConfigParser()
            ConfigUtil.config_instance.read(os.path.join(os.path.dirname(__file__), "../setting.prop"))
        return ConfigUtil.config_instance

    @staticmethod
    def get(section, key):
        config = ConfigUtil.init_config()
        return config.get(section, key)
