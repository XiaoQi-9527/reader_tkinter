def get_book(name, site):
    """
    书本信息整理
    :param name: 书名
    :param site: 站点
    :return:
    """
    if site == '笔趣阁':
        from source.bqg import get_book_info, get_book_chapters
    elif site == '起点':
        from source.qd import get_book_info, get_book_chapters

    chapters = []
    try:
        book = get_book_info(name, site)
        book = get_book_chapters(book)
        chapter_urls = book.get('章节信息')
        for key in chapter_urls.keys():
            chapters.append(key)
    except Exception as e:
        return {'msg': 404, 'err': str(e)}

    book['章节名信息'] = chapters
    return book


def get_one_chapter(url, site):
    """
    获取单章
    :param url:
    :param site:
    """
    if site == '笔趣阁':
        from source.bqg import get_chapter
    elif site == '起点':
        from source.qd import get_chapter

    try:
        return get_chapter(url, site=site)
    except Exception as e:
        return {'msg': 404, 'err': str(e)}


if __name__ == '__main__':
    # res = get_book('信息全知者', '笔趣阁')
    res = get_book('信息全知者', '起点')
    print(res)
