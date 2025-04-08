import sys
import threading
from utils.cords import update_cords
from utils.cultures import locate_culture
from utils.scenarios import Scenario
from utils.logger import get_logger

cmd = sys.argv

locate_culture("firetouched_mullein")


if __name__ == "__main__":
    logger = get_logger(threading.current_thread().name)

    cords_updater = threading.Thread(name="CordsUpdater", target=update_cords)
    cords_updater.start()

    #test_sceanrio = Scenario("collect_single_test")
    #test_sceanrio = Scenario("drive_test")
    test_sceanrio = Scenario("collect_firetouched_mullein")
    
    test_results = test_sceanrio.run()

    logger.info(f"TScenario stats: {test_results}")

    '''
    driver = threading.Thread(
        name="Driver",
        target=drive_path,
        args=(find_path('bed_2', 'bed_3'),))
    driver.start()
'''