import time

import pydirectinput
import numpy as np
import win32api
import win32con

# 初始化pydirectinput
pydirectinput.PAUSE = 0.0001

# 创建一个变量来跟踪侧键状态
side_button_pressed = False


#
# 按压时间: 0.104
# 秒
# 间隔时间: 0.056
# 秒
# 按压时间: 0.106
# 秒
# 间隔时间: 0.068
# 秒
# 按压时间: 0.088
# 秒

def human_like_press_duration():
    mu, sigma = 0.060, 0.015  # 平均值135ms，标准差15ms
    duration = np.random.normal(mu, sigma)
    return max(0.0450, min(duration, 0.075))  # 限制在120ms到150ms之间

def human_like_click_gap():
    mu, sigma = 0.002, 0.00065  # 平均值21.5ms，标准差6.5ms
    interval = np.random.normal(mu, sigma)
    return max(0.001, min(interval, 0.0030))  # 限制间隔在15ms到28ms之间


def human_like_move():
    mu, sigma = 0.5, 0.3
    move =  np.random.normal(mu, sigma)
    return max(1, min(int(move), 2))

def on_event():
    global side_button_pressed
    while True:
        # 检查鼠标侧键状态（这里使用X2按钮，通常是"前进"键）
        # if win32api.GetAsyncKeyState(win32con.VK_XBUTTON2) & 0x8000:
        if win32api.GetAsyncKeyState(win32con.VK_SHIFT) & 0x8000:
            if not side_button_pressed:
                side_button_pressed = True
                print('侧键被按下')



            pydirectinput.mouseDown(button='left')
            # time.sleep(random.uniform(0.120, 0.150))  # 随机等待120到150毫秒
            press_time = human_like_press_duration()
            # press_time =0.06
            print("按压时间: %f" % press_time)
            time.sleep(press_time)
            pydirectinput.mouseUp(button='left')

            click_gap = human_like_click_gap()
            # click_gap = 0.008
            print("间隔时间: %f" % click_gap)

            # time.sleep(click_gap)



            # 压枪效果：向下移动鼠标

            # move_distance = human_like_move()
            # pydirectinput.moveRel(0, move_distance)


        else:
            if side_button_pressed:
                side_button_pressed = False
                pydirectinput.mouseUp(button='left')
                print('侧键被释放')

        time.sleep(0.01)

if __name__ == "__main__":
    try:
        print("压枪脚本已启动，按Ctrl+C停止")
        pydirectinput.FAILSAFE = False  # 禁用故障安全功能
        on_event()
    except KeyboardInterrupt:
        print("程序已停止")
    finally:
        pydirectinput.mouseUp(button='left')  # 确保在程序结束时释放鼠标按键
