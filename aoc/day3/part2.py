from functools import reduce

from aoc.util.data import get_input_data
from aoc.day3.part1 import Panel as Part1Panel, Wire as Part1Wire, Point


class Wire(Part1Wire):
    def get_point_index(self, point: Point):
        return self.points.index(point)


class Panel(Part1Panel):
    def __init__(self, wire1: Wire, wire2: Wire):
        super().__init__(wire1, wire2)

    def get_combined_length(self, point: Point):
        return self.wire1.get_point_index(point) + self.wire2.get_point_index(point) + 2

    def get_shortest_crossing_path(self):
        return min(self.get_combined_length(x) for x in self.get_crossings())


if __name__ == "__main__":
    line1, line2 = get_input_data(3)
    wire1, wire2 = Wire(line1), Wire(line2)
    panel = Panel(wire1, wire2)
    print(panel.get_shortest_crossing_path())
