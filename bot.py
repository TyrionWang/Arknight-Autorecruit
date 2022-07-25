import airtest.core.android.android

from connect import *
from core import *


class AndroidDevice(airtest.core.android.android.Android):
    def __init__(self, device_type):
        super().__init__()
        self.dev = connect_device(device_type)


if __name__ == "__main__":
    global current_device
    cbox = ['安卓', 'UU模拟器', '蓝叠模拟器']
    device_type = cbox[0]
    current_device = AndroidDevice(device_type)
    auto_recruit(current_device.dev)
