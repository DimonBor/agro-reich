import os
import PIL
import mss
import time
import pyautogui
import threading
from agro_reich.utils.logger import get_logger
from agro_reich.utils.driver import drive_path
from agro_reich.utils.cords import read_cords


def get_screen():
    logger = get_logger(threading.current_thread().name)

    logger.info("Capturing screen")

    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])

    image = PIL.Image.frombytes(
        'RGB',
        (screenshot.width, screenshot.height),
        screenshot.rgb
        ).convert("RGBA")

    vignette = PIL.Image.open(
        "samples/vignette/vignette.png"
        ).convert("RGBA")
    vignette = vignette.resize(image.size)

    result = PIL.Image.alpha_composite(image, vignette)
    result.save("samples/tmp/current_screen.png")


def locate_culture(culture):
    logger = get_logger(threading.current_thread().name)

    logger.info(f"Locating {culture}")

    get_screen()

    for sample in os.listdir(f'samples/{culture}'):
        try:
            logger.debug(f"Processing sample {sample}")
            culture_position = pyautogui.center(
                pyautogui.locate(
                    f'samples/{culture}/{sample}',
                    'samples/tmp/current_screen.png',
                    confidence=0.472,
                    grayscale=True
                    )
                )

            pyautogui.moveTo(culture_position)
            logger.info(f"Found {culture} on {culture_position}")

            return culture_position

        except Exception:
            continue

    logger.error(f"Culture {culture} not found")

    return None


def collect_culture(culture):

    start_cords = read_cords()
    collected = 0

    culture_location = locate_culture(culture)

    while culture_location:
        pyautogui.keyDown('shiftleft')
        pyautogui.moveTo(culture_location)
        pyautogui.doubleClick()
        pyautogui.keyUp('shiftleft')

        time.sleep(2)

        drive_path([start_cords])

        collected += 1

        culture_location = locate_culture(culture)

    return collected
