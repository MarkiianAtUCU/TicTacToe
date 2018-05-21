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

    def check():
        pos = [[(0, 0), (0, 1), (0, 2)],
               [(1, 0), (1, 1), (1, 2)],
               [(2, 0), (2, 1), (2, 2)],

               [(0, 0), (1, 0), (2, 0)],
               [(0, 1), (1, 1), (2, 1)],
               [(0, 2), (1, 2), (2, 2)],

               [(0, 0), (1, 1), (2, 2)],
               [(0, 2), (1, 1), (2, 0)]]

        for i in range(8):
            pass


x = Board()

print(x)
