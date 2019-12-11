"""
Tools related to AoC daily input data
"""
from typing import Any

from aocd.models import Puzzle

__TRANSFORM = {
    1: lambda x: [int(x) for x in x.splitlines()],
    3: lambda x: (line.split(",") for line in x.splitlines())
}


def get_input_data(day: int) -> Any:
    """
    Get input data for a given day
    @param day: day of the month
    @return: raw input data
    """
    puzzle = Puzzle(year=2019, day=day)
    data = puzzle.input_data

    if day in __TRANSFORM:
        return __TRANSFORM[day](data)

    return data
