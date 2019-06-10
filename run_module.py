import queue
import threading
from mysql_module import LinkMysql
from request_module import Request

from config import *

lock = threading.Lock()
q = queue.Queue()


def run():
    while not q.empty():
        mobile = q.get()
        if request.verify(mobile) is not None:
            lock.acquire()
            mysql.save_mobile(mobile)       # 保存结果
            lock.release()


if __name__ == '__main__':

    mysql = LinkMysql()
    request = Request()

    while mysql.read_page < ENDPAGE:

            print("当前读取页面：%s, 分页大小：%s, 开始页面: %s, 结束页面: %s"
                  % (mysql.read_page, PAGESIZE, STARTPAGE, ENDPAGE))

            lock.acquire()
            mobiles = mysql.get_mobile()  # 获取一页数据
            lock.release()

            for mobile in mobiles[:]:
                q.put(mobile)

            for i in range(THREAD_NUM):
                t = threading.Thread(target=run, )
                t.start()

            mysql.read_page = mysql.read_page + 1

