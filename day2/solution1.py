#! /usr/bin/python3.12
import csv
import re


class Solution(object):
    def __init__(self, filename):
        self.filename = filename

    def sum_invalid_ids(self, lo: str, hi: str) -> int:
        """Sum all invalid IDs between lo and hi as ints."""
        invalid_id_sum = 0

        curr_base = lo[: (len(lo) // 2)] if int(lo) >= 10 else "1"
        curr_invalid_id = int(curr_base + curr_base)

        lo_int = int(lo)
        hi_int = int(hi)

        while curr_invalid_id <= hi_int:
            if lo_int <= curr_invalid_id <= hi_int:
                invalid_id_sum += curr_invalid_id

            curr_base = str(int(curr_base) + 1)
            curr_invalid_id = int(curr_base + curr_base)

        return invalid_id_sum

    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            range_pattern = r"(\d+)-(\d+)"
            total_invalid_id_sum = 0

            for row in csv_reader:
                for group in row:
                    match = re.search(range_pattern, group)
                    total_invalid_id_sum += self.sum_invalid_ids(
                        match.group(1), match.group(2)
                    )

            print(total_invalid_id_sum)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
