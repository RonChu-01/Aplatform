# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/1/20.
# Copyright (c) 2019 3KWan.
# Description :

import logging

from app.constant.const_log import LOG


class Logger:

    def __init__(self, module):
        self.logger = logging.getLogger(module)
        self.logger.setLevel(logging.DEBUG)

        self.log_name = LOG.LOG_FILE  # 记录日志文件名
        self.format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    def __console(self, level, msg):
        # 输出至控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.format)
        self.logger.addHandler(sh)

        # 保存至文件
        fh = logging.FileHandler(filename=self.log_name, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)

        if level == "debug":
            self.logger.debug(msg)
        elif level == "info":
            self.logger.info(msg)
        elif level == "waring":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "critical":
            self.logger.critical(msg)
        else:
            self.logger.error("-> no this level.")

        # 避免产生重复日志
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, msg):
        self.__console("debug", msg)

    def info(self, msg):
        self.__console("info", msg)

    def warning(self, msg):
        self.__console("warning", msg)

    def error(self, msg):
        self.__console("error", msg)

    def critical(self, msg):
        self.__console("critical", msg)
