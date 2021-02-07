import tkinter as tk


def button(**kwargs):
    """按钮"""
    group = kwargs.pop("group", None)                   # 父元素
    text = kwargs.pop("text", None)                     # 固定文字
    textvariable = kwargs.pop('textvariable', None)     # 可变文字
    font = kwargs.pop("font", ('黑体', 10))              # 字体样式
    fg = kwargs.pop('fg', 'black')                      # 背景色
    event = kwargs.pop('event', group.quit)             # 绑定事件
    relief = kwargs.pop('relief', 'groove')             # 边框样式
    cursor = kwargs.pop('cursor', 'hand2')              # 鼠标样式
    site = kwargs.pop('site', None)                     # 坐标

    but = tk.Button(group, font=font, fg=fg, command=event, relief=relief, cursor=cursor)

    if text is None:
        but.configure(textvariable=textvariable)
    else:
        but.configure(text=text)

    but.place(**site)


if __name__ == '__main__':
    button()
