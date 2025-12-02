#! /usr/bin/python3.12
import csv
import re


class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.position = 50

    def move_dial(self, direction: str, clicks: int):
        """Moves the dial in the given direction by `clicks` positions."""

        if direction == "L":
            self.position -= clicks
        else:
            self.position += clicks

        self.position %= 100

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            pointed_at_zero_count = 0

            for row in csv_reader:
                pattern = r"(L|R)(\d+)"
                match = re.search(pattern, row[0])
                self.move_dial(match.group(1), int(match.group(2)))

                if self.position == 0:
                    pointed_at_zero_count += 1

            print(pointed_at_zero_count)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
