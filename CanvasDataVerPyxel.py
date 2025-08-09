import pyxel

SCREEN_WIDTH,SCREEN_HEIGHT = 1400,800

class CanvasData:
    def __init__(self, master):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title="床塗りげ～む")
        pyxel.load("GameYukanuriPrototype001verPyxel001.pyxres")
        directory = "./gazou/"
        pass

    def paint(self, mapdata, cx, cy):
        for x in range(10):
            for y in range(10):
                if mapdata.is_back_kuro(y, x) == True:
                    

                    
                    pyxel.blt(50 * x + 5, 50 * y + 5, 0, 32, 32, 32,None, 1, 2)
        pass
