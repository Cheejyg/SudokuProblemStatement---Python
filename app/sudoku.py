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
