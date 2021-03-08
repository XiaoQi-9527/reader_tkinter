from utils.website import search, get_soup


def get_book_info(name, site):
    """
    获取书本信息
    :param name: 书名
    :param site: 站点名称
    """

    url, result = search(name, site=site)
    # print(result.prettify())
    try:
        result1 = result.select(".odd")
        # print(result1)
        # 书本代码
        # book_code = result1[0].select("a[href]")[0]['href']
        for i in range(len(result1)):
            try:
                text = result1[i].select("a[href]")[0].get_text()
                if text == name:
                    book_code = result1[i].select("a[href]")[0]['href']
                    # print(book_code)
                    break
            except:
                pass
        # 作者
        writer = result1[1].get_text()
        result2 = result.select(".even")
        # 最新章节
        new_chapter = result2[0].select("a")[0].get_text()
        # 状态
        status = result2[-1].get_text()

        return {'msg': 200, '书源': site, '书名': name, '作者': writer, '状态': status,
                '书本链接': url + book_code, '最新章节': new_chapter}

    except Exception as e:
        raise e


def get_book_chapters(book):
    """
    获取章节信息
    :param book: 书本信息
    :param site: 站点
    """
    name = book.get('书名')
    url = book.get('书本链接')
    site = book.get('书源')
    site_url, result = search(name, url=url, site=site)
    # 简介
    summary = result.select('[property="og:description"]')[0]['content'].replace('<br/><br/>', '\n')
    # print(result.prettify())
    chapters = {}
    try:
        a_tags = result.select("a[title]")
        # print(a_tags)
        for a_tag in a_tags:
            href = url + a_tag.get("href")
            # title = a_tag["title"]
            title = a_tag.get("title")
            # print(href, title)
            chapters[title] = href
    except Exception as e:
        raise e

    book['简介'] = summary
    book['章节信息'] = chapters
    return book


def get_chapter(url, site):
    """
    获取单章
    :param url:
    :param site:
    """
    result = get_soup(url, site=site)
    # print(result.prettify())
    try:
        return result.select('div[id="content"]')[0].get_text().replace('    ', '\n').strip()
    except Exception as e:
        raise e


if __name__ == '__main__':
    res = get_book_info('信息全知者', '笔趣阁')
    # res = get_book_info('赘婿', '笔趣阁')
    # res = get_chapters_dict(res, '笔趣阁')
    # res = get_book('信息全知者', '笔趣阁')
    # test_url = 'http://www.biquge.info//82_82472/23390256.html'
    # res = get_chapter(test_url, '笔趣阁')
    print(res)


