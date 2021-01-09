import win32api, win32con, win32gui
from win32gui import EnumWindows, IsWindow, IsWindowEnabled, IsWindowVisible, GetWindowText
from PIL import Image, ImageGrab
import numpy as np

def get_window_pos(hwnd, hwnd_list):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        #
        hwnd_list.append(hwnd)
        # return win32gui.GetWindowRect(hwnd), hwnd


def fetch_image(keyword):
    hwnd_list = []
    (x1, y1, x2, y2), handle = (0, 0, 0, 0), 0
    EnumWindows(get_window_pos, hwnd_list)  # 传引用获取所有窗口
    for hwnd in hwnd_list:
        if keyword in win32gui.GetWindowText(hwnd):
            (x1, y1, x2, y2), handle = win32gui.GetWindowRect(hwnd), hwnd
            break
    # 发送还原最小化窗口的信息
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # 设为高亮
    # win32api.keybd_event(0x41, 0, 0, 0)  #
    win32gui.SetForegroundWindow(handle)
    # 截图
    grab_image = ImageGrab.grab((x1, y1, x2, y2))
    return grab_image

if __name__ == "__main__":
    keyword = 'BlueStacks'
    img = fetch_image(keyword)
    img.save(r'.\screen_shot1.png')
    # img1 = np.array(img)  # 转出来值不对需要调试
    # import cv2
    # cv2.imwrite(r'.\screen_shot2.png', img1)

