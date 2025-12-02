#! /usr/bin/python3.12
import csv
import re


class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.position = 50

    def count_zeros(self, direction: str, clicks: int) -> int:
        """Counts the number of times dial points at 0 after `clicks` in given direction."""

        pointed_at_zero = 0

        if direction == "L":
            new_position = (self.position - clicks) % 100
            pointed_at_zero += clicks // 100
            # New position > old position or new position == 0 implies crossing
            # 0 unless currently at 0, which would cause double-counting
            if self.position != 0 and (new_position > self.position or new_position == 0):
                pointed_at_zero += 1
        else:
            new_position = (self.position + clicks) % 100
            pointed_at_zero += clicks // 100
            pointed_at_zero += 1 if new_position < self.position else 0

        self.position = new_position
        return pointed_at_zero

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            pointed_at_zero_count = 0

            for row in csv_reader:
                pattern = r"(L|R)(\d+)"
                match = re.search(pattern, row[0])
                pointed_at_zero_count += self.count_zeros(
                    match.group(1), int(match.group(2))
                )

            print(pointed_at_zero_count)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
