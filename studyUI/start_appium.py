# -*- coding:utf-8 -*-
# Author: chenjianmin
# TIME: 2022/8/26 15:00

# import os
# import time
# from multiprocessing.dummy import Pool
# from base.common import get_devices
from base.common import *


num = len(get_devices())  # 获取设备数量。
if num:
    print(f"共有{num}个设备。")
    ls = [4725 + i * 5 for i in range(num)]  # 端口号
else:
    print("还没有连接任何设备，请先检查一下。")
    exit(100)


def start_appium(port):
    os.system(f"appium -p {port}")
    time.sleep(1)


p = Pool(num)
p.map(start_appium, ls)  # 开完就阻塞了，不会往下走。不过这边的任务也只是开启.后面就不需要管了.
