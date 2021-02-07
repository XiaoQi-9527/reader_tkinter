from window.public import set_size, chapter, set_title, get_dirs
from window.read import read_context
import tkinter as tk
import tkinter.messagebox

page_num, text = 1, ''


def show_dirs(window, result, chapters, page, obj, group, book_info, sc=None, mc=None, dc=None):
    """
    展示章节
    :param window:
    :param result:
    :param chapters:
    :param page:
    :param obj:
    :param group:
    :param book_info
    :param sc:
    :param mc:
    :param dc:
    """
    def event0():
        global text
        text = button0['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event1():
        global text
        text = button1['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event2():
        global text
        text = button2['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event3():
        global text
        text = button3['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event4():
        global text
        text = button4['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event5():
        global text
        text = button5['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event6():
        global text
        text = button6['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event7():
        global text
        text = button7['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event8():
        global text
        text = button8['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event9():
        global text
        text = button9['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event10():
        global text
        text = button10['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event11():
        global text
        text = button11['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event12():
        global text
        text = button12['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event13():
        global text
        text = button13['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event14():
        global text
        text = button14['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event15():
        global text
        text = button15['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event16():
        global text
        text = button16['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event17():
        global text
        text = button17['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event18():
        global text
        text = button18['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()

    def event19():
        global text
        text = button19['text']
        context = chapter(book_info.get(text))
        read_context(window, result=result, chapter_name=text, cache=context, sc=sc, mc=mc)
        for c in dc.keys():
            c.destroy()
    chapters = chapters[page-1]

    canvas = obj.Canvas(group, width=360, height=470)
    canvas.place(x=5, y=5)

    button_list = []

    for index, chapter_n in enumerate(chapters):
        chapter_name = obj.StringVar()
        chapter_name.set(chapter_n)
        try:
            if index == 0:
                button0 = obj.Button(group, textvariable=chapter_name, command=event0)
                button_list.append(button0)
            if index == 1:
                button1 = obj.Button(group, textvariable=chapter_name, command=event1)
                button_list.append(button1)
            if index == 2:
                button2 = obj.Button(group, textvariable=chapter_name, command=event2)
                button_list.append(button2)
            if index == 3:
                button3 = obj.Button(group, textvariable=chapter_name, command=event3)
                button_list.append(button3)
            if index == 4:
                button4 = obj.Button(group, textvariable=chapter_name, command=event4)
                button_list.append(button4)
            if index == 5:
                button5 = obj.Button(group, textvariable=chapter_name, command=event5)
                button_list.append(button5)
            if index == 6:
                button6 = obj.Button(group, textvariable=chapter_name, command=event6)
                button_list.append(button6)
            if index == 7:
                button7 = obj.Button(group, textvariable=chapter_name, command=event7)
                button_list.append(button7)
            if index == 8:
                button8 = obj.Button(group, textvariable=chapter_name, command=event8)
                button_list.append(button8)
            if index == 9:
                button9 = obj.Button(group, textvariable=chapter_name, command=event9)
                button_list.append(button9)
            if index == 10:
                button10 = obj.Button(group, textvariable=chapter_name, command=event10)
                button_list.append(button10)
            if index == 11:
                button11 = obj.Button(group, textvariable=chapter_name, command=event11)
                button_list.append(button11)
            if index == 12:
                button12 = obj.Button(group, textvariable=chapter_name, command=event12)
                button_list.append(button12)
            if index == 13:
                button13 = obj.Button(group, textvariable=chapter_name, command=event13)
                button_list.append(button13)
            if index == 14:
                button14 = obj.Button(group, textvariable=chapter_name, command=event14)
                button_list.append(button14)
            if index == 15:
                button15 = obj.Button(group, textvariable=chapter_name, command=event15)
                button_list.append(button15)
            if index == 16:
                button16 = obj.Button(group, textvariable=chapter_name, command=event16)
                button_list.append(button16)
            if index == 17:
                button17 = obj.Button(group, textvariable=chapter_name, command=event17)
                button_list.append(button17)
            if index == 18:
                button18 = obj.Button(group, textvariable=chapter_name, command=event18)
                button_list.append(button18)
            if index == 19:
                button19 = obj.Button(group, textvariable=chapter_name, command=event19)
                button_list.append(button19)
        except Exception as e:
            pass

    for index, button in enumerate(button_list):
        y_site = 5 + index * 24
        button.configure(font=('黑体', 10), fg='black', relief='flat', cursor='hand2')
        button.place(x=10, y=y_site)


def show_director(window, **kwargs):
    global page_num, text

    def back():
        """
        返回搜索结果界面
        """
        from window.middle import mid
        set_title(window, result.get('书源'))
        mid(window, result=result, sc=search_controls)
        for c in dir_controls.keys():
            c.destroy()
        for c in search_controls.keys():
            c.place(**search_controls.get(c))

    def prev():
        """上一页"""
        global page_num
        if page_num == 1:
            tkinter.messagebox.showwarning(title='提示', message='当前为第一页！')
            return
        page_num -= 1
        now_page.set(f'第 {page_num} 页, 共 {pages} 页')
        show_dirs(window, result, chapters, page_num, tk, group1, book_info, sc=search_controls, mc=mid_controls, dc=dir_controls)

    def jump():
        """
        跳转
        """
        global page_num
        # 获取输入的内容
        num = number.get()
        # 判断输入的内容是否符合要求
        try:
            num = int(num)
            num = abs(num)
        except:
            tkinter.messagebox.showwarning(title='提示', message='请填写数字！')
            return
        # 判断是否超出最大章节数
        if num > pages:
            num = pages
            tkinter.messagebox.showwarning(title='提示', message='数值过大，即将转到最后一页！')
        number.set('')
        show_dirs(window, result, chapters, num, tk, group1, book_info, sc=search_controls, mc=mid_controls, dc=dir_controls)

    def next():
        """下一页"""
        global page_num
        if page_num == pages:
            tkinter.messagebox.showwarning(title='提示', message='当前为最后一页！')
            return
        page_num += 1
        now_page.set(f'第 {page_num} 页, 共 {pages} 页')
        show_dirs(window, result, chapters, page_num, tk, group1, book_info, sc=search_controls, mc=mid_controls, dc=dir_controls)
    # 控件列表
    dir_controls = {}
    search_controls = kwargs.get('sc')
    mid_controls = kwargs.get('mc')

    # 接收数据
    result = kwargs.get('result')
    # 背景色
    bg_color = result.get('bg')
    # 书名
    name = result.get('书名')
    # 章节信息
    book_info = result.get('章节信息')
    # 章节名信息
    chapters = result.get('章节名信息')
    # 总页数
    pages = len(chapters) // 20 + 1
    chapters = get_dirs(chapters, pages)

    # 配置
    search_controls = kwargs.get('sc')
    mid_controls = kwargs.get('mc')

    # 设置大小, 标题
    set_size(window, '400x600')
    set_title(window, name)

    # 窗格
    group = tk.LabelFrame(window, text="", padx=2, pady=2, width=390, height=75)
    group.place(x=5, y=5)
    dir_controls[group] = {'x': 5, 'y': 5}

    but_1 = tk.Button(group, text='返回搜索', font=('黑体', 11), fg='black', command=back, relief='groove', cursor='hand2')
    but_1.place(x=300, y=5)
    dir_controls[but_1] = {'x': 300, 'y': 5}
    # 当前页数
    now_page = tk.StringVar()
    now_page.set(f'第 {page_num} 页, 共 {pages} 页')
    lab_3 = tk.Label(group, textvariable=now_page, font=('黑体', 12), fg='black')
    lab_3.place(x=0, y=5)
    dir_controls[lab_3] = {'x': 0, 'y': 5}
    # 总页数
    # chap_text = tk.StringVar()
    # chap_text.set(f'共 {pages} 页'))
    # lab_4 = tk.Label(group, textvariable=chap_text, font=('宋体', 12), fg='black')
    # lab_4.place(x=45, y=5)
    # read_controls[lab_4] = {'x': 45, 'y': 7}

    but_2 = tk.Button(group, text='上一页', font=('黑体', 11), fg='black', command=prev, relief='groove', cursor='hand2')
    but_2.place(x=0, y=35)
    dir_controls[but_2] = {'x': 0, 'y': 35}

    # 输入框, 获取数字
    number = tk.StringVar()
    ent_1 = tk.Entry(group, textvariable=number, font=('黑体', 11), fg='black', width=5)
    ent_1.place(x=160, y=39)
    dir_controls[ent_1] = {'x': 160, 'y': 39}

    but_3 = tk.Button(group, text='跳转', font=('黑体', 11), fg='black', command=jump, relief='groove', cursor='hand2')
    but_3.place(x=215, y=35)
    dir_controls[but_3] = {'x': 215, 'y': 35}

    but_4 = tk.Button(group, text='下一页', font=('黑体', 11), fg='black', command=next, relief='groove', cursor='hand2')
    but_4.place(x=316, y=35)
    dir_controls[but_4] = {'x': 316, 'y': 35}

    # 窗格
    group1 = tk.LabelFrame(window, text="目录", labelanchor='n', padx=2, pady=2, width=380, height=512, container=False)
    group1.place(x=10, y=80)
    dir_controls[group1] = {'x': 10, 'y': 80}

    # 目录显示
    show_dirs(window, result, chapters, page_num, tk, group1, book_info, sc=search_controls, mc=mid_controls, dc=dir_controls)


