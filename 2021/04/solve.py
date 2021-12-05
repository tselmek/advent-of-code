from typing import List
import numpy as np

lines = [line.rstrip("\n") for line in open("example.txt")]


class Bingo():
    ALL = []

    def __init__(self, board) -> None:
        self.board = np.array(board)
        self.unmarked = np.array([[True for _ in range(5)] for _ in range(5)])

        self.indices = {}
        for l, line in enumerate(self.board):
            for c, number in enumerate(line):
                self.indices[number] = (l, c)

    def mark_number(self, number: int) -> bool:
        if number not in self.indices:
            return False

        l, c = self.indices[number]
        self.unmarked[l, c] = False

        return self.check_victory(l, c)

    def check_victory(self, line: int, column: int) -> bool:
        check_line = sum(self.unmarked[line]) == 0
        check_column = sum(self.unmarked[:, column]) == 0
        return check_line or check_column

    def sum_of_unmarked_numbers(self) -> int:
        return sum(sum(np.multiply(self.board, self.unmarked)))

    def score(self, last_number: int) -> int:
        return last_number * self.sum_of_unmarked_numbers()

    def reset_all() -> None:
        for board in Bingo.ALL:
            board.unmarked = np.array(
                [[True for _ in range(5)] for _ in range(5)])


def process_bingo(lines: List[str]) -> List[int]:
    draw_order = list(map(int, lines[0].split(",")))

    # Instanciate the bingo board
    k = 2
    while k + 5 <= len(lines):
        board = [
            list(map(int, board_line.strip().replace("  ", " ").split(" "))) for board_line in lines[k: k+5]
        ]
        Bingo.ALL.append(
            Bingo(board)
        )
        k += 6

    return draw_order


def first_winning_board(draw_order: List[int]) -> int:
    # Mark the numbers on the boards
    for number in draw_order:
        for board in Bingo.ALL:
            if board.mark_number(number):
                return board.score(number)


def last_winning_board(draw_order: List[int]) -> int:
    bingos = Bingo.ALL[:]
    for number in draw_order:
        print(number)
        for k, board in enumerate(bingos):
            if board.mark_number(number):
                print(board.unmarked)
                last_bingo = bingos.pop(k)
                if len(bingos) == 0:
                    return last_bingo.score(number)


draw_order = process_bingo(lines)

print(first_winning_board(draw_order))

Bingo.reset_all()

print(last_winning_board(draw_order))
