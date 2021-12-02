from typing import List


Direction = str
Distance = int
Instruction = tuple[Direction, Distance]


class Submarine():
    def __init__(self):
        self.depth = 0
        self.horizontal_position = 0
        self.aim = 0

    def use_path(self, path: List[Instruction]) -> None:
        for instruction in path:
            match instruction:
                case("forward", x):
                    self.horizontal_position += x
                case("up", d):
                    self.depth -= d
                case("down", d):
                    self.depth += d

    def use_corrected_path(self, path: List[Instruction]) -> None:
        for instruction in path:
            match instruction:
                case("forward", x):
                    self.depth += self.aim * x
                    self.horizontal_position += x
                case("up", d):
                    self.aim -= d
                case("down", d):
                    self.aim += d

    def final_position(self) -> int:
        return self.depth * self.horizontal_position


def extract_instruction(raw_instruction: str) -> Instruction:
    direction, raw_distance = raw_instruction.rstrip("\n").split(" ")
    return (direction, int(raw_distance))


lines = [
    extract_instruction(line) for line in open("input.txt")
]

submarine = Submarine()
submarine.use_path(lines)
print(submarine.final_position())

submarine = Submarine()
submarine.use_corrected_path(lines)
print(submarine.final_position())
