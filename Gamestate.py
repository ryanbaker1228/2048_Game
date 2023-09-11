from enum import Enum
import random
import math


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

        self.board[square_1 % 4][square_1 // 4] = initial_number_1
        self.board[square_2 % 4][square_2 // 4] = initial_number_2

    def MakeMove(self, direction: str):
        if direction == 'right':
            for row in self.board:
                for tile in range(3, -1, -1):
                    if tile == 3 or row[tile] == 0: continue

                    for index in range(tile + 1, 4):
                        if index == 4:
                            break

                        if row[index] == row[tile]:
                            row[index] *= 2
                            row[tile] = 0
                            break

                        elif row[index] != 0:
                            row[index - 1] = row[tile]
                            if index != tile + 1: row[tile] = 0
                            break

                        elif index == 3:
                            row[index] = row[tile]
                            row[tile] = 0
                            break

            rand_num = random.random()
            if rand_num > 0.99:
                number = 8
            elif rand_num > 0.9:
                number = 4
            else:
                number = 2

            square = math.floor(random.random() * 16)
            while self.board[square % 4][square // 4] > 0:
                square = math.floor(random.random() * 16)

            self.board[square % 4][square // 4] = number

        elif direction == 'left':
            for row in self.board:
                row.reverse()

            self.MakeMove('right')

            for row in self.board:
                row.reverse()

        elif direction == 'up':
            self.board = Transpose(self.board)
            self.MakeMove('left')
            self.board = Transpose(self.board)

        elif direction == 'down':
            self.board = Transpose(self.board)
            self.MakeMove('right')
            self.board = Transpose(self.board)

    def GameOver(self):
        board = self.board[0] + self.board[1] + self.board[2] + self.board[3]
        if board.count(0) > 0: return False

        for row in self.board:
            for index in range(3):
                if row[index] == row[index + 1]: return False

        board = Transpose(self.board)
        for row in board:
            for index in range(3):
                if row[index] == row[index + 1]: return False

        return True

def Transpose(matrix):
    transposed = [[0] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            transposed[i][j] = matrix[j][i]

    return transposed