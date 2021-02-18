from config.headers import headers
from config.urls import urls
from urllib import parse
from bs4 import BeautifulSoup
import requests


def bs(**kwargs):
    """
    获取网页对象
    """
    link = kwargs.get("url")
    site = kwargs.get('site', '起点')

    url = urls.get(site)[0]
    headers['referer'] = url
    try:
        if site in ['代理']:
            return BeautifulSoup(requests.get(url=link, headers=headers, timeout=5).content, "lxml")
        elif site in ['起点']:
            return BeautifulSoup(requests.get(url=link, headers=headers, timeout=5).content, "html5lib")
        else:
            return BeautifulSoup(requests.get(url=link, headers=headers, timeout=5).content, "lxml")
    except Exception as e:
        print(e)
        return None


def get_soup(url=None, site=None):
    """
    访问网页结果处理
    :param url: 链接
    :param site: 站点
    """
    return bs(url=url, site=site)


def search(name, url=None, site=None):
    """
    搜索书本
    :param name: 书名
    :param url: 书本链接
    :param site: 站点信息
    """
    site = "起点" if site is None else site
    # 从配置文件获取站点信息
    source = urls.get(site)
    if url is None:
        # 搜索链接
        search_link = source[1]
        # 对书名进行 url 编码
        name = parse.quote(name)
        # 搜索链接拼接
        this_link = search_link.format(name)
    else:
        this_link = url
    # 链接
    url = source[0]

    return url, get_soup(this_link, site)


