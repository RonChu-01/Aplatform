# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/1/20.
# Copyright (c) 2019 3KWan.
# Description :
import os
import time

from app.constant.const import Constant
from app.constant.const_app import APP

LOG = Constant()

LOG.ROOT_PATH = os.path.join(APP.PROJECT_ROOT_PATH, "app", "log")  # 日志文件记录根目录
# 文件夹不存在创建
if not os.path.exists(LOG.ROOT_PATH):
    os.makedirs(LOG.ROOT_PATH)
log_file_format = "{}.txt".format(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time())))  # 日志文件格式
LOG.LOG_FILE = os.path.join(LOG.ROOT_PATH, log_file_format)  # 日志文件
