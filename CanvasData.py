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
        self.jiki_path = directory + "playerC_A50x50.png"
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
                    # はけ画像：透過対象色=紫、tolerance=10、画像全体は不透明(alpha=255)
                    self.create_image_with_alpha(
                        50*x, 50*y,
                        path=self.hake_path,
                        alpha=255,
                        anchor="nw",
                        tags=("mass_char_item",),
                        transparent_color=(234,63,247),
                        tolerance=10
                    )

                #ローラー
                if mapdata.get_item(y, x) == 3:
                    # ローラー画像：透過対象色=紫、tolerance=10、画像全体は不透明(alpha=255)
                    self.create_image_with_alpha(
                        50*x, 50*y,
                        path=self.roll_path,
                        alpha=255,
                        anchor="nw",
                        tags=("mass_char_item",),
                        transparent_color=(234,63,247),
                        tolerance=10
                    )

                #爆弾
                if mapdata.get_item(y, x) == 5:
                    # 爆弾画像：透過対象色=紫、tolerance=10、画像全体は不透明(alpha=255)
                    self.create_image_with_alpha(
                        50*x, 50*y,
                        path=self.bakdan_path,
                        alpha=255,
                        anchor="nw",
                        tags=("mass_char_item",),
                        transparent_color=(234,63,247),
                        tolerance=10
                    )
                
        # プレイヤー画像の指定色（紫）を透過する（透過対象は完全透過、画像全体は不透明）
        self.create_image_with_alpha(
            50*cx, 50*cy,
            path=self.jiki_path,
            alpha=255,  # 透過度を100%（画像本体は不透明、透過対象色は完全に透過）
            anchor="nw",
            tags=("overlay",),
            transparent_color=(234,63,247),  # 紫
            tolerance=10
        )
    
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
        # アイテム１はオレンジはけ：紫を透過、tolerance=10、画像全体は不透明(alpha=255)
        self.create_image_with_alpha(
            ITEM_LIST_X1, LIST_ITEM_Y1,
            path=self.hake_path,
            alpha=255,
            anchor="center",
            tags=("list_mass_char_item",),
            transparent_color=(234,63,247),
            tolerance=10
        )
        self.create_image_with_alpha(
            ITEM_LIST_X1, LIST_ITEM_Y2,
            path=self.roll_path,
            alpha=255,
            anchor="center",
            tags=("list_mass_char_item",),
            transparent_color=(234,63,247),
            tolerance=10
        )
        self.create_image_with_alpha(
            ITEM_LIST_X1, LIST_ITEM_Y3,
            path=self.bakdan_path,
            alpha=255,
            anchor="center",
            tags=("list_mass_char_item",),
            transparent_color=(234,63,247),
            tolerance=10
        )
#        self.canvas.create_rectangle(555,50,555+self.n,50+self.n)
        self.canvas.create_text(ITEM_LIST_X1,LIST_TEXT_Y1,text=orange_hake_count,tag="item_count")
#アイテム２は黒はけ
#        self.canvas.create_image(ITEM_LIST_X2,LIST_ITEM_Y1,image=self.hakeCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(655,50,655+self.n,50+self.n)
#        self.canvas.create_text(ITEM_LIST_X2,LIST_TEXT_Y1,text=kuro_hake_count,tag="item_count")
#アイテム３はオレンジローラー
#        self.canvas.create_rectangle(555,150,555+self.n,150+self.n)
        self.canvas.create_text(ITEM_LIST_X1,LIST_TEXT_Y2,text=orange_roller_count,tag="item_count")
#アイテム４は黒ローラー
#        self.canvas.create_image(ITEM_LIST_X2,LIST_ITEM_Y2,image=self.rollCg,tag="list_mass_char_item")
#        self.canvas.create_rectangle(655,150,655+self.n,150+self.n)
#        self.canvas.create_text(ITEM_LIST_X2,LIST_TEXT_Y2,text=kuro_roller_count,tag="item_count")
#アイテム５は小さいハンマー
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

    def load_image_with_alpha(self, path, alpha=255):
        """
        path: 画像ファイルパス（RGBA PNG 推奨）
        alpha: 0(完全透明)~255(不透明) のアルファ値（既存アルファに乗算）
        戻り値: ImageTk.PhotoImage
        """
        # 互換性のため引数に透明化カラー/tolerance をサポート（呼び出し側で渡す）
        img = Image.open(path).convert("RGBA")
        # 呼び出し側が透明化をしたい場合は、create_image_with_alpha 側から引数で渡すため
        # ここでは alpha の乗算処理のみ行う（transparent_color 処理は下の分岐で行うことを想定）
        # （下の create_image_with_alpha が透明化を渡すための実装に合わせている）
        # この関数は呼び出し側で transparent_color/tolerance を渡されていればそれらを受け取れるようにしている。
        # ただし既存呼び出しとの互換性を保つため、呼び出し側で透明化処理を行う実装へ変更します。
        # ここでは alpha を適用して戻すのみ。
        if alpha < 255:
            r, g, b, a = img.split()
            a = a.point(lambda p: int(p * (alpha / 255.0)))
            img = Image.merge("RGBA", (r, g, b, a))
        tk_img = ImageTk.PhotoImage(img)
        if not hasattr(self, "_image_refs"):
            self._image_refs = []
        self._image_refs.append(tk_img)
        return tk_img

    def create_image_with_alpha(self, x, y, path, alpha=255, transparent_color=(234,63,247), tolerance=0, **create_kwargs):
        """
        Canvas.create_image のラッパー。
        - path: 画像ファイルパス（RGBA PNG 推奨）
        - alpha: 0~255（既存アルファに乗算）
        - transparent_color: (r,g,b) を渡すとその色に近いピクセルを完全透過にする
        - tolerance: transparent_color との許容差（0 で完全一致）
        """
        img = Image.open(path).convert("RGBA")
        # transparent_color が指定されていれば、その色に近いピクセルを透過（alpha=0）にする
        if transparent_color is not None:
            rt, gt, bt = transparent_color
            datas = img.getdata()
            newData = []
            tol = int(tolerance)
            for item in datas:
                r, g, b, a = item
                if abs(r - rt) <= tol and abs(g - gt) <= tol and abs(b - bt) <= tol:
                    newData.append((r, g, b, 0))
                else:
                    newData.append((r, g, b, a))
            img.putdata(newData)
        # alpha の乗算処理
        if alpha < 255:
            r, g, b, a = img.split()
            a = a.point(lambda p: int(p * (alpha / 255.0)))
            img = Image.merge("RGBA", (r, g, b, a))
        tk_img = ImageTk.PhotoImage(img)
        if not hasattr(self, "_image_refs"):
            self._image_refs = []
        self._image_refs.append(tk_img)
        return self.canvas.create_image(x + 5, y + 5, image=tk_img, **create_kwargs)
