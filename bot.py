import airtest.core.android.android
import logging
import json
import easyocr

from connect import *
from core import *


with open("config.json", 'r') as file:
    config = json.load(file)


class AndroidDevice(airtest.core.android.android.Android):
    def __init__(self, device_type):
        super().__init__()
        self.dev = connect_device(device_type)


logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

if __name__ == "__main__":
    reader = easyocr.Reader(['ch_sim'], gpu=True, download_enabled=False)
    device_box = ['安卓', 'UU模拟器', '蓝叠模拟器']
    device_type = device_box[0]
    current_device = AndroidDevice(device_type)
    auto_recruit(current_device.dev, reader)
