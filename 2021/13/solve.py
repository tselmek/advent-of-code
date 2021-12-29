import re

DOT_REGEX = "^(\d+),(\d+)$"
FOLD_REGEX = "^fold along ([xy])=(\d+)$"

lines = [line.rstrip("\n") for line in open("input.txt")]


class Dot:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"Dot({self.x},{self.y})"

    def transpose_at(self, fold_x: int = None, fold_y: int = None) -> None:
        if fold_x:
            if self.x > fold_x:
                self.x -= 2 * (self.x - fold_x)
        if fold_y:
            if self.y > fold_y:
                self.y -= 2 * (self.y - fold_y)
        if fold_x == self.x or fold_y == self.y:
            print("blorp")


class Paper:
    def __init__(self) -> None:
        self.dots = []

    def instanciate_dot(self, x: int, y: int) -> None:
        self.dots.append(Dot(x, y))

    def fold_along(self, x: int = None, y: int = None) -> None:
        for dot in self.dots:
            dot.transpose_at(x, y)
        self.treeshake_copies()

    def treeshake_copies(self) -> None:
        k = 0
        while k < len(self.dots):
            if self.dots[k] in self.dots[:k]:
                self.dots.pop(k)
            else:
                k += 1

    def print_code(self) -> None:
        height = max(dot.y for dot in self.dots) + 1
        width = max(dot.x for dot in self.dots) + 1
        code = [[" " for x in range(width)] for y in range(height)]
        for dot in self.dots:
            code[dot.y][dot.x] = "█"
        for line in code:
            print("".join(line))


paper = Paper()
fold = 0

for line in lines:
    if len(line) > 0:
        is_dot = re.match(DOT_REGEX, line)
        if is_dot:
            x, y = is_dot.groups()
            paper.instanciate_dot(int(x), int(y))

        is_fold = re.match(FOLD_REGEX, line)
        if is_fold:
            # print(sorted(paper.dots, key=lambda dot: (dot.x, dot.y)))
            axis, value = is_fold.groups()
            if axis == "x":
                paper.fold_along(x=int(value))
            if axis == "y":
                paper.fold_along(y=int(value))
            fold += 1

            if fold == 1:
                print(len(paper.dots))

paper.print_code()
