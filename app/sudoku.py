import copy
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

        self._generate_puzzle()

    def _generate_puzzle(self) -> None:
        grid = [[None for _ in range(9)] for _ in range(9)]
        self.pre_filled_cells = set()
        self._solve(grid)

        for i in range(9 * 9 - self.pre_filled_numbers):
            row = self.generate_number(0, 8)
            col = self.generate_number(0, 8)
            while grid[row][col] is None:
                row = self.generate_number(0, 8)
                col = self.generate_number(0, 8)
            grid[row][col] = None

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] is not None:
                    self.pre_filled_cells.add((row, col))

        self.grid = grid

    def _display_welcome(self) -> None:
        print("Welcome to Sudoku!")
        print()
        print("Here is your puzzle:")
        self.display_grid()
        print()

    def play(self):
        self._display_welcome()
        while True:
            command = input("Enter command (e.g., A3 4, C5 clear, hint, check, quit):\n").strip().split(" ")
            if not command:
                continue

            if len(command) == 2:
                if len(command[0]) == 2:
                    if command[0][0].isalpha() and command[0][1].isdigit() and command[1].isdigit():
                        print()
                        if self.enter_number(int(command[1]), command[0]):
                            print("Move accepted.")
                        else:
                            print("Invalid move. " + command[0] + " is pre-filled.")
                        print()
                        print("Current grid:")
                        self.display_grid()
                        print()
                        if self.check_end():
                            print("You have successfully completed the Sudoku puzzle!")
                            input("Press any key to play again...")
                            self._generate_puzzle()
                            self._display_welcome()
                            continue
                    elif command[1] == "clear":
                        print()
                        if self.clear_cell(command[0]):
                            print("Move accepted.")
                        else:
                            print("Invalid move. " + command[0] + " is pre-filled.")
                        print()
                        print("Current grid:")
                        self.display_grid()
                        print()
                continue
            elif len(command) == 1:
                if command[0] == "hint":
                    self.request_hint()
                    print()
                elif command[0] == "check":
                    self.check_validity()
                    print()
                elif command[0] == "quit":
                    break
            else:
                continue

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
        if row < 0 or col < 0 or row >= 9 or col >= 9:
            return None
        return chr(ord("A") + row) + str(col + 1)

    def enter_number(self, number: int, cell: str) -> bool:
        if number not in range(1, 9 + 1):
            return False

        cell = self.cell_to_rowcol(cell)
        if not cell:
            return False

        row, col = cell
        if (row, col) in self.pre_filled_cells:
            return False

        self.grid[row][col] = number
        return True

    def clear_cell(self, cell: str) -> bool:
        cell = self.cell_to_rowcol(cell)
        if not cell:
            return False

        row, col = cell
        if (row, col) in self.pre_filled_cells:
            return False

        self.grid[row][col] = None
        return True

    def request_hint(self) -> None:
        grid = copy.deepcopy(self.grid)
        if not self._solve(grid):
            return

        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] is None:
                    print("Hint: Cell " + self.rowcol_to_cell(row, col) + " = ", grid[row][col])
                    return

    def check_validity(self) -> bool:
        for row in range(len(self.grid)):
            check = set()
            for col in range(len(self.grid[row])):
                if self.grid[row][col]:
                    if self.grid[row][col] in check:
                        print("Number", self.grid[row][col], "already exists in Row", chr(ord('A') + row) + ".")
                        return False
                    check.add(self.grid[row][col])

        for col in range(len(self.grid[0])):
            check = set()
            for row in range(len(self.grid)):
                if self.grid[row][col]:
                    if self.grid[row][col] in check:
                        print("Number", self.grid[row][col], "already exists in Col " + str(col + 1) + ".")
                        return False
                    check.add(self.grid[row][col])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = set()
                for x in range(3):
                    for y in range(3):
                        row = i + x
                        col = j + y
                        if self.grid[row][col]:
                            if self.grid[row][col] in check:
                                print("Number", self.grid[row][col], "already exists in the same 3×3 subgrid.")
                                return False
                            check.add(self.grid[row][col])

        print("No rule violations detected.")
        return True

    def check_move_validity(self, grid: list[list[int | None]], row: int, col: int, number: int) -> bool:
        for i in range(len(grid)):
            if i != col and grid[row][i] == number:
                return False

        for i in range(len(grid)):
            if i != row and grid[i][col] == number:
                return False

        i = (row // 3) * 3
        j = (col // 3) * 3
        for x in range(3):
            for y in range(3):
                if not (i + x == row or j + y == col) and grid[i + x][j + y] == number:
                    return False

        return True

    def check_end(self) -> bool:
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] is None:
                    return False

        for row in range(len(self.grid)):
            check = set()
            for col in range(len(self.grid[row])):
                if self.grid[row][col]:
                    if self.grid[row][col] in check:
                        return False
                    check.add(self.grid[row][col])

        for col in range(len(self.grid[0])):
            check = set()
            for row in range(len(self.grid)):
                if self.grid[row][col]:
                    if self.grid[row][col] in check:
                        return False
                    check.add(self.grid[row][col])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = set()
                for x in range(3):
                    for y in range(3):
                        row = i + x
                        col = j + y
                        if self.grid[row][col]:
                            if self.grid[row][col] in check:
                                return False
                            check.add(self.grid[row][col])

        return True

    def _solve(self, grid: list[list[int | None]]) -> bool:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] is None:
                    numbers = list(range(1, 9 + 1))
                    random.shuffle(numbers)
                    for number in numbers:
                        if self.check_move_validity(grid, row, col, number):
                            grid[row][col] = number
                            if self._solve(grid):
                                return True
                            grid[row][col] = None
                    return False
        return True

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
