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
        select = result.select('li[class="res-book-item"]')[0]
        select0 = select.select('div[class="book-img-box"]')[0]
        img_src = select0.select('img')[0]['src']
        book_code = select0.select('a')[0]['href']
        select1 = select.select('div[class="book-mid-info"]')[0]
        select2 = select1.select('p[class="author"]')[0]
        writer = select2.select('a')[0].get_text()
        status = select2.select('span')[0].get_text()
        new_chapter = select1.select('p[class="update"]')[0].select('a')[0].get_text()
        introduction = select1.select('p[class="intro"]')[0].get_text().replace(' ', '')

        return {'msg': 200, '书源': site, '书名': name, '书本链接': 'https:' + book_code, '作者': writer, '状态': status,
                '封面': 'https:' + img_src, '最新章节': new_chapter, '简介': introduction}
    except Exception as e:
        raise e


def get_book_chapters(book):
    """
    获取章节信息
    :param book: 书本信息
    :param site: 站点
    """
    name = book.get('书名')
    url = book.get('书本链接') + "#Catalog"
    site = book.get('书源')
    site_url, result = search(name, url=url, site=site)
    # print(result.prettify())
    chapters = {}
    try:
        a_tags = result.select('a[data-cid]')
        for a_tag in a_tags:
            # print(a_tag)
            href = 'https:' + a_tag.get("href")
            title = a_tag.get_text()
            # print(href, title)
            chapters[title] = href
    except Exception as e:
        raise e

    book['章节信息'] = chapters
    return book


def get_chapter(url, site):
    try:
        site_url, result = get_soup(url, site)
        # print(result)
        p_tags = result.select('div[class="read-content j_readContent"]')[0].select('p')
        con_list = []
        for p_tag in p_tags:
            # print(p_tag)
            con_list.append(p_tag.get_text().strip())
        return '\n'.join(con_list)
    except Exception as e:
        raise e


if __name__ == '__main__':
    res = get_book_info('信息全知者', '起点')
    # res = get_chapters_dict(res, '起点')
    # res = get_book('信息全知者', '起点')
    # test_url = 'https://read.qidian.com/chapter/ZQGodBOIkVJtl3KA8Mw5oQ2/vgNKUnoX7dzwrjbX3WA1AA2'
    # vip_url = 'https://vipreader.qidian.com/chapter/1019222135/632566366'
    # res = get_chapter(test_url, '起点')
    print(res)
