#!/usr/bin/env python3

import argparse
import sys
import timeit
import statistics

from sudoku import Board, find_one_solution


def parse_arguments(argv):
    parser = argparse.ArgumentParser(description='Benchmark your Sudoku solver.')
    parser.add_argument('benchmark', help="Path to the benchmark file with all benchmark instances.")
    parser.add_argument('-n', default=10, type=int, help="Max. number of boards from the benchmark file to test.")
    return parser.parse_args(argv)


def read_benchmark_file(file):
    with open(file, 'r') as f:
        for line in f:
            yield line.rstrip('\n')


def main(argv):
    args = parse_arguments(argv)
    times = []
    for i, board in enumerate(read_benchmark_file(args.benchmark), start=1):
        times.append(timeit.timeit(lambda: find_one_solution(Board(board), verbose=False), number=1))
        if i == args.n:
            break
    print(f"Runs: {args.n}, Total time (sec): {sum(times):.3f}, Max: {max(times):.3f},"
          f" Min: {min(times):.3f}, Avg: {statistics.mean(times):.3f}, stdev: {statistics.stdev(times):.3f}")


if __name__ == "__main__":
    main(sys.argv[1:])
