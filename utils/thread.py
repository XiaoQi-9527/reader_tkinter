# from threading import _newname
from time import sleep, strftime
import threading
import random


class MyThread(threading.Thread):
    """创建有返回值的线程任务"""

    # def __init__(self, target=None, args=None, kwargs=None):
    def __init__(self, target=None, name=None, args=(), kwargs=None):
        super(MyThread, self).__init__()
        self.fn = target  # 任务名
        num = f'thread{strftime("%S") + str(random.randint(1, 99)).zfill(2)}'
        self.name = str(name) if name is not None else num  # 线程名
        self.args = args  # 元祖传参
        self.kwargs = kwargs  # 字典传参
        self.result = None  # 返回结果

    def run(self):
        try:
            if self.fn:
                self.result = self.fn(*self.args)  # 添加返回值
        finally:
            del self.fn, self.args, self.kwargs


def timeout(limit=30, retry=1, wait=0):
    """
    超时重试
    :param limit: 限制时间
    :param retry: 重试次数
    :param wait: 等待间隔
    """

    def outer(fn):
        def inner(*args, **kwargs):
            for i in range(retry):
                try:
                    t = MyThread(target=fn, name=f'thread{str(i + 1).zfill(2)}', args=args, kwargs=kwargs)
                    # print(t.getName())
                    t.setDaemon(True)  # 设置守护
                    t.start()  # 启动
                    t.join(limit)  # 设置主线程等待
                    if t.is_alive():  # 判断是否执行成功
                        raise TimeoutError
                    else:
                        return t.result
                except Exception as e:
                    if i == retry - 1:
                        raise e
                    sleep(wait)

        return inner

    return outer


if __name__ == "__main__":
    @timeout(limit=30, retry=2, wait=3)
    def func(a, b):
        sleep(3)
        print(a, b)
        print('ok')
        return a


    print(func(1, 2))
