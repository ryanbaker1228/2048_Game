import Gamestate
import pygame as py



square_colors = {
    2: py.Color(250, 230, 85, 255),
    4: py.Color(214, 223, 78, 255),
    8: py.Color(250, 230, 85, 255),
    16: py.Color(250, 230, 85, 255),
    32: py.Color(250, 230, 85, 255),
    64: py.Color(250, 230, 85, 255),
    128: py.Color(250, 230, 85, 255),
    256: py.Color(250, 230, 85, 255),
    512: py.Color(250, 230, 85, 255),
    1024: py.Color(250, 230, 85, 255),
    2048: py.Color(250, 230, 85, 255),
    4096: py.Color(250, 230, 85, 255),
    8192: py.Color(250, 230, 85, 255),
}


class GUI:
    def __init__(self):
        self.screen_size = 600
        self.square_size = 135
        self.border_size = (self.screen_size - self.square_size * 4) / 5

        self.window = py.display.set_mode((self.screen_size, self.screen_size))
        self.font = py.font.Font('freesansbold.ttf', 40)

    def DrawGame(self, gamestate: Gamestate.Gamestate):
        for square in range(16):
            row = square // 4
            col = square % 4

            centerX = col * self.square_size + (col + 1) * self.border_size
            centerY = row * self.square_size + (row + 1) * self.border_size

            number = gamestate.board[row][col]
            color = py.Color(50, 200, 140, 255)
            black = py.Color(0, 0, 0, 255)
            text = self.font.render(str(number), True, black, None)

            d_rect = py.Rect(centerX, centerY, self.square_size, self.square_size)
            py.draw.rect(self.window, color, d_rect)
            self.window.blit(text, text.get_rect(center=d_rect.center))
