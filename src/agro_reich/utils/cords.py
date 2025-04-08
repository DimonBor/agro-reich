import struct
import threading
import subprocess
from utils.logger import get_logger


def update_cords():
    logger = get_logger(threading.current_thread().name)

    cmd = "tshark -i enp4s0 -l -T fields -e udp.payload port 5056 and udp and ip[2:2] == 109".split()

    while True:
        x_old = 0
        y_old = 0
        popen = subprocess.Popen(
            cmd, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            universal_newlines=True
            )
        for packet_from_pipe in iter(popen.stdout.readline, ""):
            packet = bytes.fromhex(packet_from_pipe)
            x_offset = 44
            y_offset = 48

            x_new_chunk = packet[x_offset:x_offset+4]
            y_new_chunk = packet[y_offset:y_offset+4]

            try:
                x_new = struct.unpack('!f', x_new_chunk)[0]
                y_new = struct.unpack('!f', y_new_chunk)[0]

                logger.debug(f"New cords: {x_new:.3f} {y_new:.3f}")
                logger.debug(
                    f"Cord diff: {(x_old - x_new):.3f} {(y_old - y_new):.3f}"
                    )

                write_cords(x_new, y_new)

                x_old = x_new
                y_old = y_new

            except Exception:
                pass

        popen.stdout.close()

        logger.error("Cord update failed, restarting...")


def write_cords(x, y):
    f = open("cords", "w")
    f.write(f"{x} {y}")
    f.close()


def read_cords():
    try:
        f = open("cords", "r")
    except FileNotFoundError:
        write_cords(0, 0)
        f = open("cords", "r")

    cords = []

    while len(cords) == 0:
        cords = list(map(float, f.read().split()))

    return cords
