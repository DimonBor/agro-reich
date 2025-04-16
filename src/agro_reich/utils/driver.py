import time
import keyboard
import threading
import pyautogui
from agro_reich.utils.logger import get_logger
from agro_reich.utils.cords import read_cords


def drive(to_drive):
    logger = get_logger(threading.current_thread().name)
    logger.debug(f"Driving {to_drive}")
    to_press = []

    for i in range(len(to_drive)):
        to_press.append([])
        match to_drive[i]:
            case "right":
                to_press[i].append("right")
                to_press[i].append("down")
            case "left":
                to_press[i].append("left")
                to_press[i].append("up")
            case "up":
                to_press[i].append("right")
                to_press[i].append("up")
            case "down":
                to_press[i].append("left")
                to_press[i].append("down")

    if len(to_press) == 2:
        for button in list(set(to_press[0]) & set(to_press[1])):
            keyboard.press(button)
    else:
        for button in to_press[0]:
            keyboard.press(button)

    time.sleep(0.07)
    keyboard.release("right")
    keyboard.release("left")
    keyboard.release("up")
    keyboard.release("down")


def drive_path(path):
    logger = get_logger(threading.current_thread().name)
    logger.info(f"Driving path {path}")
    for point in path:
        logger.info(f"Driving to {point}")
        X, Y = map(float, read_cords())
        while abs(point[0] - X) > 1 or abs(point[1] - Y) > 1:
            to_drive = []
            if abs(point[0] - X) > 1:
                if point[0] > X:
                    to_drive.append("right")
                elif point[0] < X:
                    to_drive.append("left")

            if abs(point[1] - Y) > 1:
                if point[1] > Y:
                    to_drive.append("up")
                elif point[1] < Y:
                    to_drive.append("down")
            drive(to_drive)
            X, Y = map(float, read_cords())

    logger.info(f"Finished path {path}")


def dismount():
    pyautogui.press("a")


def mount():
    pyautogui.press("a")
    time.sleep(3.5)


def park():
    start_cords = read_cords()
    start_cords[0] += 12
    drive_path([start_cords])
    dismount()
    start_cords[0] -= 12
    drive_path([start_cords])


def travel(island):
    pass
