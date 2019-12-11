"""
The gravity assist was successful, and you're well on your way to the Venus refuelling station.
During the rush back on Earth, the fuel management system wasn't completely installed, so that's
next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a
central port and extend outward on a grid. You trace the path each wire takes as it leaves the
central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need
to find the intersection point closest to the central port. Because the wires are on a grid, use the
Manhattan distance for this measurement. While the wires do technically cross right at the central
port where they both start, this point does not count, nor does a wire count as crossing with
itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it
goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port:
its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

What is the Manhattan distance from the central port to the closest intersection?
"""
from __future__ import annotations

from operator import attrgetter
from dataclasses import dataclass
from typing import List

from aoc.util.data import get_input_data


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


class Wire:
    def __init__(self, movements: List[str]):
        self.points = []

        pointer = {"x": 0, "y": 0}
        for movement in movements:
            direction, count = movement[0], int(movement[1:])
            axis = "x" if direction in ["L", "R"] else "y"
            mod = -1 if direction in ["L", "D"] else 1
            for x in range(count):
                pointer[axis] += mod
                self.points.append(Point(**pointer))


class Panel:
    def __init__(self, wire1: Wire, wire2):
        self.wire1 = wire1
        self.wire2 = wire2

    def get_crossings(self) -> List[Point]:
        return list(set(self.wire1.points).intersection(self.wire2.points))

    def get_closest_crossing(self) -> Point:
        return min(self.get_crossings(), key=attrgetter("manhattan_distance"))


if __name__ == "__main__":
    line1, line2 = get_input_data(3)
    panel = Panel(Wire(line1), Wire(line2))
    print(panel.get_closest_crossing())
