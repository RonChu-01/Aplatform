# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/1/20.
# Copyright (c) 2019 3KWan.
# Description :


class Config:
    """  base config """
    DEBUG = False
    TESTING = False
    DB_SERVER = "127.0.0.1"

    @property
    def DATABASE_URI(self):
        return "mysql+pymysql://root:chuy5945@{}:3306/k_platform".format(self.DB_SERVER)


class ProductionConfig(Config):
    """  生产环境 """
    DB_SERVER = ""


class DevelopmentConfig(Config):
    """  开发环境 """
    DB_SERVER = ""
    DEBUG = True


class TestingConfig(Config):
    """  测试环境 """
    DB_SERVER = ""
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

