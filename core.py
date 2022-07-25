import os
from time import sleep

from airtest.core.api import Template
from airtest.core.api import touch

from TagSelect import *


def post_processing():
    pth = os.getcwd()+"\\img_data"
    touch(Template(pth + "\\confirm_cruit_botton.png", record_pos=(0.261, 0.173), resolution=(1600, 900)))
    sleep(2)
    touch(Template(pth + "\\start_recruit_button.png", record_pos=(-0.131, 0.014), resolution=(1600, 900)))
    sleep(2)
    touch(Template(pth + "\\confirm_excess_button.png", record_pos=(0.248, 0.116), resolution=(1600, 900)))
    sleep(2)
    touch(Template(pth + "\\confirm_recruit_button.png", record_pos=(-0.251, 0.016), resolution=(1600, 900)))
    sleep(2)
    touch(Template(pth + "\\skip_button.png", record_pos=(0.458, -0.25), resolution=(1600, 900)))
    sleep(2)


def auto_recruit(dev, reader):
    pth = os.getcwd()
    while True:
        touch(Template(pth + "\\img_data\\+_button.png", record_pos=(-0.247, -0.054), resolution=(1600, 900)))
        sleep(0.5)
        dev.snapshot(filename=pth + "\\.tmp\\tags.jpg", quality=99)
        tags_info = recommend_tags(pth + "\\.tmp\\tags.jpg", reader)
        if tags_info == 400:  # 无特殊情况（指从Tag上看都是2、3星）
            pass
        elif tags_info == 404:  # easyocr识别出错，重新识别
            print("Tag检测错误，正在尝试重新检测")
            continue
        elif tags_info == 666:  # 测试过程中还没出现过。。。不保证好用
            print("检测到6星Tag,自动中止脚本运行")
            break
        elif tags_info[1] == 1:
            touch(tags_info[0])
        elif tags_info[1] == 9:
            touch(tags_info[0])
            sleep(1)
            touch(Template(pth + "\\img_data\\change_recruit_time.png", record_pos=(-0.15, -0.051), resolution=(1600, 900)))
        post_processing()
        sleep(2)
        touch((100, 100))
        sleep(1)
        touch((100, 100))
        sleep(1)
