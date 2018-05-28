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


class OutOfFieldError(Exception):
    pass


class AlreadyOccupiedError(Exception):
    pass


class BoardTree():
    def __init__(self, cmp_turn, usr_turn, free_cells, cmp_list, usr_list):
        self.free_cells = free_cells[:]
        self.free_cells.remove(usr_turn if usr_turn else cmp_turn)
        self.childs = []

        self.cmp_turn = cmp_turn
        self.usr_turn = usr_turn

        self.cmp_list = cmp_list[:]
        self.cmp_list.append(cmp_turn)

        self.usr_list = usr_list[:]
        self.usr_list.append(usr_turn)

        self.all_weights = 0
        self.my_weight = self.self_evaluate()

    def add_turn(self, pos, t_type):
        added = BoardTree(pos if t_type == "cmp" else None,
                          pos if t_type == "usr" else None, self.free_cells,
                          self.cmp_list, self.usr_list)
        self.childs.append(added)
        return added


    def self_evaluate(self):
        cmb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
               (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]
        for i in cmb:
            if i[0] in self.usr_list and i[1] in self.usr_list and i[2] in self.usr_list:
                return -1
            elif i[0] in self.cmp_list and i[1] in self.cmp_list and i[2] in self.cmp_list:
                return 1
        return 0

    def __repr__(self):
        return f"CT-{self.cmp_turn}, UT-{self.usr_turn}, Free-{self.free_cells}"


class Board():
    def __init__(self):
        self.board = [["   " for i in range(3)] for i in range(3)]
        self.previous_turn = None
        self.board_tree = None

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
                elif self.board[i[0][0]][i[0][1]] == " O ":
                    self.board[i[0][0]][i[0][1]] = "[O]"
                    self.board[i[1][0]][i[1][1]] = "[O]"
                    self.board[i[2][0]][i[2][1]] = "[O]"
                    return 1
                else:
                    return 0

    def set(self, num, sign):
        variants = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1),
                    6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
        if num in variants:
            if self.board[variants[num][0]][variants[num][1]] == "   ":
                self.board[variants[num][0]][variants[num][1]] = sign
                self.previous_turn = (sign, variants[num][1])
            else:
                raise AlreadyOccupiedError
        else:
            raise OutOfFieldError

    def init_tree(self, pos):
        self.tree = BoardTree(None, pos, [1, 2, 3, 4, 5, 6, 7, 8, 9], [], [])
        state = 0

        def recursive(tree, state):
            state += 1
            if tree.free_cells != []:
                for i in tree.free_cells:
                    if state % 2 == 1:
                        res = tree.add_turn(i, "cmp")
                    else:
                        res = tree.add_turn(i, "usr")
                    if res.my_weight==0:
                        recursive(res, state)
                    else:
                        res.all_weights=res.my_weight
            else:
                return 0

        def recursive_weight(tree):
            if tree.childs!=[]:
                tree.all_weights=sum([recursive_weight(i) for i in tree.childs])
                return sum([recursive_weight(i) for i in tree.childs])
            else:
                return tree.all_weights

        recursive(self.tree, state)
        recursive_weight(self.tree)

    def get_the_best(self):
            res=[]
            best= sorted(list(map(lambda z: z.all_weights, self.tree.childs)))
            print (best)
            for i in self.tree.childs:
                if i.all_weights==best[0]:
                    return i


    def get_on_usr_input(self, pos):
        for i in self.tree.childs:
            if i.usr_turn == pos:
                return i

    def turn(self, num):
        if num==0:
            turn = int(input(">> "))
            x.set(turn, " X ")
            x.init_tree(turn)
            return 0

        if num%2==1:
            self.tree=self.get_the_best()
            self.set(self.tree.cmp_turn, " O ")
        else:
            turn = int(input(">> "))
            self.tree=self.get_on_usr_input(turn)
            print (self.tree.childs)
            self.set(turn, " X ")

x = Board()


for i in range(9):
    x.check()
    print(x)
    x.turn(i)

    # print(list(map(lambda z: z.all_weights, x.tree.childs)))
    # print(x.tree.childs[0].all_weights)
    # print(x.tree.childs[0].childs[0].all_weights)
    # print(x.tree.childs[0].childs[0].childs[0])
    # print(x.tree.childs[0].childs[0].childs[0].childs[0])
    # print(x.tree.childs[0].childs[0].childs[0].childs[0].childs[0])
    # print(x.tree.childs[0].childs[0].childs[0].childs[0].childs[0].childs[0])
    # print(x.tree.childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].childs[0])
    # print(x.tree.childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].usr_list)
    # print(x.tree.childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].cmp_list)
    # print(x.tree.childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].childs[0].childs[0])
