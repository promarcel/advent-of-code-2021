import re

from rich import print


def get_input():
    commands = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            reg = re.compile("""
                x=(-?[0-9]+)..(-?[0-9]+),
                y=(-?[0-9]+)..(-?[0-9]+),
                z=(-?[0-9]+)..(-?[0-9]+)
            """, re.X)
            match = reg.search(line)
            on = line.startswith("on")
            xrange = sorted((int(match.group(1)), int(match.group(2)) + 1))
            yrange = sorted((int(match.group(3)), int(match.group(4)) + 1))
            zrange = sorted((int(match.group(5)), int(match.group(6)) + 1))
            commands.append((on, xrange, yrange, zrange))
    return commands


class Binary:
    def __init__(self, on, xrange, yrange, zrange):
        self.on = on
        self.xrange = xrange
        self.yrange = yrange
        self.zrange = zrange
        self._left = None
        self._right = None

    def by(self, xrange, yrange, zrange):
        result = True
        result &= self.xrange[0] >= xrange[0]
        result &= self.xrange[1] <= xrange[1]
        result &= self.yrange[0] >= yrange[0]
        result &= self.yrange[1] <= yrange[1]
        result &= self.zrange[0] >= zrange[0]
        result &= self.zrange[1] <= zrange[1]
        return result

    def volume(self):
        return ((self.xrange[1] - self.xrange[0]) *
                (self.yrange[1] - self.yrange[0]) *
                (self.zrange[1] - self.zrange[0]))

    def split(self, axis, value):
        left_extent = [self.xrange, self.yrange, self.zrange]
        axis_default = left_extent[axis]
        left_extent[axis] = (axis_default[0], value)
        self._left = Binary(self.on, *left_extent)

        right_extent = [self.xrange, self.yrange, self.zrange]
        right_extent[axis] = (value, axis_default[1])
        self._right = Binary(self.on, *right_extent)

    def intersects(self, xrange, yrange, zrange):
        intersects = True
        intersects &= self.xrange[0] < xrange[1]
        intersects &= self.xrange[1] > xrange[0]
        intersects &= self.yrange[0] < yrange[1]
        intersects &= self.yrange[1] > yrange[0]
        intersects &= self.zrange[0] < zrange[1]
        intersects &= self.zrange[1] > zrange[0]
        return intersects

    def count(self):
        if self.children():
            return self._left.count() + self._right.count()
        return self.volume() * self.on

    def children(self):
        return self._left is not None and self._right is not None

    def apply(self, on, xrange, yrange, zrange):
        if not self.intersects(xrange, yrange, zrange):
            return
        elif self.by(xrange, yrange, zrange):
            self.on = on
            self._left = None
            self._right = None
            return
        elif self.children():
            pass
        elif self.xrange[0] < xrange[0]:
            self.split(0, xrange[0])
        elif self.xrange[1] > xrange[1]:
            self.split(0, xrange[1])
        elif self.yrange[0] < yrange[0]:
            self.split(1, yrange[0])
        elif self.yrange[1] > yrange[1]:
            self.split(1, yrange[1])
        elif self.zrange[0] < zrange[0]:
            self.split(2, zrange[0])
        elif self.zrange[1] > zrange[1]:
            self.split(2, zrange[1])

        self._left.apply(on, xrange, yrange, zrange)
        self._right.apply(on, xrange, yrange, zrange)


def part_1(commands):
    cubes = Binary(0, (-50, 51), (-50, 51), (-50, 51))
    for on, xrange, yrange, zrange in commands:
        cubes.apply(on, xrange, yrange, zrange)

    return cubes.count()


def part_2(commands):
    box_bounds = (-200000, 200000)
    cubes = Binary(0, box_bounds, box_bounds, box_bounds)
    for on, xrange, yrange, zrange in commands:
        cubes.apply(on, xrange, yrange, zrange)

    return cubes.count()


if __name__ == "__main__":
    input = get_input()

    part_1 = part_1(input)
    print(f"Puzzle Part 1: {part_1}")

    part_2 = part_2(input)
    print(f"Puzzle Part 2: {part_2}")
