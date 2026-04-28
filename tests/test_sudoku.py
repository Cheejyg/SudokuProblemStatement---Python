import random

from app.sudoku import Sudoku


def test_init():
    pre_filled_numbers = random.randint(0, (9 * 9) - 1)
    sudoku = Sudoku(
        pre_filled_numbers=pre_filled_numbers,
    )
    assert sudoku.pre_filled_numbers == pre_filled_numbers
