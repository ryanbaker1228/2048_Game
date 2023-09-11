from enum import Enum
import random
import math


class Direction(Enum):
    right = 0,
    left = 1,
    up = 2,
    down = 3


class Gamestate:
    def __init__(self):
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        rand_num_1 = random.random()
        rand_num_2 = random.random()
        if rand_num_1 > 0.99:
            initial_number_1 = 8
        elif rand_num_1 > 0.9:
            initial_number_1 = 4
        else:
            initial_number_1 = 2

        if rand_num_2 > 0.99:
            initial_number_2 = 8
        elif rand_num_2 > 0.9:
            initial_number_2 = 4
        else:
            initial_number_2 = 2

        square_1 = math.floor(random.random() * 16)
        square_2 = math.floor(random.random() * 16)
        while square_2 == square_1:
            square_2 = math.floor(random.random() * 16)

        self.board[square_1 // 4][square_1 % 4] = initial_number_1
        self.board[square_2 // 4][square_2 % 4] = initial_number_2

    def MakeMove(self, direction: Direction):
        pass

