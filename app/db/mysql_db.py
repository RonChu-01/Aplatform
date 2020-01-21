# -*- coding: utf-8 -*-
# Created by #chuyong, on 2020/1/20.
# Copyright (c) 2019 3KWan.
# Description :

import pymysql

from app.libs.logger import Logger

logger = Logger("MysqlDB")


class MysqlDB:
    """  mysql数据库操作类 """

    # 数据库配置信息
    _db_info = {
        "host": "",
        "user": "",
        "password": "",
        "database": "",
        "port": 3306
    }

    def __init__(self, host, user, password, database, port=3306):
        """
            ps: 进行数据库操作，需手动建立连接和断开连接

        :param host:
        :param user:
        :param password:
        :param database:
        :param port:
        """
        self._db_info["host"] = host
        self._db_info["user"] = user
        self._db_info["password"] = password
        self._db_info["database"] = database
        self._db_info["port"] = port

        self.conn = None
        self.cursor = None

    def connect(self):
        """  获取数据库连接 """
        try:
            self.conn = pymysql.connect(**self._db_info)  # 建立连接
        except pymysql.Error as e:
            logger.error("-> connect to mysql error {}.".format(str(e)))
        else:
            self.cursor = self.conn.cursor()  # 获取游标对象

    def make_table(self):
        pass

    def __item(self, sql, params=None):
        """
            数据库操作（抽离）

        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        """
        count = 0  # 受影响的行数
        try:
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            logger.error("-> 执行数据库操作失败 {}".format(str(e)))
        finally:
            self.close()
        return count

    def insert(self, sql, params=None):
        """  增 """
        self.__item(sql, params)

    def delete(self, sql, params=None):
        """ 删 """
        self.__item(sql, params)

    def update(self, sql, params=None):
        """  改 """
        self.__item(sql, params)

    def select_one(self, sql, params=None):
        """  查寻一条记录 """

        result_one = None

        try:
            count = self.cursor.execute(sql, params)
            if count != 0:
                result_one = self.cursor.fetchone()
        except Exception as e:
            logger.error("-> select one failed {}.".format(str(e)))
        finally:
            self.close()

        return result_one

    def select_all(self, sql, params=None):
        """  查寻全部记录 """

        result_all = None

        try:
            count = self.cursor.execute(sql, params)
            if count != 0:
                result_all = self.cursor.fetchall()
        except Exception as e:
            logger.error("-> select all failed {}.".format(str(e)))
        finally:
            self.close()

        return result_all

    def close(self):
        """  断开连接 """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    # def __del__(self):
    #     """  析构函数 """
    #     if self.cursor:
    #         self.cursor.close()
    #     if self.conn:
    #         self.conn.close()


if __name__ == '__main__':
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "chuy5945",
        "database": "k_platform"
    }
    m_db = MysqlDB(**config)
    m_db.connect()
    # sql_ = "CREATE TABLE IF NOT EXISTS blog(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))"
    # m_db.cursor.execute(sql_)
    # m_db.conn.commit()
    # m_db.insert("insert into blog(name, title) values(%s, %s)", ("ron", "hello"))
    # results = m_db.select_all("select * from blog where name = %s", ("ron", ))
    # print("全部结果 -> {}".format(results))
    # for index, result in enumerate(results):
    #     print("第 {} 行数据 -> {}".format(index, result))
