#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_args = len(sys.argv)

    if total_args != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    class NQueen:
        def __init__(self, N):
            if N < 4:
                raise ValueError("N must be at least 4")
            self.N = N
            self.board = [[0 for _ in range(N)] for _ in range(N)]
            self.solutions = []

        def solution(self):
            for i in self.solutions:
                final_sol = [[row, colum] for row, colum in enumerate(i)]
                print(final_sol)

        def is_safe(self, row, colum):
            for i in range(colum):
                if self.board[row][i] == 1:
                    return False
                for x, y in zip(range(row, -1, -1), range(colum, -1, -1)):
                    if self.board[x][y] == 1:
                        return False
                for x, y in zip(range(row, self.N, 1), range(colum, -1, -1)):
                    if self.board[x][y] == 1:
                        return False
            return True

        def solve(self, colum=0, solution=[]):
            if colum == self.N:
                self.solutions.append(solution.copy())
                return True
            result = False
            for i in range(self.N):
                if self.is_safe(i, colum):
                    self.board[i][colum] = 1
                    solution.append(i)
                    result = self.solve(colum + 1, solution) or result
                    solution.pop()
                    self.board[i][colum] = 0
            return result

    solver = NQueen(N)
    solver.solve()
    solver.solution()
