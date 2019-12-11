import pytest

from aoc.day1.part1 import Module as Part1Module, get_total_mass
from aoc.day1.part2 import Module as Part2Module
from aoc.util.data import get_input_data


@pytest.mark.parametrize(
    argnames=["mass", "fuel"],
    argvalues=[
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583)
    ]
)
def test_part1_module(mass, fuel):
    module = Part1Module(mass)
    assert module.fuel == fuel


def test_part1_total():
    modules = [Part1Module(mass) for mass in get_input_data(1)]
    assert get_total_mass(modules) == 3271095


@pytest.mark.parametrize(
    argnames=["mass", "fuel"],
    argvalues=[
        (14, 2),
        (1969, 966),
        (100756, 50346)
    ]
)
def test_part2_module(mass, fuel):
    module = Part2Module(mass)
    assert module.fuel == fuel


def test_part2_total():
    modules = [Part2Module(mass) for mass in get_input_data(1)]
    assert get_total_mass(modules) == 4903759
