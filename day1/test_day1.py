import unittest
from pathlib import Path

import lib

with open(
    Path(__file__).parent.joinpath("data/test_input.txt"), "r", encoding="utf-8"
) as f:
    test_input_lines = f.read().split("\n")


class Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(11, lib.part1(test_input_lines))

    def test_part2(self):
        self.assertEqual(31, lib.part2(test_input_lines))


tc = unittest.TestCase()
