from urllib import parse
from time import sleep
from bs4 import BeautifulSoup
from utils.thread import MyThread
import requests
import os

# 网站链接
bqg_url = "http://www.biquge.info/"
# 设置请求头
headers = {'referer': 'http://www.biquge.info/',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.88 Safari/537.36'
           }
# 缓存目录
cache_path = './cache/'
img_path = 'window/cache'


# @timeout(limit=5, retry=3, wait=1)
def get_soup(url=None):
    """
    获取网页对象
    :param url: 链接
    """
    sleep(1)
    global headers

    response = requests.get(url=url, headers=headers, timeout=3).content
    return BeautifulSoup(response, 'html.parser')


# @timeout(limit=5, retry=3, wait=1)
def get_chapter(chapter_url):
    """
    单章处理
    :param chapter_url: 单章链接
    """
    soup = get_soup(url=chapter_url)
    try:
        return soup.select("div #content")[0].get_text().replace('    ', '\n').strip()
    except Exception as e:
        return '内容获取失败' + '\n' + str(e) + '\n' + chapter_url


# @timeout(limit=5, retry=3, wait=1)
def get_book(name):
    """
    获取书本信息
    :param name: 书名
    """
    global bqg_url, cache_path
    # 搜索链接
    search_url = bqg_url + 'modules/article/search.php?searchkey={0}'

    # 对名字进行 URL 编码
    new_name = parse.quote(name)

    # 搜索结果处理, 获取书本代码
    soup = get_soup(url=search_url.format(new_name))
    # print(soup.prettify())
    try:
        select = soup.select(".odd")
        book_code = select[0].select("a[href]")[0]['href']
        writer = select[1].get_text()
    except Exception as e:
        return {'result': 404, 'err': str(e)}
    # 书本链接
    book_url = bqg_url + book_code

    # 章节处理, 对应 章节名 与 链接
    soup = get_soup(url=book_url)
    # print(soup.prettify())

    # 文章简介
    summary = soup.select('[property="og:description"]')[0]['content'].replace('<br/><br/>', '\n')

    # 封面缓存
    cover_url = soup.select('[id="fmimg"]')[0].select('img')[0]['src']
    cover_file = requests.get(cover_url).content

    # 保存书本信息的目录
    book_path = os.path.join(cache_path, name)
    if not os.path.exists(book_path):
        os.makedirs(book_path)
    # 保存封面的路径
    cover_path = os.path.join(book_path, name+'.jpg')
    # if not os.path.exists(cover_path):
    #     open(cover_path, "wb").write(cover_file)

    cover_path = cover_path.replace('\\', '/')

    # 章节信息, 章名: 链接
    links = soup.select("a[title]")
    # 章节信息, 章节名信息
    book_info, chapter_list = {}, []
    for link in links:
        title = link['title']
        book_info[title] = book_url + link['href']
        chapter_list.append(title)
    cha_cache = {'第一章': chapter_list[0], '最后一章': chapter_list[-1]}
    # # chapter_00 = get_chapter(chapter_list[0])
    # # chapter_01 = get_chapter(chapter_list[-1])
    for key, value in cha_cache.items():
        url = book_info.get(value)
        t = MyThread(target=get_chapter, name=str(key), args=(url,))
        # print(t.getName())
        t.setDaemon(True)  # 设置守护
        t.start()  # 启动
        t.join()  # 设置主线程等待
        cha_cache[key] = t.result

    result = {'result': 200, '书源': '笔趣阁',
              '书名': name,
              '作者': writer, '简介': summary, '封面': cover_path,
              '章节信息': book_info, '章节名信息': chapter_list, '缓存': cha_cache}
    return result


def chapter_cache(book_data, now_chapter, total=10):
    """
    章节缓存
    :param book_data: 书本数据
    :param now_chapter: 当前章节名
    :param total: 缓存章节数
    """
    chapter_link = book_data.get('章节信息')
    chapter_list = []
    chapter_info = {}
    for chapter in chapter_link.keys():
        chapter_list.append(chapter)
    try:
        index = chapter_list.index(now_chapter) + 1
        new_chapter_list = chapter_list[index: index+total]
    except Exception as e:
        return {'result': '缓存失败', 'err': str(e)}
    for i in new_chapter_list:
        chapter_url = chapter_link.get(i)
        t = MyThread(target=get_chapter, name=str(i), args=(chapter_url,))
        # print(t.getName())
        t.setDaemon(True)  # 设置守护
        t.start()  # 启动
        t.join()  # 设置主线程等待
        chapter_info[i] = t.result
    return {'result': 'ok', '数据': chapter_info}


if __name__ == '__main__':
    res = get_book('信息全知者')
    print(res)
    # get_chapter()
    # res = chapter_cache(res, '第七章 怪拳', 5)
    # print(res)
