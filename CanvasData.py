import tkinter as tk


class CanvasData:
    def __init__(self, master):
        self.canvas = tk.Canvas(master,width=700+5,height=500+5,bg="skyblue")
        directory = "./gazou/"
        self.jiki = tk.PhotoImage(file=directory + "character00164x64.jpg")    
    def paint(self, mapdata, cx, cy):
        for x in range(10):
            for y in range(10):
                if mapdata.is_back_kuro(y, x) == True:
                    
                    self.canvas.create_rectangle(50*x+5,50*y+5,50*(x+1)+5,50*(y+1)+5,fill="black",outline="brown",width=10,tag="mass_char_item")
                elif mapdata.is_back_orange(y, x) == True:
                    
                    self.canvas.create_rectangle(50*x+5,50*y+5,50*(x+1)+5,50*(y+1)+5,fill="orange",outline="brown",width=10,tag="mass_char_item")
                elif mapdata.is_back_renga(y, x) == True:
                    self.canvas.create_rectangle(50*x+5,50*y+5,50*(x+1)+5,50*(y+1)+5,fill="brown",outline="brown",width=10,tag="mass_char_item")
                    
                if mapdata.get_item(y, x) == 1:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="1",fill="white", tag="mass_char_item")
                if mapdata.get_item(y, x) == 2:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="2",tag="mass_char_item")
                if mapdata.get_item(y, x) == 3:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="3",tag="mass_char_item")
                if mapdata.get_item(y, x) == 4:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="4",tag="mass_char_item")
                if mapdata.get_item(y, x) == 5:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="5",tag="mass_char_item")
                if mapdata.get_item(y, x) == 6:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="6",tag="mass_char_item")
                if mapdata.get_item(y, x) == 7:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="7",tag="mass_char_item")
                if mapdata.get_item(y, x) == 8:
                    self.canvas.create_text(50*x+25+5,50*y+25+5,text="8",tag="mass_char_item")

        self.canvas.create_image(cx * 50 + 25 + 5, cy * 50 + 25 + 5, image=self.jiki, tag="mass_char_item")
    
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
        self.n = 30
        self.canvas.create_rectangle(555,50,555+self.n,50+self.n)
        self.canvas.create_text(555,95,text=orange_hake_count,tag="item_count")
        self.canvas.create_rectangle(655,50,655+self.n,50+self.n)
        self.canvas.create_text(655,95,text=kuro_hake_count,tag="item_count")
        self.canvas.create_rectangle(555,150,555+self.n,150+self.n)
        self.canvas.create_text(555,195,text=orange_roller_count,tag="item_count")
        self.canvas.create_rectangle(655,150,655+self.n,150+self.n)
        self.canvas.create_text(655,195,text=kuro_roller_count,tag="item_count")
        self.canvas.create_rectangle(555,250,555+self.n,250+self.n)
        self.canvas.create_text(555,295,text=small_hammer_count,tag="item_count")
        self.canvas.create_rectangle(655,250,655+self.n,250+self.n)
        self.canvas.create_text(655,295,text=big_hammer_count,tag="item_count")
        self.canvas.create_rectangle(555,350,555+self.n,350+self.n)
        self.canvas.create_text(555,395,text=orange_colorball_count,tag="item_count")
        self.canvas.create_rectangle(655,350,655+self.n,350+self.n)
        self.canvas.create_text(655,395,text=kuro_colorball_count,tag="item_count")
    
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
