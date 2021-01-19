from window.public import set_title, set_icon, set_size
from window.search import search
from window.menu import menu
import tkinter as tk


def main():
    # 初始化
    root = tk.Tk()
    # 设置大小
    set_size(root, '400x100+100+100')
    # 获取默认背景色
    bg = "#%x%x%x" % root.winfo_rgb(root.cget('background'))
    # 设置窗口标题
    set_title(root, title='笔趣阁')
    # 设置图标
    set_icon(root)
    # 创建菜单栏
    menu(root)
    # 搜索界面
    search(root, bg_color=bg)

    # 显示窗口
    root.mainloop()


if __name__ == '__main__':
    main()
