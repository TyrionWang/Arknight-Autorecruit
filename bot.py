import airtest.core.android.android

from connect import *
from core import *


class AndroidDevice(airtest.core.android.android.Android):
    def __init__(self, device_type):
        super().__init__()
        self.dev = connect_device(device_type)


def device_select(device_type):
    if device_type == 'ios':
        pass
    else:
        global current_device
        current_device = AndroidDevice(device_type)


def recruit():
    global current_device
    auto_recruit(current_device.dev)


if __name__ == "__main__":
    global current_device
    cbox = ['安卓', 'ios', 'UU模拟器', '蓝叠模拟器']
    device_select(cbox[0])
    recruit()
