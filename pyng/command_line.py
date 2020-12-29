import argparse
from pyng import Pyng


def main():
    parser = argparse.ArgumentParser(description="Pings multiple hosts at the same time")
    parser.add_argument("host", type=str, nargs="+")
    parser.add_argument("--delay", type=float, default=1)
    parser.add_argument("--logfile", type=str)
    args = parser.parse_args()
    pyng = Pyng(args.logfile, args.host, args.delay)
    pyng.run()
