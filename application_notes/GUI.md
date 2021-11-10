# Python GUI 程序设计
## GUI工具包简介
## GUI编程步骤
1. 安装和导入GUI工具包
2. 创建一个顶层窗口对象，它包含着整个GUI应用程序
3. 在创建顶层窗口内部制作GUI应用程序的一些部件，包括控件、标签、文本框、菜单等等
4. 把这些GUI部件与应用程序代码结合起来，以事件驱动，然后把控件放在窗口合适位置
5. 进入主事件循环（mainloop()）
## tkinter模块使用
1. import tkinter
2. window = tkinter.Tk()
3. label = tkinter.Label(window, text='')
4. label.pack()
5. window.mainloop()
## wxPython模块使用
## 弹子球游戏示例
[BounceBall.py](example_code/BounceBalls.py)
## 贪吃蛇游戏示例
[SnakeGame.py](example_code/SnakeGame.py)