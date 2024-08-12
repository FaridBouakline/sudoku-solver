import tkinter as tk
from tkinter import messagebox
import random

class SudokuSolver:
    def __init__(self, board=9):
        if board:
            self.board = board
        else:
            self.board = [[0 for _ in range(9)] for _ in range(9)]

    # ... (keep other methods as they were) ...

    def initialize_board(self, num_cells):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        cells_filled = 0
        
        while cells_filled < num_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            
            if self.board[row][col] == 0 and self.valid(num, (row, col)):
                self.board[row][col] = num
                cells_filled += 1

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def valid(self, num, pos):
        # Check row
        for j in range(len(self.board[0])):
            if self.board[pos[0]][j] == num and pos[1] != j:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False

        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

# Example usage
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

solver = SudokuSolver(board)
print("Sudoku puzzle:")
solver.print_board()
print("\nSolving...\n")
solver.solve()
print("Solved Sudoku:")
solver.print_board()
class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.cells = {}
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                cell = tk.Entry(self.master, width=2, font=('Arial', 18), justify='center')
                cell.grid(row=i, column=j, padx=1, pady=1)
                if (i in [0, 1, 2, 6, 7, 8] and j in [3, 4, 5]) or (i in [3, 4, 5] and j in [0, 1, 2, 6, 7, 8]):
                    cell.config(bg='lightgray')
                self.cells[(i, j)] = cell

    def create_buttons(self):
        solve_button = tk.Button(self.master, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=3, columnspan=3, pady=10)
        
        clear_button = tk.Button(self.master, text="Clear", command=self.clear_grid)
        clear_button.grid(row=9, column=0, columnspan=3, pady=10)

        initialize_button = tk.Button(self.master, text="Initialize", command=self.initialize_sudoku)
        initialize_button.grid(row=9, column=3, columnspan=3, pady=10)
    
    def initialize_sudoku(self):
        num_cells = 20  # You can adjust this number or make it user-input
        self.solver.initialize_board(num_cells)
        self.set_board(self.solver.board)    

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[(i, j)].get()
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                self.cells[(i, j)].delete(0, tk.END)
                self.cells[(i, j)].insert(0, str(board[i][j]) if board[i][j] != 0 else "")

    def solve_sudoku(self):
        self.solver.board = self.get_board()
        if self.solver.solve():
            self.set_board(self.solver.board)
        else:
            messagebox.showinfo("No Solution", "This Sudoku puzzle has no solution.")


    def clear_grid(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)

def main():
    root = tk.Tk()
    SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()