board = """
1    |2    |3
 {} | {} | {}
_____|_____|_____
4    |5    |6
 {} | {} | {}
_____|_____|_____
7    |8    |9
 {} | {} | {}
     |     |
"""


class Board():
    def __init__(self):
        self.board = [["   " for i in range(3)] for i in range(3)]

    def __str__(self):
        return board.format(*[item for sub in self.board for item in sub])

    def check(self,):
        pos = [[(0, 0), (0, 1), (0, 2)],
               [(1, 0), (1, 1), (1, 2)],
               [(2, 0), (2, 1), (2, 2)],

               [(0, 0), (1, 0), (2, 0)],
               [(0, 1), (1, 1), (2, 1)],
               [(0, 2), (1, 2), (2, 2)],

               [(0, 0), (1, 1), (2, 2)],
               [(0, 2), (1, 1), (2, 0)]]

        for i in pos:
            if self.board[i[0][0]][i[0][1]] == self.board[i[1][0]][i[1][1]]\
                    == self.board[i[2][0]][i[2][1]] != "   ":
                if self.board[i[0][0]][i[0][1]] == " X ":
                    self.board[i[0][0]][i[0][1]] = "[X]"
                    self.board[i[1][0]][i[1][1]] = "[X]"
                    self.board[i[2][0]][i[2][1]] = "[X]"
                    return -1
                else:
                    self.board[i[0][0]][i[0][1]] = "[O]"
                    self.board[i[1][0]][i[1][1]] = "[O]"
                    self.board[i[2][0]][i[2][1]] = "[O]"
                    return 1

    def set(self, num, sign):
        variants = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1),
                    6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
        if num in variants:
            self.board[variants[num][0]][variants[num][1]] = sign


x = Board()

while True:
    print(x.check())
    print(x)
    x.set(int(input(">> ")), " O ")
