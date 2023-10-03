import pyautogui as pg
from PIL import ImageGrab

def find_rgb_on_screen(rgb_color):
    # 화면 캡처
    screen = ImageGrab.grab()

    # 화면 크기 구하기
    screen_width, screen_height = screen.size

    # 화면을 왼쪽위에서 아래로 스캔하면서 RGB 값을 찾음
    for y in range(screen_height):
        for x in range(screen_width):
            pixel_color = screen.getpixel((x, y))
            if pixel_color == rgb_color:
                return x, y

    return None 

def find_rgb_on_screen_right(rgb_color):
    # 화면 캡처
    screen = ImageGrab.grab()

    # 화면 크기 구하기
    screen_width, screen_height = screen.size

    # 화면을 오른쪽위에서 아래로 스캔하면서 RGB 값을 찾음
    for y in range(screen_height):
        for x in range(screen_width):
            pixel_color = screen.getpixel((screen_width-x, y))
            if pixel_color == rgb_color:
                return x, y

    return None  # 원하는 색상을 찾지 못한 경우 None 반환

# 원하는 RGB 색상 값 설정 (예: 빨간색)

DarkBurgundy = (255, 68, 15)
Burgundy = (249, 24, 247)


if __name__ == '__main__':
    # 화면에서 RGB 값을 찾음
    result = find_rgb_on_screen(Burgundy)

    if result:
        print(f"찾은 좌표: {result}")
        pg.moveTo(result)
    else:
        print("원하는 RGB 값을 찾을 수 없습니다.")
