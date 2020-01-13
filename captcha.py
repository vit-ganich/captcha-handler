import pyautogui
import time
import glob

scroll_templates = './templates/scroll/*.png'
hole_templates = './templates/hole/*.png'


def get_coordinates(path_to_templates: str) -> pyautogui.Point:
    """Go through the files in templates folder and check
    if the template file matches with the screen
    """
    for file in glob.glob(path_to_templates):
        # returns coordinates in case of success. otherwise returns None
        target = pyautogui.locateCenterOnScreen(file)
        if target:
            return target


def handle_captcha():
    #time.sleep(3)  # need some time to open browser
    # get scroll Point() object with coordinates X.Y
    scroll = get_coordinates(scroll_templates)

    # get hole Point() object with coordinates X.Y
    hole = get_coordinates(hole_templates)

    # get distance to drag and drop
    relative_path = hole.x - scroll.x

    # mouse Down on scroll center
    pyautogui.mouseDown(scroll, button='left')

    # drag scroll to hole Y coordinate
    pyautogui.dragRel(relative_path, button='left', duration=2)
    time.sleep(1)
    # mouse Up
    pyautogui.mouseUp(button='left')


handle_captcha()
target = pyautogui.locateCenterOnScreen('./templates/retry.png')
if target:
    pyautogui.click(target)
    time.sleep(2)
    handle_captcha()
