from window.public import set_size, search_info
from window.middle import mid
import tkinter as tk
import tkinter.messagebox


def search(window, **kwargs):
    def submit():
        # 覆盖上一次的结果
        tk.Canvas(window, width=400, height=400, bg=bg).place(x=0, y=60)
        # # 销毁控件
        # for c in search_controls.keys():
        #     c.destroy()
        # 获取当前窗口标题
        title = window.title()
        if title == '阅读':
            tkinter.messagebox.showwarning(title='提示', message='请选择书源！')
            return
        name = book.get()
        if not name:
            tkinter.messagebox.showwarning(title='提示', message='请正确填写书名！')
            return
        # 结果查询
        result = search_info(name, title)
        # print(result)
        # 添加当前默认背景色的字段
        result['bg'] = bg
        if result.get('result') == 404:
            tkinter.messagebox.showwarning(title='提示', message='本书为找到，请检查书名，或者换本书试试吧！')
            return
        # 调用下一层窗口
        mid(window, result=result, sc=search_controls)
    # 背景色
    bg = kwargs.get('bg_color')
    # 设置大小
    set_size(window, '400x100')

    # 窗格, 样式: groove, flat, sunken, raised, ridge
    group1 = tk.LabelFrame(window, text="", padx=2, pady=2, width=390, height=55, relief='groove')
    group1.place(x=5, y=5)

    # 添加标签
    lab_1 = tk.Label(group1, text='书名：', font=('黑体', 15), fg='black')
    lab_1.place(x=0, y=10)
    # 添加输入框
    book = tk.StringVar()
    ent_1 = tk.Entry(group1, textvariable=book, font=('黑体', 15), fg='black', width=20)
    ent_1.place(x=60, y=13)
    # 添加按钮, 样式: flat, groove, raised, ridge, solid, or sunken
    but_1 = tk.Button(group1, text='提交', font=('宋体', 12), fg='black', command=submit, relief='ridge')
    but_1.place(x=280, y=10)
    but_2 = tk.Button(group1, text='退出', font=('宋体', 12), fg='black', command=window.quit, relief='ridge')
    but_2.place(x=330, y=10)
    # 控件列表
    search_controls = {group1: {'x': 5, 'y': 5},
                       lab_1: {'x': 0, 'y': 10},
                       ent_1: {'x': 60, 'y': 13},
                       but_1: {'x': 280, 'y': 10},
                       but_2: {'x': 330, 'y': 10}}



