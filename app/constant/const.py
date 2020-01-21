# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/1/20.
# Copyright (c) 2019 3KWan.
# Description :


class Constant:
    """  常量类 """

    class ConstantError(TypeError):
        pass

    class ConstantCaseError(ConstantError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise self.ConstantError("-> constant {} is already bind can not bind again.".format(key))
        elif not key.isupper():
            raise self.ConstantCaseError("-> constant name {} is not all upper.".format(key))
        self.__dict__[key] = value
