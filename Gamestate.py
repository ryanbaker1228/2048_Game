import random
import math
import pygame as py


class Gamestate:
    def __init__(self, rows: int):
        self.size = rows
        self.tiles = [0] * rows ** 2

        self.addTile()
        self.addTile()

    def shiftTiles(self, direction: int):
        copy = self.tiles

        if direction in (py.K_UP, py.K_DOWN):
            self.transposeTiles()

        if direction in (py.K_RIGHT, py.K_DOWN):
            self.mirrorTiles()

        rows = [self.tiles[row_start:row_start + self.size] for row_start in range(0, self.size ** 2, self.size)]

        for row_num in range(self.size):
            row = rows[row_num]
            for tile in range(1, self.size):
                degree = row[tile]
                if degree == 0: continue

                for destination in range(tile, -1, -1):
                    if destination == 0:
                        row[destination] = degree
                        row[tile] = 0
                        break

                    if row[destination - 1] == 0:
                        continue

                    if row[destination - 1] == degree:
                        row[destination - 1] += 1
                        row[tile] = 0
                        break

                    row[tile] = 0
                    row[destination] = degree
                    break

            self.tiles[row_num * self.size:(row_num + 1) * self.size] = row

        if direction in (py.K_RIGHT, py.K_DOWN):
            self.mirrorTiles()

        if direction in (py.K_UP, py.K_DOWN):
            self.transposeTiles()

        if not self.tiles != copy:
            self.addTile()

    def addTile(self):
        if self.tiles.count(0) == 0: return

        tile = math.floor(random.random() * self.size ** 2)
        while self.tiles[tile] != 0:
            tile = math.floor(random.random() * self.size ** 2)

        degree = min(math.floor(-math.log10(random.random())), 4) + 1

        self.tiles[tile] = degree

    def transposeTiles(self):
        transposed = [0] * self.size ** 2

        for tile in range(self.size ** 2):
            row = tile // self.size
            col = tile % self.size

            transposed[tile] = self.tiles[self.size * col + row]

        self.tiles = transposed

    def mirrorTiles(self):
        mirrored = []

        for row_number in range(self.size):
            row = self.tiles[row_number * self.size: (row_number + 1) * self.size]
            mirrored_row = row[::-1]  # Reverse the row to mirror it
            mirrored.extend(mirrored_row)

        self.tiles = mirrored

    def gameOver(self) -> bool:
        if self.tiles.count(0) > 0: return False

        rows = [self.tiles[row_start:row_start + self.size] for row_start in range(0, self.size ** 2, self.size)]
        self.transposeTiles()
        cols = [self.tiles[col_start:col_start + self.size] for col_start in range(0, self.size ** 2, self.size)]
        self.transposeTiles()

        for row in range(self.size):
            for tile in range(self.size - 1):
                if rows[row][tile] == rows[row][tile + 1]: return False
                if cols[row][tile] == cols[row][tile + 1]: return False

        return True

