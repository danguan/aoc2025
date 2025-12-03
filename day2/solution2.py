#! /usr/bin/python3.12
import csv
import re
from typing import List
from bisect import bisect_left


class Solution(object):
    def __init__(self, filename):
        self.filename = filename
        self.groups = []
        self.max_id = -1
        self.invalid_ids = set()

    def sum_invalid_ids(self, lo: int, hi: int, sorted_invalid_ids: List[int]) -> int:
        """Sum all `invalid_ids` between lo and hi as ints."""
        invalid_id_sum = 0

        idx = bisect_left(sorted_invalid_ids, lo)

        while idx < len(sorted_invalid_ids):
            curr_invalid_id = sorted_invalid_ids[idx]

            if curr_invalid_id > hi:
                break
            
            invalid_id_sum += curr_invalid_id
            idx += 1
        
        return invalid_id_sum

    def populate_invalid_ids(self):
        """Populate all invalid IDs from 1 to `self.max_id`."""
        curr_base = "1"

        while int(curr_base + curr_base) <= self.max_id:
            # If curr_base is in self.invalid_ids, we have processed a shorter
            # version of it already, and reprocessing will double count.
            if int(curr_base) not in self.invalid_ids:
                curr_invalid_id = int(curr_base + curr_base)

                while curr_invalid_id <= self.max_id:
                    self.invalid_ids.add(curr_invalid_id)
                    curr_invalid_id = int(str(curr_invalid_id) + curr_base)

            curr_base = str(int(curr_base) + 1)


    def solve(self):
        with open(self.filename) as f:
            csv_reader = csv.reader(f)
            range_pattern = r"(\d+)-(\d+)"
            total_invalid_id_sum = 0

            for row in csv_reader:
                for group in row:
                    match = re.search(range_pattern, group)
                    self.groups.append((int(match.group(1)), int(match.group(2))))

            for _, hi in self.groups:
                self.max_id = max(self.max_id, hi)
            
            self.populate_invalid_ids()
            
            sorted_invalid_ids = list(self.invalid_ids)
            sorted_invalid_ids.sort()

            for lo, hi in self.groups:
                total_invalid_id_sum += self.sum_invalid_ids(lo, hi, sorted_invalid_ids)

            print(total_invalid_id_sum)


if __name__ == "__main__":
    sol = Solution("input.csv")
    sol.solve()
