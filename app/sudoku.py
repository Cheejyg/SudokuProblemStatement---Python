import random


class Sudoku:
    def __init__(
        self,
        *,
        pre_filled_numbers: int = 30,
        empty_cells_representation: str = "_",
    ) -> None:
        self.pre_filled_numbers = pre_filled_numbers
        self.empty_cells_representation = empty_cells_representation
        self.grid: list[list[int | None]] = [[None for _ in range(9)] for _ in range(9)]
        self.pre_filled_cells = set()

        def generate_puzzle() -> None:
            for i in range(pre_filled_numbers):
                number = self.generate_number(1, 9)
                row = self.generate_number(0, 8)
                col = self.generate_number(0, 8)
                while (row, col) in self.pre_filled_cells:
                    number = self.generate_number(1, 9)
                    row = self.generate_number(0, 8)
                    col = self.generate_number(0, 8)
                # TODO: check_validity
                self.grid[row][col] = number
                self.pre_filled_cells.add((row, col))

        generate_puzzle()

    def generate_number(self, low: int, high: int) -> int:
        return random.randint(low, high)

    def cell_to_rowcol(self, cell: str) -> tuple[int, int] | None:
        if len(cell) != 2:
            return None

        row = cell[0].upper()
        col = cell[1]
        if not col.isdigit():
            return None
        col = int(col)

        if ord(row) not in range(ord("A"), ord("I") + 1) or col <= 0 or col > 9:
            return None

        return ord(row) - ord('A'), int(col) - 1

    def rowcol_to_cell(self, row: int, col: int) -> str | None:
        if row < 0 or col < 0 or row > 9 or col > 9:
            return None
        return chr(ord("A") + row) + str(col + 1)

    def enter_number(self, number: int, cell: str) -> None:
        if number not in range(1, 9 + 1):
            return None

        cell = self.cell_to_rowcol(cell)
        if not cell:
            return
        row, col = cell
        if (row, col) not in self.pre_filled_cells:
            self.grid[row][col] = number

    def clear_cell(self, cell: str) -> None:
        cell = self.cell_to_rowcol(cell)
        if not cell:
            return
        row, col = cell
        if (row, col) not in self.pre_filled_cells:
            self.grid[row][col] = None

    def request_hint(self) -> None:
        number = self.generate_number(1, 9)
        row = self.generate_number(0, 8)
        col = self.generate_number(0, 8)
        while (row, col) in self.pre_filled_cells:
            number = self.generate_number(1, 9)
            row = self.generate_number(0, 8)
            col = self.generate_number(0, 8)
        # TODO: check_validity
        self.grid[row][col] = number

    def check_validity(self) -> None:
        pass

    def display_grid(self) -> None:
        output = "    " + " ".join(map(str, [i + 1 for i in range(0, 9)])) + "\n"

        j = ord("A")
        for row in range(len(self.grid)):
            output += "  " + chr(j)
            for col in range(len(self.grid[row])):
                output += " " + (str(self.grid[row][col]) if self.grid[row][col] else self.empty_cells_representation)
            output += "\n"
            j += 1

        print(output.rstrip())
