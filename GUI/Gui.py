import Gamestate
import pygame as py
import math
from GUI import Button

start_button = Button.Button(200, 200, 200, 200, "Start!")
square_colors = [
    py.Color(40, 42, 58, 255),
    py.Color(250, 230, 85, 255),
    py.Color(214, 223, 78, 255),
    py.Color(177, 216, 85, 255),
    py.Color(143, 205, 99, 255),
    py.Color(115, 193, 114, 255),
    py.Color(94, 179, 126, 255),
    py.Color(80, 165, 134, 255),
    py.Color(72, 150, 139, 255),
    py.Color(67, 130, 85, 255),
    py.Color(64, 119, 139, 255),
    py.Color(62, 104, 138, 255),
    py.Color(62, 87, 136, 255),
    py.Color(65, 70, 130, 255),
]


class GUI:
    def __init__(self, rows):
        self.screen_size = 640
        self.border_size = 60 / rows
        self.square_size = (640 - (rows + 1) * self.border_size) / rows

        self.window = py.display.set_mode((self.screen_size, self.screen_size))
        self.window.fill((30, 31, 43, 255))
        self.font = py.font.Font('freesansbold.ttf', math.ceil(self.square_size * 0.3))

    def DrawGame(self, gamestate: Gamestate.Gamestate):
        for square in range(gamestate.size ** 2):
            row = square // gamestate.size
            col = square % gamestate.size

            centerX = col * self.square_size + (col + 1) * self.border_size
            centerY = row * self.square_size + (row + 1) * self.border_size

            degree = gamestate.tiles[square]
            color = square_colors[degree]

            if degree > 0:
                text = self.font.render(str(2 ** degree), True, py.Color(0, 0, 0, 255), None)
            else:
                text = self.font.render('', True, py.Color(0, 0, 0, 255), None)

            d_rect = py.Rect(centerX, centerY, self.square_size, self.square_size)
            py.draw.rect(self.window, color, d_rect)
            self.window.blit(text, text.get_rect(center=d_rect.center))

    def drawStartScreen(self):
        text = self.font.render("2048", self.screen_size // 2, self.screen_size // 2 - 40)
        d_rect = py.Rect(0, 0, self.screen_size, self.screen_size)
        self.window.blit(text, text.get_rect(center=d_rect.center))
        start_button.draw(self.window)

