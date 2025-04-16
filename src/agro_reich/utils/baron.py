import os
import json
import requests
import threading

from agro_reich.utils.logger import get_logger

BARON_TOKEN = os.getenv("BARON_TOKEN")
BARON_URL = os.getenv("BARON_URL")


def get_job():

    logger = get_logger(threading.current_thread().name)

    data = {
        "token": BARON_TOKEN
    }

    response = requests.post(
        f"{BARON_URL}/get_job",
        data=json.dumps(data)
        ).json()

    try:
        if response['status'] == "OK" and response['job']:
            logger.info(f"Received a new job {response['job']}")
            return response['job']
        else:
            return None

    except Exception:
        return None


def hand_in_job(job_id, stats={}):

    logger = get_logger(threading.current_thread().name)

    data = {
        "token": BARON_TOKEN,
        "job_id": job_id,
        "stats": stats
    }

    response = requests.post(
        f"{BARON_URL}/hand_in_job",
        data=json.dumps(data)
        ).json()

    try:
        if response['status'] == "OK":
            logger.info(f"Successfully hand in job {job_id}")
            return True
        else:
            logger.error(f"Can't hand in job {response}")
            return False

    except Exception:
        return False


def get_config():

    logger = get_logger(threading.current_thread().name)

    data = {
        "token": BARON_TOKEN,
    }

    response = requests.post(
        f"{BARON_URL}/get_config",
        data=json.dumps(data)
        ).json()

    try:
        if response['status'] == "OK":
            logger.info("Got new config")
            return response
        else:
            logger.error(f"Can't getconfig {response}")
            return False

    except Exception:
        return False


config = get_config()
