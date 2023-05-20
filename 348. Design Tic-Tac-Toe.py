class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n
        self.col_tot = [0] * n
        self.row_tot = [0] * n
        self.left_diag = 0
        self.right_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        curr_val = 1 if player == 1 else -1
        win_con = self.n * curr_val
        self.col_tot[col] += curr_val
        if self.col_tot[col] == win_con: return player
        self.row_tot[row] += curr_val
        if self.row_tot[row] == win_con: return player
        if row == col:
            self.left_diag += curr_val
        if self.left_diag == win_con:
            return player
        if row + col == self.n - 1:
            self.right_diag += curr_val
        if self.right_diag == win_con:
            return player
        return 0
