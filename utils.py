import pyautogui as pg
import time

def waiting_image_region(left, top, width, height, img_path, wait_until=10):
    im = pg.screenshot(region=(left, top, width, height))
    cord = pg.locate(needleImage=img_path, haystackImage=im, confidence=0.8)
    while cord is None :
        print(f'waiting for {img_path}', end='\r')
        time.sleep(0.1)
        im = pg.screenshot(region=(left, top, width, height))
        cord = pg.locate(needleImage=img_path, haystackImage=im, confidence=0.8)
    print(f'image found: {cord}')


def click_img(img_path):
    # 경로의 이미지 클릭
    result = pg.locateCenterOnScreen(img_path, confidence=0.8)
    if result:
        pg.click(result)

def waiting_image(img_path):
    cord = pg.locateCenterOnScreen(img_path, confidence=0.9)
    while cord is None :
        print(f'waiting for {img_path}', end='\r')
        time.sleep(0.1)
        cord = pg.locateCenterOnScreen(img_path, confidence=0.8)
    print()

