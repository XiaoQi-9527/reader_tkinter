from window.public import set_size, chapter
from window.read import read_context
import tkinter as tk


def mid(window, **kwargs):
    def last():
        """
        打开最后一章
        """
        read_context(window, result=result, chapter_name=new_cha, show='最后一章', sc=search_controls, mc=mid_controls)
        for c in mid_controls.keys():
            c.destroy()
        for c in search_controls.keys():
            c.place_forget()

    def first():
        """
        打开第一章
        """
        read_context(window, result=result, chapter_name=fir_cha, show='第一章', sc=search_controls, mc=mid_controls)
        for c in mid_controls.keys():
            c.destroy()
        for c in search_controls.keys():
            c.place_forget()
    # 控件列表
    mid_controls = {}
    search_controls = kwargs.get('sc')

    # 设置大小
    set_size(window, '400x300')
    # 接收数据
    result = kwargs.get('result')
    # 数据判断, 简介
    summary = result.get('简介')
    summary = '加载失败' if summary is None else summary
    # 第一章, 最新章节名
    cache = result.get('章节名信息')
    # # 获取第一章与最后一章
    # cache = result.get('缓存')
    # print(cache)
    fir_cha = '暂无数据' if cache is None else cache[0]
    fir_cha = cache[0]
    new_cha = '暂无数据' if cache is None else cache[-1]
    new_cha = cache[-1]
    # 作者
    writer = result.get('作者')
    writer = '佚名' if writer is None else writer
    # # 封面保存路径
    # title_path = result.get('封面')

    # # 封面控件
    # group1 = tk.LabelFrame(window, text="", padx=0, pady=0, width=188, height=248, relief='groove')
    # group1.place(x=5, y=60)
    # try:
    #     image_file = ImageTk.PhotoImage(file=title_path)
    #     cover = tk.Label(group1, image=image_file)
    #     cover.place(x=0, y=0)
    # except Exception as e:
    #     print(e)
    #     tk.Label(group1, text='封面', font=('黑体', 20), fg='black').place(x=60, y=100)

    # 信息控件
    lab_1 = tk.Label(window, text='作者：', font=('黑体', 12), fg='black')
    lab_1.place(x=10, y=60)
    mid_controls[lab_1] = {'x': 10, 'y': 60}
    # 作者
    wri_text = tk.StringVar()
    wri_text.set(writer)
    lab_2 = tk.Label(window, textvariable=wri_text, font=('宋体', 11), fg='black')
    lab_2.place(x=55, y=62)
    mid_controls[lab_2] = {'x': 55, 'y': 62}

    lab_3 = tk.Label(window, text='简介：', font=('黑体', 12), fg='black')
    lab_3.place(x=10, y=90)
    mid_controls[lab_3] = {'x': 10, 'y': 90}
    # 简介
    mid_text = tk.StringVar()
    mid_text.set(summary)
    mes_1 = tk.Message(window, textvariable=mid_text, font=('宋体', 11), fg='black', width=320, justify='left')
    mes_1.place(x=50, y=92)
    mid_controls[mes_1] = {'x': 50, 'y': 90}

    but_1 = tk.Button(window, text='最新章节', font=('宋体', 10), fg='black', command=last, relief='ridge')
    but_1.place(x=10, y=270)
    mid_controls[but_1] = {'x': 10, 'y': 270}
    # 章节名
    new_chapter = tk.StringVar()
    new_chapter.set(new_cha)
    lab_4 = tk.Label(window, textvariable=new_chapter, font=('黑体', 10), fg='black')
    lab_4.place(x=90, y=272)
    mid_controls[lab_4] = {'x': 90, 'y': 270}

    but_2 = tk.Button(window, text='开始阅读', font=('宋体', 10), fg='black', command=first, relief='ridge')
    but_2.place(x=330, y=270)
    mid_controls[but_2] = {'x': 330, 'y': 270}
