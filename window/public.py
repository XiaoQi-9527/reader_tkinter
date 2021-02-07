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
    # print(result)
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
    icon = 'window/image/bqg.ico' if icon is None else icon
    window.iconbitmap(icon)


def show_context(obj, text, font=('宋体', 11), spacing1=15, spacing2=15, spacing3=10):
    """
    正文展示
    :param obj: 控件对象
    :param text: 正文内容
    :param font: 字体
    :param spacing1: 段间距(与上方)
    :param spacing2: 行间距
    :param spacing3: 段间距(与下方)
    """
    # 解除内容锁定
    obj.configure(state='normal')
    try:
        # 清理之前的内容
        obj.edit_undo()
    except:
        pass
    # 插入内容
    obj.insert("insert", text)
    # 标记正文, '1.0': 第一行第一列, '100000.1000': 最后一行最后一列, 超过计数即为最后
    obj.tag_add('line1', '1.0', '100000.1000')
    # 样式, 每一段的段首缩进
    obj.tag_config('line1', lmargin1=32, font=font, spacing1=spacing1, spacing2=spacing2, spacing3=spacing3)
    # 锁定内容
    obj.configure(state='disabled')


def get_dirs(chapters, page_num):
    """
    章节分页
    :param chapters: 总章节列表
    :param page_num:
    """
    all_page = []
    pages = []
    for index, chapter in enumerate(chapters):
        pages.append(chapter)
        if (index + 1) % 20 == 0:
            all_page.append(pages)
            pages = []
            continue
        if len(all_page) == page_num - 1:
            all_page.append(pages)
    # print(all_page)
    return all_page
