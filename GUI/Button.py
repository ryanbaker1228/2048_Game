import pygame as py


class Button:
    def __init__(self, x, y, width, height, text, font_size=24, bg_color=(0, 128, 255), text_color=(255, 255, 255)):
        self.rect = py.Rect(x, y, width, height)
        self.text = text
        self.font = py.font.Font(None, font_size)
        self.bg_color = bg_color
        self.text_color = text_color
        self.clicked = False

    def draw(self, screen):
        py.draw.rect(screen, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event, callback=None):
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                if callback:
                    callback()

    def reset(self):
        self.clicked = False