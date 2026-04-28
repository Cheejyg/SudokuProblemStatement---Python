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


def test_cell_to_rowcol():
    sudoku = Sudoku()
    assert sudoku.cell_to_rowcol("B3") == (1, 2)
    assert sudoku.cell_to_rowcol("C5") == (2, 4)
    assert sudoku.cell_to_rowcol("A3") == (0, 2)
    assert sudoku.cell_to_rowcol("I4") == (8, 3)
    assert sudoku.cell_to_rowcol("A1") == (0, 0)
    assert sudoku.cell_to_rowcol("C1") == (2, 0)
    assert sudoku.cell_to_rowcol("A-1") is None
    assert sudoku.cell_to_rowcol("A0") is None
    assert sudoku.cell_to_rowcol("A9") == (0, 8)
    assert sudoku.cell_to_rowcol("A10") is None
    assert sudoku.cell_to_rowcol("J-1") is None
    assert sudoku.cell_to_rowcol("J0") is None
    assert sudoku.cell_to_rowcol("J9") is None
    assert sudoku.cell_to_rowcol("J10") is None


def test_enter_and_clear_number():
    sudoku = Sudoku()
    number = sudoku.generate_number(1, 9)
    row = sudoku.generate_number(0, 8)
    col = sudoku.generate_number(0, 8)
    while (row, col) in sudoku.pre_filled_cells:
        number = sudoku.generate_number(1, 9)
        row = sudoku.generate_number(0, 8)
        col = sudoku.generate_number(0, 8)
    cell = sudoku.rowcol_to_cell(row, col)
    sudoku.enter_number(number, cell)
    assert sudoku.grid[row][col] == number

    sudoku.clear_cell(cell)
    assert sudoku.grid[row][col] is None
