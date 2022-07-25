from airtest.core.api import auto_setup
from airtest.core.api import init_device


def connect_device(device_type):
    all_device_type = {"蓝叠模拟器": "Android://127.0.0.1:5037/127.0.0.1:5555", "安卓": "Android:///"}
    device_address = all_device_type.get(device_type)
    auto_setup(__file__, devices=[device_address])
    device = init_device(platform="Android", cap_method="JAVACAP")
    return device


if __name__ == "__main__":
    dev = connect_device("蓝叠模拟器")
    print(dev)
