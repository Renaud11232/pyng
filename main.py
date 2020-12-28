from ping3 import ping
import argparse
import threading
import time
import logging
import sys


def send_ping(host, delay, logger):
    while True:
        result = ping(host, unit="ms")
        if result is None:
            logger.warning("%s : timed out" % host)
        elif result is False:
            logger.warning("%s = cannot resolve host" % host)
        else:
            logger.info("%s : answered in %0.3f ms" % (host, result))
        time.sleep(delay)


def main():
    parser = argparse.ArgumentParser(description="Pings multiple hosts at the same time")
    parser.add_argument("host", type=str, nargs="+")
    parser.add_argument("--delay", type=float, default=1)
    parser.add_argument("--logfile", type=str)
    args = parser.parse_args()
    logger = logging.getLogger("pyng")
    logger.setLevel(logging.INFO)
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if args.logfile:
        file_handler = logging.FileHandler(args.logfile)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(log_format)
    logger.addHandler(stdout_handler)
    for host in args.host:
        thread = threading.Thread(target=send_ping, args=(host, args.delay, logger))
        thread.setDaemon(True)
        thread.start()
    try:
        while True:
            time.sleep(10)
    except:
        logger.info("Exiting...")


if __name__ == "__main__":
    main()
