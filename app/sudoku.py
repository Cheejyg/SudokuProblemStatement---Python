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

        def generate_number(low: int, high: int) -> int:
            return random.randint(low, high)

        def generate_puzzle() -> None:
            self.pre_filled_cells = set()

            for i in range(pre_filled_numbers):
                number = generate_number(1, 9)
                row = generate_number(0, 8)
                col = generate_number(0, 8)
                while (row, col) in self.pre_filled_cells:
                    number = generate_number(1, 9)
                    row = generate_number(0, 8)
                    col = generate_number(0, 8)
                # TODO: check_validity
                self.grid[row][col] = number
                self.pre_filled_cells.add((row, col))

        generate_puzzle()

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
