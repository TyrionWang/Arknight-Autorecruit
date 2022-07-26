import os
from time import sleep

from airtest.core.api import Template
from airtest.core.api import touch

from TagSelect import *


def post_processing():
    pth = os.getcwd()+"img_data"
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


def auto_recruit(dev):
    pth = os.getcwd()+"img_data"
    while True:
        touch(Template(pth + "\\img_data\\+_button.png", record_pos=(-0.247, -0.054), resolution=(1600, 900)))
        sleep(0.5)
        dev.snapshot(filename=pth + "\\.tmp\\tags.jpg", quality=99)
        tags_info = recommend_tags(pth + "\\.tmp\\tags.jpg")
        if tags_info == 404:  # easyocr出错，重新识别
            continue
        if tags_info == 400:
            pass
        elif tags_info[1] == 1:
            touch(tags_info[0])
        elif tags_info[1] == 9:
            touch(tags_info[0])
            sleep(1)
            touch(Template(pth + "\\change_recruit_time.png", record_pos=(-0.15, -0.051), resolution=(1600, 900)))
        post_processing()
        sleep(2)
        touch((100, 100))
        sleep(1)
        touch((100, 100))
        sleep(1)
