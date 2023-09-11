import pygame as py
import Gamestate
from GUI import Gui


def main():
    py.init()
    gamestate = Gamestate.Gamestate(4)
    gui = Gui.GUI(4)

    clock = py.time.Clock()
    timer = py.time.get_ticks()

    running = True
    while running:
        if gamestate.gameOver(): running = False

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

            if event.type == py.KEYDOWN:
                gamestate.shiftTiles(event.key)


        #gui.DrawGame(gamestate)
        gui.drawStartScreen()
        py.display.flip()
        clock.tick(60)

        if py.time.get_ticks() - timer > 500:
            timer = py.time.get_ticks()
            gamestate.addTile()

if __name__ == main():
    main()
