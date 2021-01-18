from source.bqg import get_book, get_chapter
# import json


def search_info(name, title='笔趣阁'):
    """
    修改图标, 根据不同书源获取书本
    """
    if title == '笔趣阁':
        result = get_book(name)

    # result = json.loads(result)
    # print(result.get('result'))
    return result


def chapter(url):
    """
    根据链接获取正文内容
    :param url: 链接
    """
    return get_chapter(url)


def set_size(window, size):
    """
    设置窗口大小 (长, 宽), 位置 (左上角顶点)
    :param window: 窗口对象
    :param size: '600x200+274+182'
    """
    window.geometry(size)


def set_title(window, title="阅读"):
    """
    设置窗口标题
    """
    window.title(title)


def set_icon(window, icon=None):
    """
    设置窗口图标
    """
    icon = './image/bqg.ico' if icon is None else icon
    window.iconbitmap(icon)

