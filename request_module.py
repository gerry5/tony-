import requests
import json
import queue
import threading
from mysql_module import LinkMysql

from config import *


class Request(object):
    def __init__(self):
        self.format_url()
        self.format_headers()
        self.format_form()
        self.session = requests.session()

    def format_url(self):
        self.url = ''

        # 判断get方式的 phone= 是否出现在url中
        if QUERY_FILED + "=" in URL:
            self.method = "GET"
            # self.url =          # TODO 格式化字符串
        else:
            self.method = "POST"
            self.url = URL.strip()      # url不变

    def format_headers(self):
        self.headers = {}

        header_lines = HEADERS.strip().split("\n")
        for header_line in header_lines:
            header_key = header_line.split(":")[0].strip()
            header_value = header_line.split(":")[1].strip()

            # 筛选过滤
            if header_key.lower() == "content-length":
                continue
            elif header_key.lower() == "connection":
                header_value = "close"      # 请求完成，立即关闭连接

            self.headers[header_key] = header_value

        # print(self.headers)   # 调试点

    def format_form(self):
        self.form = {}

        datas = FORM.strip().split("&")
        for data in datas:
            form_key = data.split("=")[0]
            form_value = data.split("=")[1]

            if form_key == KEY_FIELD:
                form_value = ''         # 关键字段置空，待从数据库读取填充

            self.form[form_key] = form_value

        # print(self.form)        # 调试点

    def verify(self, mobile):

        # if self.method == "POST":     # TODO GET请求
        self.form[KEY_FIELD] = mobile       # 更新表单请求内容

        try:
            r = self.session.post(self.url, data=self.form, headers=self.headers)

            if r.status_code == 200:

                try:
                    r = json.loads(r.text)
                    if r == SUCCEED_JSON:
                        print(mobile)

                        return mobile

                    else:
                        if OUT_PRINT == 0:
                            print(mobile, r)

                except Exception:
                    print("请求结果解析为json格式异常", r.text)

            else:
                if OUT_PRINT == 0:
                    print("状态码异常", r.status_code)
                if RETRY_403:
                    self.verify(mobile)

        except Exception as e:
            print("请求出错", self.method, e)


if __name__ == '__main__':
    r = Request()