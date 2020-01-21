# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/1/20.
# Copyright (c) 2019 3KWan.
# Description :
import os

from app.constant.const import Constant

APP = Constant()

# 项目根路径
APP.PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



