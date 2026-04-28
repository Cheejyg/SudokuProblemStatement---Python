import random

from app.sudoku import Sudoku


def test_init():
    pre_filled_numbers = random.randint(0, (9 * 9) - 1)
    sudoku = Sudoku(
        pre_filled_numbers=pre_filled_numbers,
    )
    assert sudoku.pre_filled_numbers == pre_filled_numbers


def test_generate_puzzle():
    pre_filled_numbers = random.randint(0, (9 * 9) - 1)
    sudoku = Sudoku(
        pre_filled_numbers=pre_filled_numbers,
    )
    filled_numbers = 0
    for row in range(len(sudoku.grid)):
        for col in range(len(sudoku.grid[row])):
            if sudoku.grid[row][col]:
                filled_numbers += 1
    assert pre_filled_numbers == filled_numbers
