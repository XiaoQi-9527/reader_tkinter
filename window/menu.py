from window.public import set_title,set_icon
import tkinter as tk
import tkinter.messagebox


def menu(window):
    def bqg():
        set_icon(window)
        set_title(window, "笔趣阁")

    def none():
        set_icon(window, icon='window/image/none.ico')
        set_title(window)

    def more():
        tkinter.messagebox.showwarning(title='提示', message='更多书源敬请期待！')
    # 创建菜单栏
    menubar = tk.Menu(window)

    # 创建一个下拉菜单，然后讲台添加到顶级菜单中
    source_menu = tk.Menu(menubar, tearoff=0)

    # 将上面定义的空菜单命名，放在菜单栏中
    menubar.add_cascade(label='书源选择', menu=source_menu)

    # 加入小菜单
    source_menu.add_command(label="笔趣阁", command=bqg)
    source_menu.add_command(label="空", command=none)

    # 下拉菜单的分隔线
    source_menu.add_separator()

    source_menu.add_command(label="更多", command=more)

    # 显示菜单栏
    window.config(menu=menubar)



