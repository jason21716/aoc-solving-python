import re
import statistics
import timeit
import argparse


def main(module_name: str):
    running_module = __import__(
        "puzzles.{0}".format(module_name), globals(), locals(), ["main_1", "main_2"], 0
    )
    main_1_reulst = running_module.main_1()
    main_2_reulst = running_module.main_2()

    print("Part 1 result:", main_1_reulst)
    print("Part 2 result:", main_2_reulst)


def performance(module_name: str, repeats: int):
    performance_time = timeit.repeat(
        "running_module.performance()",
        setup=f"running_module = __import__('puzzles.{module_name}', globals(), locals(), ['performance'], 0)",
        repeat=repeats,
        number=1,
    )

    performance_time_quantiles = statistics.quantiles(performance_time)

    print(
        f"Running script in {repeats} times, running time statics is at below: (seconds)"
    )
    print(f"min\t{min(performance_time)}")
    print(f"perc25\t{performance_time_quantiles[0]}")
    print(f"avg\t{statistics.mean(performance_time)}")
    print(f"median\t{performance_time_quantiles[1]}")
    print(f"perc75\t{performance_time_quantiles[2]}")
    print(f"max\t{max(performance_time)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("module_name", help="Module name will running")
    parser.add_argument(
        "-p", "--performance", help="Running performance mode", action="store_true"
    )
    parser.add_argument(
        "-r",
        "--repeat",
        help="repeat times in performance mode",
        type=int,
        default=1000,
    )
    args = parser.parse_args()

    selected_module_name: str = args.module_name

    if args.performance:
        performance(selected_module_name, repeats=args.repeat)
    else:
        main(selected_module_name)
