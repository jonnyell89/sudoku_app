from typing import List

from app.library.grids import empty_grid, valid_grid, invalid_row, invalid_col, invalid_subgrid, easy_grid, medium_grid, hard_grid, expert_grid, master_grid, extreme_grid, brute_force, mit, full_grid
from config.config import GRID_SIZE

def print_formatted_grid(grid: List[List[int]]) -> None:

    """
    Prints the grid as a two-dimensional matrix, with visual separators forming nine 3X3 subgrids.
    
    """

    print("--------------------")

    for row_index in range(GRID_SIZE):

        # Prints inner horizontal subgrid construction lines.
        if row_index > 0 and row_index % 3 == 0:

            print("-" * 15)

        for col_index in range(GRID_SIZE):

            # Prints inner vertical subgrid construction lines.
            if col_index > 0 and col_index % 3 == 0:

                print(" | ", end="")

            if col_index == GRID_SIZE - 1:

                # Ensures a new line after printing last cell in row.
                print(grid[row_index][col_index])

            else:

                # Ensures each cell is printed on the same line.
                print(grid[row_index][col_index], end="")

if __name__ == "__main__":

    print("--------------------")
