from argparse import ArgumentParser
from typing import Mapping, Any

from pyrates.pyrates import PyRates
from pyrates.pyrates_gui import PyRatesGUI


def main():
    parser = ArgumentParser(description="Convert rates between currencies")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-g", 
        "--gui", 
        action="store_true",
        help="starts pyrates gui"
    )
    group.add_argument(
        "-r", 
        "--all-rates", 
        action="store_true",
        help="get all rates"
    )
    group.add_argument(
        "-c", 
        "--conversion", 
        action="store_true",
        help="conversion flag"
    )
    parser.add_argument(
        "-a", 
        type=float, 
        help="amount to convert", 
        default=1.0
    )
    parser.add_argument(
        "-f",
        type=str, 
        help="convert from currency-code", 
        default="eur"
    )
    parser.add_argument(
        "-t",
        type=str, 
        help="convert to currency-code", 
        default="usd"
    )
    vargs: Mapping[str, Any] = vars(parser.parse_args())

    if vargs["gui"]:
        PyRatesGUI.Run()
    elif vargs["all_rates"]:
        print(PyRates())
    else:
        conversion: float = PyRates().Convert(fromRate=vargs["f"], toRate=vargs["t"], amount=vargs["a"])
        if conversion > 0:
            print(f'{vargs["a"]} {vargs["f"].upper()} -> {conversion} {vargs["t"].upper()}')
