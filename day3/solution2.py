#! /usr/bin/python3.12
import csv


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def get_largest_joltage(self, digits: int, bank: str) -> int:
        """Returns the largest joltage that can be formed from bank.

        Joltage should have `digits` size.
        """
        output = [0 for _ in range(digits)]

        for idx, ch in enumerate(bank):
            battery = int(ch)

            positions_from_end = len(bank) - idx
            start_idx = max(0, digits - positions_from_end)

            # Replace first (highest order) smaller digit that is found, while
            # leaving room for remaining batteries in bank
            for output_idx in range(start_idx, digits):
                if battery > output[output_idx]:
                    output[output_idx] = battery

                    # Set next digit to 0, since we can make a larger joltage
                    # after replacing the digit at output_idx
                    if output_idx < digits - 1:
                        output[output_idx + 1] = 0
                    break

        return int("".join(map(str, output)))

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            joltage_sum = 0

            for row in csv_reader:
                joltage_sum += self.get_largest_joltage(12, row[0])

            print(joltage_sum)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
