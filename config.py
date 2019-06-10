
"""
    通用批量请求工具 V1.0 2019-06-10 00: 00

"""

""" 1. 请求设置 """

# ----- 1.1 请求地址
URL = "https://login.api.guxiansheng.cn/index.php?c=verification&a=send"

# ----- 1.2 请求头 注意不与上下引号同行
HEADERS = """
Host: login.api.guxiansheng.cn
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Connection: keep-alive
Accept: */*
User-Agent: MrStock/3.0.8 (iPhone; iOS 12.2; Scale/3.00)
Accept-Language: zh-Hans-CN;q=1, bo-CN;q=0.9
iOS-Head: size=375*812
Accept-Encoding: br, gzip, deflate
"""

# ----- 1.3 POST 请求设置
FORM = "mobile=15358936986&pattern=0&type=2"       # 请求数据
KEY_FIELD = "mobile"        # 请求体中需批量处理的字段，如：mobile、phone等

# ----- 1.4 GET 请求设置 ------
# TODO 待完善
QUERY_FILED = "phone"      # 请求URL中的批量处理字段，如：https://xxx.com?phone=138xxx 中的 phone字段

""" """

""" 2. 响应设置 """

# ----- 2.1 视为成功的json数据，保存结果的判断条件
SUCCEED_JSON = {'code': 1, 'message': 'ok', 'data': 1}

# ----- 2.2 视为失败的json数据
IGNORE_JSON = {'code': -1, 'message': '该手机号还未注册'}

""" """

""" 3. 数据库设置 """

# ----- 3.1 主机连接信息
HOST      = "139.9.52.22"
PORT      = 6789
USER      = "jrj"
PASSWORD  = "jrjwu"

# ----- 3.2 数据库和表，没有将自动创建
DATABASE  = "youshua"       # 读取数据库
TABLE     = "you1"          # 读取表
COLUMN    = "mobile"        # 读取字段

# ----- 3.3 批量读取页面设置
STARTPAGE = 0            # 开始页面
ENDPAGE   = 1            # 结束页面
PAGESIZE  = 110000           # 每页数量

# ----- 3.4 保存结果表名
SAVE_TABLE = "xxx_registered"

""" """

""" 4. 其他设置 """
# ----- 4.1 线程设置
THREAD_NUM = 20

# ----- 4.2 打印设置
OUT_PRINT = 0           # 1: 只显示成功结果  0: 显示所有结果

# ----- 4.1 状态码异常重试
RETRY_403  = 1          # 重试403请求

""" """