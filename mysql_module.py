import pymysql
import warnings
warnings.filterwarnings("ignore")

from config import *


class LinkMysql(object):
    def __init__(self):
        self.link_mysql()
        self.check_table()
        self.read_page = STARTPAGE

    def link_mysql(self):
        try:
            self.conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("\n数据库连接失败：%s\n请检查MYSQL配置！\n" % e)

    def check_table(self):
        sql = "CREATE TABLE IF NOT EXISTS %s" % SAVE_TABLE + \
              "(id INT (11) AUTO_INCREMENT, mobile VARCHAR(11), " \
              "PRIMARY KEY(id), UNIQUE KEY `mobile` (`mobile`) USING BTREE); "
        self.cursor.execute(sql)

    def get_mobile(self):
        sql = "SELECT %s" % COLUMN + " FROM %s" % TABLE + " LIMIT %s, %s; " % \
                (self.read_page * PAGESIZE, PAGESIZE)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()  # 读取结果

        mobiles = []
        for result in results:      # 清洗数据
            mobile = result[0]        # 取(10086,)第一元
            if mobile is not None:
                if len(mobile) == 11:
                    mobiles.append(mobile)
                elif len(mobile) > 11:
                    mobiles.append(mobile.strip()[-11:])    # 后11位

        return mobiles

    def save_mobile(self, mobile):
        try:
            sql = "INSERT IGNORE INTO %s" % SAVE_TABLE + "(mobile) VALUES(%s)" % mobile
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print("保存失败：", e)