import pyxel
from CanvasDataVerPyxel import CanvasData
from MapData import MapData

SCREEN_WIDTH,SCREEN_HEIGHT = 1400,800
MASU_SIZE = 32
BAIRITU = 2

class CanvasData:
    def __init__(self, master):
        pyxel.load("GameYukanuriPrototype001verPyxel001.pyxres")
#        directory = "./gazou/"
        pass

    def paint(self, mapdata, cx, cy):
        for x in range(10):
            for y in range(10):
                if mapdata.is_back_kuro(y, x) == True:
                    

                    
                    pyxel.rect(MASU_SIZE * x * BAIRITU, MASU_SIZE * y * BAIRITU, MASU_SIZE * BAIRITU, MASU_SIZE * BAIRITU, 4)
                    pass
                if mapdata.is_back_renga(y, x) == True:
                    pyxel.blt(MASU_SIZE * x * BAIRITU, MASU_SIZE * y * BAIRITU, 0, MASU_SIZE * 0, MASU_SIZE * 1, MASU_SIZE, MASU_SIZE, 1, 2, BAIRITU)
                    pass
        pass


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title="床塗りげ～む")
        pyxel.load("GameYukanuriPrototype001verPyxel001.pyxres")

        self.cx = 0
        self.cy = 0

        self.mapdata = MapData([
            [0,0,0,0,0,0,0,0,0,0],
            [0,2,2,2,0,0,2,2,2,0],
            [0,2,0,0,1,0,0,0,2,0],
            [0,2,0,0,1,0,0,0,2,0],
            [1,2,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,0,2,0],
            [0,2,0,0,0,0,0,0,2,0],
            [0,2,2,2,2,2,2,2,2,0],
            [0,0,0,0,0,0,0,0,0,0]
        ],[
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])


        self.canvasdata = CanvasData("")#初期化


        pyxel.run(self.update, self.draw)

    def update(self):
       
        pass

    def draw(self):
        pyxel.cls(16)

        self.repaint()
        pass

    def repaint(self):
        
        self.canvasdata.paint(self.mapdata, self.cx, self.cy)

App()