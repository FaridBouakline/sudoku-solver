import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    # ... (Keep the previous SudokuSolver class implementation here) ...

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
        board = self.get_board()
        solver = SudokuSolver(board)
        if solver.solve():
            self.set_board(solver.board)
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