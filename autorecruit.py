import os
from time import sleep

import airtest.core.android.android
import easyocr
from airtest.core.api import Template, auto_setup, init_device, touch

from TagSelect import recommend_tags
from core import post_processing
from utilities import coordinate_change


class AutoRecruit:
    all_tags = {'狙击干员', '术师干员', '先锋干员', '近卫干员', '重装干员', '医疗干员', '辅助干员', '特种干员', '近战位', '远程位',
                '输出', '支援机械', '防护', '生存', '治疗', '费用回复', '群攻', '减速', '支援', '快速复活', '削弱', '位移', '召唤',
                '控场', '爆发', '新手', '资深干员', '高级资深干员'}

    def __init__(self, device_type):
        self.reader = easyocr.Reader(['ch_sim'], gpu=True, download_enabled=False)
        self.dev = AndroidDevice(device_type)
        self.pth = os.getcwd()


    def recruit(self):
        pass

    def recuitonce(self):
        touch(Template(self.pth + "\\img_data\\+_button.png", record_pos=(-0.247, -0.054), resolution=(1600, 900)))
        sleep(0.5)
        self.dev.snapshot(filename=self.pth + "\\.tmp\\tags.jpg", quality=99)
        tags_info = recommend_tags(self.pth + "\\.tmp\\tags.jpg")
        if tags_info == 400:  # 无特殊情况（指从Tag上看都是2、3星）
            pass
        elif tags_info == 404:  # easyocr识别出错，重新识别
            print("Tag检测错误，正在尝试重新检测")
            return  -1
        elif tags_info == 666:  # 测试过程中还没出现过。。。不保证好用
            print("检测到6星Tag,自动中止脚本运行")
            return 666
        elif tags_info[1] == 1:
            touch(tags_info[0])
        elif tags_info[1] == 9:
            touch(tags_info[0])
            sleep(1)
            touch(Template(self.pth + "\\img_data\\change_recruit_time.png", record_pos=(-0.15, -0.051),
                           resolution=(1600, 900)))
        post_processing()
        sleep(2)
        touch((100, 100))
        sleep(1)
        touch((100, 100))
        sleep(1)

    def select_tags(self, v):
        result = self.reader.readtext(v)
        current_tags = set()
        tag_num = 0
        temp_set = set()
        tag_info = dict()
        for item in result:
            temp_set.add(item[1])
            if item[1] in self.all_tags:
                tag_info[item[1]] = coordinate_change(item[0])  # 包含准备返回的tag信息
                tag_num += 1
                current_tags.add(item[1])
        if tag_num != 5:  # 检测到的tag数量出错
            return 404
        if "高级资深干员" in current_tags:
            return 666
        elif "支援机械" in current_tags:
            return [tag_info["支援机械"], 1]
        elif "资深干员" in current_tags != 0:
            return [tag_info["资深干员"], 9]
        elif current_tags & {"召唤", "控场", "爆发"} != set():
            temp_tag = current_tags & {"召唤", "控场", "爆发"}
            temp = temp_tag.pop()
            return [tag_info[temp], 9]
        elif current_tags & {"特种", "削弱", "快速复活", "支援", "位移"} != set():
            temp_tag = current_tags & {"特种", "削弱", "快速复活", "支援", "位移"}
            temp = temp_tag.pop()
            return [tag_info[temp], 9]
        else:
            return 400


class AndroidDevice(airtest.core.android.android.Android):
    def __init__(self, device_type):
        super().__init__()
        all_device_type = {"蓝叠模拟器": "Android://127.0.0.1:5037", "UU模拟器": "Android://127.0.0.1:5555",
                           "安卓": "Android:///"}
        device_address = all_device_type.get(device_type)
        auto_setup(__file__, devices=[device_address])
        self.dev = init_device(platform="Android", cap_method="JAVACAP")


if __name__ == '__main__':
    autorecruit = AutoRecruit("UU模拟器")
    autorecruit.recuitonce()

