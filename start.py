import tkinter as tk
from threading import Thread
from tkinter import ttk

import airtest.core.android.android

from connect import *
from main import *


class AndroidDevice(airtest.core.android.android.Android):
    def __init__(self, device_type):
        super().__init__()
        main_frame.text.insert('insert', "正在连接" + device_type + "\n")
        self.dev = connect_device(device_type)


def device_select(device_type):
    if device_type == 'ios':
        pass
    else:
        global current_device
        current_device = AndroidDevice(device_type)


def recruit():
    global current_device
    t1 = Thread(target=auto_recruit, args=(current_device.dev,))
    t1.start()


if __name__ == "__main__":
    global current_device
    root = tk.Tk()
    root.config(bg='#000000')
    root.title("舟游自动招募")
    root.geometry('400x250+200+200')
    # noinspection PyTypeChecker
    root.resizable(0, 0)
    main_frame = tk.Frame(root)
    main_frame.pack()
    main_frame.cbox = ttk.Combobox(main_frame, width=30)
    main_frame.cbox['value'] = ('安卓', 'ios', 'UU模拟器', '蓝叠模拟器')
    main_frame.cbox.current(0)
    main_frame.cbox.grid(row=0, column=0, sticky='sn')
    main_frame.connect_button = tk.Button(main_frame, text="连接", command=lambda: device_select(main_frame.cbox.get()))
    main_frame.connect_button.grid(row=0, column=1)
    main_frame.start_button = tk.Button(main_frame, text="开始自动招募", command=lambda: recruit())
    main_frame.start_button.grid(row=0, column=2)
    main_frame.text = tk.Text(main_frame, width=55, height=18)
    main_frame.text.grid(row=1, column=0, columnspan=3)
    root.mainloop()
