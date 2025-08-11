import pyxel
from CanvasDataVerPyxel import CanvasData
from MapData import MapData

MASU_SIZE = 32
BAIRITU = 2
SCREEN_WIDTH,SCREEN_HEIGHT = 1400,MASU_SIZE*10*BAIRITU


class CanvasData:
    def __init__(self, master):
        pyxel.load("GameYukanuriPrototype001verPyxel001.pyxres")
#        directory = ""
        pass

    def paint(self, mapdata, cx, cy):
        for x in range(10):
            for y in range(10):
                if mapdata.is_back_kuro(y, x) == True:
                    pyxel.rect(MASU_SIZE * x * BAIRITU, MASU_SIZE * y * BAIRITU, MASU_SIZE * BAIRITU, MASU_SIZE * BAIRITU, 5)
                    pass
                if mapdata.is_back_renga(y, x) == True:
                    pyxel.blt(MASU_SIZE * x * BAIRITU +16, MASU_SIZE * y * BAIRITU+16, 0, MASU_SIZE * 0, MASU_SIZE * 1, MASU_SIZE, MASU_SIZE, 1, 0, BAIRITU)
                    pass
        pass

    def pack(self):
        pass

    def delete(self, s):
        pass
    
    def clear(self, men):
        self.canvas.create_text(550,420,text=str(men)+"面クリア！！",tag="clear_tag")
        pass

    def item_area_init(self, orange_hake_count,
            kuro_hake_count, orange_roller_count,
            kuro_roller_count, small_hammer_count,
            big_hammer_count, orange_colorball_count,
            kuro_colorball_count):
        pass
    def item_count_repaint(self, orange_hake_count,
            kuro_hake_count, orange_roller_count,
            kuro_roller_count, small_hammer_count,
            big_hammer_count, orange_colorball_count,
            kuro_colorball_count):
        pass
    def hake(self, c1, c2, c3, c4, hake_switch, cx, cy):
        if hake_switch[0] == 1:
            self.create_rectangle(50*(cx-1),50*cy,50*cx,50*(cy+1),c1,3,"item_waku")
            pass
        if hake_switch[1] == 1:
            self.create_rectangle(50*cx,50*(cy-1),50*(cx+1),50*cy,c2,3,"item_waku")
            pass
        if hake_switch[2] == 1:
            self.create_rectangle(50*(cx+1),50*cy,50*(cx+2),50*(cy+1),c3,3,"item_waku")
            pass
        if hake_switch[3] == 1:
            self.create_rectangle(50*cx,50*(cy+1),50*(cx+1),50*(cy+2),c4,3,"item_waku")
            pass
        pass
    
    def roll(self, c1, c2, c3, c4, mass_continued_num, cx, cy):
        if mass_continued_num[0] > 0:
            self.create_rectangle(50*(cx-mass_continued_num[0]),50*cy,50*cx,50*(cy+1),c1,5,"item_waku")
            pass
        if mass_continued_num[1] > 0:
            self.create_rectangle(50*cx,50*(cy-mass_continued_num[1]),50*(cx+1),50*cy,c2,5,"item_waku")
            pass
        if mass_continued_num[2] > 0:
            self.create_rectangle(50*(cx+1),50*cy,50*(cx+mass_continued_num[2]+1),50*(cy+1),c3,5,"item_waku")
            pass
        if mass_continued_num[3] > 0:
            self.create_rectangle(50*cx,50*(cy+1),50*(cx+1),50*(cy + mass_continued_num[3]+1),c4,5,"item_waku")
            pass
        pass

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title="床塗りげ～む")


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
        pyxel.cls(7)
        self.repaint()
        pass

    def repaint(self):
        self.canvasdata.paint(self.mapdata, self.cx, self.cy)
        pass
    
    def clear(self):
        pass


App()