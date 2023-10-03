import pyautogui as pg
import keyboard as kb
from utils import *
from pixelsearch import *
import threading
import winsound as sd
import random

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 1000     # 1000 ms ==1second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)


img_reserve = 'assets/reserve.png'
img_exit = 'assets/exit.png'
img_plan1 = 'assets/plan1.png'
img_plan2 = 'assets/plan2.png'
img_plan1_fail = 'assets/plan1_fail.png'
img_plan2_fail = 'assets/plan2_fail.png'
img_select = 'assets/select.png'
img_org_select = 'assets/org_select.png'
img_red_select = 'assets/red_select.png'

def step1():
    waiting_image(img_exit)
    click_img(img_exit)

def step2():
    # 로딩 대기
    waiting_image(img_plan1)
    
    if pg.locateOnScreen(img_plan1_fail, confidence=0.8):
        print('버건디석 매진')
    else:
        print('버건디석 좌석 존재')
        click_img(img_plan1)
        click_img(img_select)
        return 1
        
    # 다크 버건디 체크
    if pg.locateOnScreen(img_plan2_fail, confidence=0.8):
        raise Exception('다크 버건디석 매진')
    else:
        print('다크 버건디석 좌석 존재')
        click_img(img_plan2)
        click_img(img_select)
        return 2

def step3(num):
    if num == 1:
        result = find_rgb_on_screen(Burgundy)
        while result is None:
            if result:
                # 버건디석이 있으면 좌표로 이동
                print(f"찾은 좌표: {result}")
                pg.click(result)
                break
            result = find_rgb_on_screen(Burgundy)

    elif num == 2:
        result = find_rgb_on_screen_right(DarkBurgundy)
        while result is None:
            if result:
                # 다크 버건디석이 있으면 좌표로 이동
                print(f"찾은 좌표: {result}")
                pg.click(result)
                break
            result = find_rgb_on_screen_right(DarkBurgundy)
            
    else:
        raise Exception('좌석이 없습니다.')

    click_img(img_org_select)
    click_img(img_red_select)
    # 알림소리 울리기
    beepsound()

def end_hotkey():
    global end_enabled
    while True:
        kb.wait('f4')
        print('f4 감지 루틴 종료')
        end_enabled = True
        break        


def end_method():
    global end_enabled
    if end_enabled:
        raise KeyboardInterrupt


if __name__ == '__main__':
    end_enabled = False
    kb.wait('f4')
    print('f4 감지 루틴 시작')
    time.sleep(0.5)
    # end_hotkey()를 스레드로 시작
    t = threading.Thread(target=end_hotkey)
    t.start()
    
    while True:
        try:
            pg.press('f5') # 새로고침
            pg.press('enter')
            step1()
            end_method()
            num = step2()
            end_method()
            step3(num)
            end_method()
        except Exception as e:
            print(e)
            # print('다시 시작하려면 f4를 누르세요')
            print('5초 후 다시 시작합니다.')
            end_method()
            time.sleep(random.uniform(5,6))
            end_method()
            continue
        except KeyboardInterrupt:
            print('프로그램 종료')
            break
    
