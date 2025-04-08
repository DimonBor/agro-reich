import yaml
import threading
from utils.logger import get_logger
from utils.driver import drive_path, mount, dismount, park
from utils.path import find_path
from utils.cultures import collect_culture


class Scenario:

    def __init__(self, name):
        self.load_config(name)
        self.stats = {}

    def load_config(self, name):
        with open(f"scenarios/{name}.yaml", "r") as file:
            config = yaml.safe_load(file)
        self.name = config["name"]
        self.tasks = config["tasks"]

    def run(self):
        logger = get_logger(threading.current_thread().name)

        logger.info(f"Starting scenario {self.name}")

        for task in self.tasks:
            match task["task"]:
                case "drive":
                    logger.info(f"Driving from {task['from']} to {task['to']}")
                    drive_path(find_path(task["from"], task["to"]))
                case "park":
                    logger.info("Parking")
                    park()
                case "mount":
                    logger.info("Mounting")
                    mount()
                case "dismount":
                    logger.info("Dismounting")
                    dismount()
                case "collect":
                    logger.info(f"Collecting culture {task["culture"]}")
                    try:
                        self.stats["collected"] += collect_culture(
                            task["culture"])
                    except KeyError:
                        self.stats["collected"] = collect_culture(
                            task["culture"])

        logger.info(f"Finished scenario {self.name}")
        return self.stats
