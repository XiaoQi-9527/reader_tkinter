from window.public import set_size, chapter, set_title, show_context
import tkinter as tk
import tkinter.messagebox

# 章节名
context_name = ''


def read_context(window, **kwargs):
    global context_name

    def back():
        """
        返回搜索结果界面
        """
        from window.middle import mid
        canvas = tk.Canvas(window, width=400, height=320)
        canvas.place(x=0, y=60)
        set_title(window, result.get('书源'))
        mid(window, result=result, sc=search_controls)
        for c in read_controls.keys():
            c.destroy()
        for c in search_controls.keys():
            c.place(**search_controls.get(c))

    def get_index():
        """
        根据章节名获取下标, 并章节列表总长
        """
        global context_name
        index = chapters.index(context_name)
        length = len(chapters)
        return index, length

    def next():
        """
        下一章
        """
        global context_name
        index, length = get_index()
        # 判断是否为最后一章
        if index == length - 1:
            tkinter.messagebox.showwarning(title='提示', message='当前为最新章节！')
            return
        # 获取下一章的章节名
        context_name = chapters[index + 1]
        # 设置显示的章节名
        chap_text.set(context_name)
        # 获取本章的链接
        url = book_info.get(context_name)
        # 获取正文内容
        text = chapter(url)
        # 展示正文内容
        show_context(t1, text)

    def prev():
        """
        上一章
        """
        global context_name
        index, length = get_index()
        if index == 0:
            tkinter.messagebox.showwarning(title='提示', message='当前为第一章！')
            return
        context_name = chapters[index - 1]
        chap_text.set(context_name)
        url = book_info.get(context_name)
        text = chapter(url)
        show_context(t1, text)

    def jump():
        """
        跳转
        """
        global context_name
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
        if num > len(chapters) - 1:
            num = len(chapters) - 1
            tkinter.messagebox.showwarning(title='提示', message='数值过大，即将转到最新章节！')
        context_name = chapters[num]
        chap_text.set(context_name)
        url = book_info.get(context_name)
        text = chapter(url)
        number.set('')
        show_context(t1, text)

    # 控件列表
    read_controls = {}
    search_controls = kwargs.get('sc')
    mid_controls = kwargs.get('mc')

    # 接收数据
    result = kwargs.get('result')
    # 背景色
    bg_color = result.get('bg')
    # 书名
    name = result.get('书名')
    # 首次进入章节名
    context_name = kwargs.get('chapter_name')
    # 章节缓存
    if kwargs.get('show') is None:
        cache = kwargs.get('cache')
    else:
        cache = result.get('缓存').get(kwargs.get('show'))
    # 章节信息
    book_info = result.get('章节信息')
    # 章节名信息
    chapters = result.get('章节名信息')

    # 设置大小, 标题
    set_size(window, '400x600')
    set_title(window, name)

    # 窗格
    group = tk.LabelFrame(window, text="", padx=2, pady=2, width=390, height=75)
    group.place(x=5, y=5)
    read_controls[group] = {'x': 5, 'y': 5}

    but_1 = tk.Button(group, text='返回搜索', font=('黑体', 11), fg='black', command=back, relief='groove', cursor='hand2')
    but_1.place(x=300, y=5)
    read_controls[but_1] = {'x': 300, 'y': 5}

    lab_3 = tk.Label(group, text='章节：', font=('黑体', 12), fg='black')
    lab_3.place(x=0, y=5)
    read_controls[lab_3] = {'x': 0, 'y': 5}
    # 当前章节名
    chap_text = tk.StringVar()
    chap_text.set(context_name)
    lab_4 = tk.Label(group, textvariable=chap_text, font=('宋体', 10), fg='black')
    lab_4.place(x=45, y=7)
    read_controls[lab_4] = {'x': 45, 'y': 7}

    but_2 = tk.Button(group, text='上一章', font=('黑体', 11), fg='black', command=prev, relief='groove', cursor='hand2')
    but_2.place(x=0, y=35)
    read_controls[but_2] = {'x': 0, 'y': 35}

    # 输入框, 获取数字
    number = tk.StringVar()
    ent_1 = tk.Entry(group, textvariable=number, font=('黑体', 11), fg='black', width=5)
    ent_1.place(x=160, y=39)
    read_controls[ent_1] = {'x': 160, 'y': 39}

    but_3 = tk.Button(group, text='跳转', font=('黑体', 11), fg='black', command=jump, relief='groove', cursor='hand2')
    but_3.place(x=215, y=35)
    read_controls[but_3] = {'x': 215, 'y': 35}

    but_4 = tk.Button(group, text='下一章', font=('黑体', 11), fg='black', command=next, relief='groove', cursor='hand2')
    but_4.place(x=316, y=35)
    read_controls[but_4] = {'x': 316, 'y': 35}

    # 窗格
    group1 = tk.LabelFrame(window, text="正文", labelanchor='n', padx=2, pady=2, width=380, height=512, container=False)
    group1.place(x=10, y=80)
    read_controls[group1] = {'x': 5, 'y': 5}

    # 竖直滚动条
    s1 = tk.Scrollbar(window, orient='vertical', width=20)
    s1.place(x=365, y=95, height=490)
    read_controls[s1] = {'x': 365, 'y': 95}

    # 文本框设置
    t1 = tk.Text(window, width=49, height=37, wrap='char', relief='flat', bg=bg_color, undo=True)  # state='disabled'
    t1.place(x=15, y=98)
    read_controls[t1] = {'x': 15, 'y': 98}

    # 绑定文本框与滚动条
    t1.config(yscrollcommand=s1.set)
    s1.config(command=t1.yview)

    # 正文显示
    show_context(t1, cache)
