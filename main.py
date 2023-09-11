import pygame as py
import Gamestate
import GUI


def main():
    py.init()
    gamestate = Gamestate.Gamestate(4)
    gui = GUI.GUI(gamestate.size)

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


        gui.DrawGame(gamestate)
        py.display.flip()
        clock.tick(60)

        if py.time.get_ticks() - timer > 1000:
            timer = py.time.get_ticks()
            gamestate.addTile()

if __name__ == main():
    main()
