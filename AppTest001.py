import pyxel

SCREEN_WIDTH,SCREEN_HEIGHT = 1400,800


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title="床塗りげ～む")

        pyxel.run(self.update, self.draw)
        pass
    def update(self):
        pass
    def draw(self):
        pass

App()