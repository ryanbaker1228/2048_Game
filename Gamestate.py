import random
import math


class Gamestate:
    def __init__(self):
        self.board = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        rand_num = random.random()
        if rand_num > 0.99:
            initial_number = 8
        elif rand_num > 0.9:
            initial_number = 4
        else:
            initial_number = 2

        square = math.floor(random.random() * 16)
        self.board[square // 4][square % 4] = initial_number

