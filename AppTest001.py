import pyxel
from CanvasDataVerPyxel import CanvasData
from MapData import MapData
import PyxelUniversalFont as puf
from ImageObject import ImageObject


MASU_SIZE = 32
BAIRITU = 2
SCREEN_WIDTH,SCREEN_HEIGHT = 1400,MASU_SIZE*10*BAIRITU
FILENAMECHARACTER = "character00164x64.jpg"

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
クラス　キャンバスデータ
　ペイント
　パック
　デリート
　クリア
　アイテム　エリア　初期化
　アイテム　カウント　リペイント
　ハケ
　ロール
　
'''
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
                if mapdata.is_back_orange(y, x) == True:
                    pyxel.rect(MASU_SIZE * x * BAIRITU, MASU_SIZE * y * BAIRITU, MASU_SIZE * BAIRITU, MASU_SIZE * BAIRITU, 8)
                    pass
                if mapdata.is_back_renga(y, x) == True:
                    pyxel.blt(MASU_SIZE * x * BAIRITU +16, MASU_SIZE * y * BAIRITU+16, 0, MASU_SIZE * 0, MASU_SIZE * 1, MASU_SIZE, MASU_SIZE, 1, 0, BAIRITU)
                    pass

#        pyxel.blt(cx * MASU_SIZE *BAIRITU + 16,  cy * MASU_SIZE *BAIRITU + 16,0, MASU_SIZE * 0, MASU_SIZE * 2, MASU_SIZE, MASU_SIZE, 1, 0, BAIRITU)
        pass

    def pack(self):
        pass

    def delete(self, s):
        pass

    def clear(self, w, men):
        w.draw(400, 400, f"{men}面クリア！！！", 64, pyxel.COLOR_BLACK)

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

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
本クラス

'''
class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT, title="床塗りげ～む")

        self.writer = puf.Writer("misaki_gothic.ttf")#フォントを指定

        self.cx = 0#変数　プレイヤーキャラクターの座標
        self.cy = 0
        self.men = 1 #変数　面数
        self.clear_switch = 0 #フラグ　クリア条件
        self.clearCount = 0
        self.count = 0
        self.img = pyxel.Image(64, 64)
        self.img.load(x=0, y=0, filename="gazou/character00164x64.jpg")
        self.image_object = ImageObject(FILENAMECHARACTER, self.cx, self.cy)


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

        self.nokori = 0
        for i in self.mapdata.back:
            for j in i:
                if j == 0:
                    self.nokori = self.nokori + 1

        self.clearPoint = self.nokori



        self.canvasdata = CanvasData("")#初期化


        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btnp(pyxel.KEY_UP):
            self.key_up()
            pass
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.key_down()
            pass
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.key_left()
            pass
        elif pyxel.btnp(pyxel.KEY_RIGHT):
            self.key_right()
            pass
        else:
            pass
        pass

    def draw(self):
        pyxel.cls(7)
        self.repaint()
        self.image_object.set_pos(self.cx * MASU_SIZE * BAIRITU,self.cy * MASU_SIZE * BAIRITU)
        self.image_object.draw()
#        pyxel.blt(0, 0, self.img, 0, 0, self.img.width, self.img.height)表示を試す
        self.writer.draw(10 * MASU_SIZE * BAIRITU + 8,0, f"残りのマス：{self.nokori} {self.clearCount}　{self.count} {self.clearPoint}", 32, pyxel.COLOR_BLACK)
        pass

    def repaint(self):
        self.canvasdata.paint(self.mapdata, self.cx, self.cy)
        pass

    def clear(self):
        pass

    def key_up(self):
        self.item_init()
        if self.cy > 0:
            if self.mapdata.is_back_kuro(self.cy - 1, self. cx) == True:
                self.cy = self.cy - 1
                self.move_finish()
        pass

    def key_down(self):
        self.item_init()
        if self.cy < 9:
            if self.mapdata.is_back_kuro(self.cy + 1, self. cx) == True:
                self.cy = self.cy + 1
                self.move_finish()
        pass

    def key_left(self):
        self.item_init()
        if self.cx > 0:
            if self.mapdata.is_back_kuro(self.cy , self. cx - 1) == True:
                self.cx = self.cx - 1
                self.move_finish()
        pass

    def key_right(self):
        self.item_init()
        if self.cx < 9:
            if self.mapdata.is_back_kuro(self.cy , self. cx + 1) == True:
                self.cx = self.cx + 1
                self.move_finish()
        pass

    def item_init(self):
        pass

    def move_finish(self):

        self.canvasdata.clear(self.writer, self.men)
        self.clear_switch = 1

        self.mapdata.back_to_orange(self.cy, self.cx)
        self.mapdata.delete_item(self.cy, self.cx)
        self.count = self.count + 1
#        self.repaint()
#        self.item_count_repaint()
#        self.clear()
        pass
App()
