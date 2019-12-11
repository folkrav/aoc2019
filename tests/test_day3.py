from typing import List

import pytest

from aoc.day3.part1 import Point, Wire, Panel
from aoc.day3.part2 import Panel as Part2Panel, Wire as Part2Wire
from aoc.util.data import get_input_data


@pytest.mark.parametrize(
    argnames=["point", "distance"],
    argvalues=[
        (Point(3, 3), 6),
        (Point(-3, 9), 12),
        (Point(10, -2), 12),
    ]
)
def test_part1_distance(point: Point, distance: int):
    assert point.manhattan_distance == distance


@pytest.mark.parametrize(
    argnames=["movements", "points"],
    argvalues=[
        (["D2", "R1", "U3"],
         [Point(0, -1), Point(0, -2), Point(1, -2), Point(1, -1), Point(1, 0), Point(1, 1)]),
        (["R3", "U1", "L2", "D2"],
         [Point(1, 0), Point(2, 0), Point(3, 0), Point(3, 1), Point(2, 1), Point(1, 1), Point(1, 0),
          Point(1, -1)]),
        (["R2", "L3"],
         [Point(1, 0), Point(2, 0), Point(1, 0), Point(0, 0), Point(-1, 0)])
    ]
)
def test_part1_wire(movements: List[str], points: List[Point]):
    wire = Wire(movements)
    assert wire.points == points


@pytest.mark.parametrize(
    argnames=["wire1", "wire2", "distance"],
    argvalues=[
        (Wire(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']),
         Wire(['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']),
         159),
        (Wire(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']),
         Wire(['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']),
         135),
        (Wire(['R8', 'U5', 'L5', 'D3']),
         Wire(['U7', 'R6', 'D4', 'L4']),
         6),
    ]
)
def test_part1_closest_distance(wire1: Wire, wire2, distance: int):
    panel = Panel(wire1, wire2)
    assert panel.get_closest_crossing().manhattan_distance == distance


def test_part1_result():
    line1, line2 = get_input_data(3)
    wire1, wire2 = Wire(line1), Wire(line2)
    panel = Panel(wire1, wire2)
    assert panel.get_closest_crossing().manhattan_distance == 280


@pytest.mark.parametrize(
    argnames=["wire1", "wire2", "length"],
    argvalues=[
        (Part2Wire(['L5', 'U10', 'R10']), Part2Wire(['U1', 'L2', 'D10', 'U20']), 6),
        (Part2Wire(['U10', 'L20', 'U10']), Part2Wire(['L2', 'U20']), 24),
        (Part2Wire(['D3', 'L12', 'U5']), Part2Wire(['L2', 'D10', 'L3', 'U20']), 10)
    ]
)
def test_part2_combined_length(wire1, wire2, length):
    panel = Part2Panel(wire1, wire2)
    assert panel.get_shortest_crossing_path() == length


def test_part2_result():
    line1, line2 = get_input_data(3)
    wire1, wire2 = Part2Wire(line1), Part2Wire(line2)
    panel = Part2Panel(wire1, wire2)
    assert panel.get_shortest_crossing_path() == 10554
