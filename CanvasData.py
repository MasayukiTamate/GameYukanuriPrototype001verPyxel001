import tkinter as tk
from PIL import Image, ImageTk

ITEM_LIST_X1 = 50 + 500
ITEM_LIST_X2 = 100 + 50 + 500
ITEM_LIST_Y1 = 100
ITEM_LIST_Y2 = 200
ITEM_LIST_Y3 = 300
ITEM_LIST_Y4 = 400

LIST_TEXT_X1 = 0
LIST_TEXT_X2 = 0
LIST_ITEM_Y1 = 50
LIST_TEXT_Y1 = 100 - 10
LIST_ITEM_Y2 = 150
LIST_TEXT_Y2 = 200 - 10
LIST_ITEM_Y3 = 250
LIST_TEXT_Y3 = 300 - 10
LIST_ITEM_Y4 = 350
LIST_TEXT_Y4 = 400 - 10


class CanvasData:
    def __init__(self, master):
        self.canvas = tk.Canvas(master, width=700+5, height=500+5, bg="white")
        directory = "./gazou/"
        # ファイルパスを保持して、Pillow に渡すときは path を使う
        self.jiki_path = directory + "playerC50x50.png"
        self.blickblock_path = directory + "brickblock50x50.png"
        self.bakdan_path = directory + "bakudan50x50.png"
        self.hake_path = directory + "hake50x50.png"
        self.hake2_path = directory + "hakeb50x50.png"
        self.hummar_path = directory + "hummar50x50.png"
        self.roll_path = directory + "roll50x50.png"
        self.floor_path = directory + "floor50x50.png"
        self.floorPaint_path = directory + "floorPaint50x50.png"
        # tkinter 用の PhotoImage（通常描画）も保持しておく（GC対策）
        self.jiki = tk.PhotoImage(file=self.jiki_path)
        self.blickblock = tk.PhotoImage(file=self.blickblock_path)
        self.bakdan = tk.PhotoImage(file=self.bakdan_path)
        self.hakeCg = tk.PhotoImage(file=self.hake_path)
        self.hake2Cg = tk.PhotoImage(file=self.hake2_path)
        self.hummarCg = tk.PhotoImage(file=self.hummar_path)
        self.rollCg = tk.PhotoImage(file=self.roll_path)
        self.floorCg = tk.PhotoImage(file=self.floor_path)
        self.floorPaintCg = tk.PhotoImage(file=self.floorPaint_path)
        # Pillowで作った ImageTk を保持するための参照リスト（GC対策）
        self._image_refs = []

    def paint(self, mapdata, cx, cy):
        for x in range(10):
            for y in range(10):
                if mapdata.is_back_kuro(y, x) == True:
                    
                    self.canvas.create_rectangle(50*x+10,50*y+10,50*(x+1),50*(y+1),fill="black",width=10,tag="mass_char_item")
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.floorCg,tag="mass_char_item")
                    pass
                elif mapdata.is_back_orange(y, x) == True:
                    
                    self.canvas.create_rectangle(50*x+10,50*y+10,50*(x+1),50*(y+1),fill="orange",width=10,tag="mass_char_item")
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.floorPaintCg,tag="mass_char_item")
                    pass
                elif mapdata.is_back_renga(y, x) == True:

                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.blickblock,tag="mass_char_item")
                

                #はけ
                if mapdata.get_item(y, x) == 1:
#                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.hakeCg,tag="mass_char_item")
                    self.create_image_with_alpha(50*x,50*y, path=self.hake_path, alpha=150, anchor="nw", tags=("overlay",))
                '''
                if mapdata.get_item(y, x) == 2:
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.hakeCg,tag="mass_char_item")
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="2",tag="mass_char_item")
                '''

                #ローラー
                if mapdata.get_item(y, x) == 3:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="3",tag="mass_char_item")
                '''
                if mapdata.get_item(y, x) == 4:
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.hakeCg,tag="mass_char_item")
                '''

                #ハンマー
                if mapdata.get_item(y, x) == 5:
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.hummarCg,tag="mass_char_item")
                '''
                if mapdata.get_item(y, x) == 6:
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.hakeCg,tag="mass_char_item")
                if mapdata.get_item(y, x) == 7:
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.hakeCg,tag="mass_char_item")
                if mapdata.get_item(y, x) == 8:
                    self.canvas.create_image(50*x+25+5,50*y+25+5,image=self.hakeCg,tag="mass_char_item")
                '''
                
        self.create_image_with_alpha(50*cx, 50*cy, path=self.jiki_path, alpha=150, anchor="nw", tags=("overlay",))
    
    def pack(self):
        self.canvas.pack()

    def delete(self, s):
        self.canvas.delete(s)
    
    def clear(self, men):
        self.canvas.create_text(550,420,text=str(men)+"面クリア！！",tag="clear_tag")

    def item_area_init(self, orange_hake_count,
            kuro_hake_count, orange_roller_count,
            kuro_roller_count, small_hammer_count,
            big_hammer_count, orange_colorball_count,
            kuro_colorball_count):
        '''
        アイテムリスト　→に表示
        '''
        self.n = 30
#       アイテム１はオレンジはけ
        self.canvas.create_image(ITEM_LIST_X1,LIST_ITEM_Y1,image=self.hakeCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(555,50,555+self.n,50+self.n)
        self.canvas.create_text(ITEM_LIST_X1,LIST_TEXT_Y1,text=orange_hake_count,tag="item_count")
#アイテム２は黒はけ
#        self.canvas.create_image(ITEM_LIST_X2,LIST_ITEM_Y1,image=self.hakeCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(655,50,655+self.n,50+self.n)
#        self.canvas.create_text(ITEM_LIST_X2,LIST_TEXT_Y1,text=kuro_hake_count,tag="item_count")
#アイテム３はオレンジローラー
        self.canvas.create_image(ITEM_LIST_X1,LIST_ITEM_Y2,image=self.rollCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(555,150,555+self.n,150+self.n)
        self.canvas.create_text(ITEM_LIST_X1,LIST_TEXT_Y2,text=orange_roller_count,tag="item_count")
#アイテム４は黒ローラー
#        self.canvas.create_image(ITEM_LIST_X2,LIST_ITEM_Y2,image=self.rollCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(655,150,655+self.n,150+self.n)
#        self.canvas.create_text(ITEM_LIST_X2,LIST_TEXT_Y2,text=kuro_roller_count,tag="item_count")
#アイテム５は小さいハンマー
        self.canvas.create_image(ITEM_LIST_X1,LIST_ITEM_Y3,image=self.hummarCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(555,250,555+self.n,250+self.n)
        self.canvas.create_text(ITEM_LIST_X1,LIST_TEXT_Y3,text=small_hammer_count,tag="item_count")
#アイテム６はでかいハンマー
#        self.canvas.create_image(ITEM_LIST_X2,LIST_ITEM_Y3,image=self.hummarCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(655,250,655+self.n,250+self.n)
#        self.canvas.create_text(ITEM_LIST_X2,LIST_TEXT_Y3,text=big_hammer_count,tag="item_count")
#アイテム７はオレンジカラーボール
#        self.canvas.create_image(ITEM_LIST_X1,LIST_ITEM_Y4,image=self.bakdan,tag="list_mass_char_item")
#        self.canvas.create_rectangle(555,350,555+self.n,350+self.n)
#        self.canvas.create_text(ITEM_LIST_X1,LIST_TEXT_Y4,text=orange_colorball_count,tag="item_count")
#アイテム８は黒カラーボール
#        self.canvas.create_image(ITEM_LIST_X2,LIST_ITEM_Y4,image=self.bakdan,tag="list_mass_char_item")
#        self.canvas.create_rectangle(655,350,655+self.n,350+self.n)
#        self.canvas.create_text(ITEM_LIST_X2,LIST_TEXT_Y4,text=kuro_colorball_count,tag="item_count")
    
    def item_count_repaint(self, orange_hake_count,
            kuro_hake_count, orange_roller_count,
            kuro_roller_count, small_hammer_count,
            big_hammer_count, orange_colorball_count,
            kuro_colorball_count):

        self.canvas.delete("item_count")
        self.canvas.create_text(555,95,text=orange_hake_count,tag="item_count")
        self.canvas.create_text(655,95,text=kuro_hake_count,tag="item_count")
        self.canvas.create_text(555,195,text=orange_roller_count,tag="item_count")
        self.canvas.create_text(655,195,text=kuro_roller_count,tag="item_count")
        self.canvas.create_text(555,295,text=small_hammer_count,tag="item_count")
        self.canvas.create_text(655,295,text=big_hammer_count,tag="item_count")
        self.canvas.create_text(555,395,text=orange_colorball_count,tag="item_count")
        self.canvas.create_text(655,395,text=kuro_colorball_count,tag="item_count")

    def create_rectangle(self,x1,y1,x2,y2,outline,width,tag):
        self.canvas.create_rectangle(x1+5,y1+5,x2+5,y2+5,outline=outline,width=width,tags=tag)
    
    def hake(self, c1, c2, c3, c4, hake_switch, cx, cy):
        if hake_switch[0] == 1:
            self.create_rectangle(50*(cx-1),50*cy,50*cx,50*(cy+1),c1,3,"item_waku")
        if hake_switch[1] == 1:
            self.create_rectangle(50*cx,50*(cy-1),50*(cx+1),50*cy,c2,3,"item_waku")
        if hake_switch[2] == 1:
            self.create_rectangle(50*(cx+1),50*cy,50*(cx+2),50*(cy+1),c3,3,"item_waku")
        if hake_switch[3] == 1:
            self.create_rectangle(50*cx,50*(cy+1),50*(cx+1),50*(cy+2),c4,3,"item_waku")
    
    def roll(self, c1, c2, c3, c4, mass_continued_num, cx, cy):
        if mass_continued_num[0] > 0:
            self.create_rectangle(50*(cx-mass_continued_num[0]),50*cy,50*cx,50*(cy+1),c1,5,"item_waku")
        if mass_continued_num[1] > 0:
            self.create_rectangle(50*cx,50*(cy-mass_continued_num[1]),50*(cx+1),50*cy,c2,5,"item_waku")
        if mass_continued_num[2] > 0:
            self.create_rectangle(50*(cx+1),50*cy,50*(cx+mass_continued_num[2]+1),50*(cy+1),c3,5,"item_waku")
        if mass_continued_num[3] > 0:
            self.create_rectangle(50*cx,50*(cy+1),50*(cx+1),50*(cy + mass_continued_num[3]+1),c4,5,"item_waku")

    def load_image_with_alpha(self, path, alpha=200):
        """
        path: 画像ファイルパス（RGBA PNG 推奨）
        alpha: 0(完全透明)~255(不透明) のアルファ値（既存アルファに乗算）
        戻り値: ImageTk.PhotoImage
        """
        img = Image.open(path).convert("RGBA")
        if alpha < 255:
            r, g, b, a = img.split()
            # 既存アルファに乗算して透過度を調整
            a = a.point(lambda p: int(p * (alpha / 255.0)))
            img = Image.merge("RGBA", (r, g, b, a))
        tk_img = ImageTk.PhotoImage(img)
        # GCされないように参照を保持
        if not hasattr(self, "_image_refs"):
            self._image_refs = []
        self._image_refs.append(tk_img)
        return tk_img

    def create_image_with_alpha(self, x, y, path, alpha=200, **create_kwargs):
        """
        Canvas.create_image ラッパー（self.canvas を使用）。
        path はファイルパス（str）を渡してください。
        """
        tk_img = self.load_image_with_alpha(path, alpha)
        # Canvas の create_image を使う（self.create_image は定義されていない）
        return self.canvas.create_image(x + 5, y + 5, image=tk_img, **create_kwargs)
