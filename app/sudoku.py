class Sudoku:
    def __init__(
        self,
        *,
        pre_filled_numbers: int = 30,
        empty_cells_representation: str = "_",
    ) -> None:
        self.pre_filled_numbers = pre_filled_numbers
        self.empty_cells_representation = empty_cells_representation
        self.grid = [[None for _ in range(9)] for _ in range(9)]

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
