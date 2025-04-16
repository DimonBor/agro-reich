import sys
import time
import threading
from agro_reich.utils.cords import update_cords
from agro_reich.utils.scenarios import Scenario
from agro_reich.utils.logger import get_logger
from agro_reich.utils.baron import get_job, hand_in_job, config

cmd = sys.argv

if __name__ == "__main__":
    logger = get_logger(threading.current_thread().name)

    cords_updater = threading.Thread(name="CordsUpdater", target=update_cords)
    cords_updater.start()

    while True:
        job = get_job()

        if not job or not config:
            time.sleep(300)

        match job['job_type']:
            case 1:  # seeding
                main_scenario = Scenario("seed_firetouched_mullein")
            case 2:  # harvesting
                main_scenario = Scenario("collect_firetouched_mullein")

        main_scenario.tasks.insert(0, {
            "travel": {"to": job['island']}
            })

        result = main_scenario.run()

        hand_in_job(job['job_id'], stats=result)
