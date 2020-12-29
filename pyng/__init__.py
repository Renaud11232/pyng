import logging
import sys
import threading
import time
from ping3 import ping


class Pyng:

    def __init__(self, logfile, hosts, delay):
        self.__logger = logging.getLogger("pyng")
        self.__logger.setLevel(logging.INFO)
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if logfile:
            file_handler = logging.FileHandler(logfile)
            file_handler.setFormatter(log_format)
            self.__logger.addHandler(file_handler)
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(log_format)
        self.__logger.addHandler(stdout_handler)
        self.__hosts = hosts
        self.__delay = delay
        self.__log_lock = threading.Lock()

    def run(self):
        try:
            while True:
                for host in self.__hosts:
                    thread = threading.Thread(target=self.__send_ping, args=(host,))
                    thread.setDaemon(True)
                    thread.start()
                time.sleep(self.__delay)
        except KeyboardInterrupt:
            self.__logger.info("Exiting...")

    def __send_ping(self, host):
        result = ping(host, unit="ms")
        self.__log_lock.acquire()
        if result is None:
            self.__logger.warning("%s : timed out" % host)
        elif result is False:
            self.__logger.warning("%s = cannot resolve host" % host)
        else:
            self.__logger.info("%s : answered in %0.3f ms" % (host, result))
        self.__log_lock.release()
