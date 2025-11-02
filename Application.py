import tkinter as tk
from tkinter import messagebox
from CanvasData import CanvasData
from MapData import MapData



class Application(tk.Frame):
    def __init__(self,master):

        super().__init__(master)
        master.title("床を塗りつぶしたら終わりのゲーム")


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
        self.count = 100 - self.mapdata.count_floor()


        print(self.count)
        self.controlball_area =[
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        self.controlball_switch = 0
        self.COLORBALL_AREA_Y = [-3,-2,-2,-2,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,3]
        self.COLORBALL_AREA_X = [0,-1,0,1,-2,-1,0,1,2,-3,-2,-1,0,1,2,3,-2,-1,0,1,2,-1,0,1,0]
        self.colorball_red_x = 0
        self.colorball_red_y = 0
        
        self.cx = 0
        self.cy = 4


        self.men = 1
        self.clear_switch = 0

        self.hake_switch = [0] * 4
        self.mass_continued_num = [0] * 4
        self.imuki = 0

        self.item = 0
        self.mode = 0

        self.orange_hake_count = 0
        self.kuro_hake_count = 0
        self.orange_roller_count = 0
        self.kuro_roller_count = 0
        self.small_hammer_count = 0
        self.big_hammer_count = 0
        self.orange_colorball_count = 0
        self.kuro_colorball_count = 0

        #
        self.canvasdata = CanvasData(master)
        master.bind("<KeyPress>",self.key_event)
        self.canvasdata.pack()
        self.canvasdata.item_area_init(self.orange_hake_count,
            self.kuro_hake_count, self.orange_roller_count,
            self.kuro_roller_count, self.small_hammer_count,
            self.big_hammer_count, self.orange_colorball_count,
            self.kuro_colorball_count)
        self.canvasdata.paint(self.mapdata, self.cx, self.cy)
        
        #面セレクト
        self.OPTIONLIST = [1,2]
        self.ot = tk.StringVar(master)
        self.ot.set("1")
        self.opt = tk.OptionMenu(master,self.ot,*self.OPTIONLIST,command= self.men_select)
        self.opt.place(x=530,y=450)

        self.canvass = tk.Canvas(master,width=700+5,height=50,bg="lightgray")

        self.canvass.pack()
        self.canvass.create_text(100,10,text="操作方法：矢印キーで移動、1～8キーでアイテム選択、Enterキーで使用")



    def repaint(self):
        self.canvasdata.delete("mass_char_item")
        self.canvasdata.paint(self.mapdata, self.cx, self.cy)
    def clear(self):
        print(self.count)
        if self.count == 100:
            self.canvasdata.clear(self.men)
            self.clear_switch = 1
#移動系メゾット
    def key_up(self):
        self.item_init()
        if self.cy > 0:
            if self.mapdata.is_back_kuro(self.cy - 1, self. cx) == True:
                self.cy = self.cy - 1
                self.move_finish()
    def key_down(self):
        self.item_init()
        if self.cy < 9:
            if self.mapdata.is_back_kuro(self.cy + 1, self. cx) == True:
                self.cy = self.cy + 1
                self.move_finish()
    def key_right(self):
        self.item_init()
        if self.cx < 9:
            if self.mapdata.is_back_kuro(self.cy , self. cx + 1) == True:
                self.cx = self.cx + 1
                self.move_finish()   
    def key_left(self):
        self.item_init()
        if self.cx > 0:
            if self.mapdata.is_back_kuro(self.cy , self. cx - 1) == True:
                self.cx = self.cx - 1
                self.move_finish()
    
    def key_a(self):
        if self.mode == 1:
            if self.item == 1 or self.item == 2:
                if self.hake_switch[0] == 1:
                    self.imuki = 1
                    self.canvasdata.delete("item_waku")
                    self.hake("red","yellow","yellow","yellow")
            elif self.item == 3 or self.item == 4:
                if self.mass_continued_num[0] > 0:
                    self.imuki = 1
                    self.canvasdata.delete("item_waku")
                    self.roll("red","yellow","yellow","yellow")
            elif self.item == 7 or self.item == 8:
                if self.colorball_red_x > 0:
                    if self.controlball_area[self.colorball_red_y][self.colorball_red_x-1] == 1:
                        self.colorball_red_x = self.colorball_red_x - 1
                        self.canvasdata.delete("item_waku")
                        for i in range(25):
                            x = self.cx + self.COLORBALL_AREA_X[i]
                            y = self.cy + self.COLORBALL_AREA_Y[i]
                            if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                                self.canvasdata.create_rectangle(50*x,50*y,50*(x+1),50*(y+1),"yellow",5,"item_waku")
                        self.canvasdata.create_rectangle(
                            50*self.colorball_red_x,
                            50*self.colorball_red_y,
                            50*(self.colorball_red_x +1),
                            50*(self.colorball_red_y +1),"red",5,"item_waku"
                        )
    def key_w(self):
        if self.mode == 1:
            if self.item == 1 or self.item == 2:
                if self.hake_switch[1] == 1:
                    self.imuki = 2
                    self.canvasdata.delete("item_waku")
                    self.hake("yellow","red","yellow","yellow")
            elif self.item == 3 or self.item == 4:
                if self.mass_continued_num[1] > 0:
                    self.imuki = 2
                    self.canvasdata.delete("item_waku")
                    self.roll("yellow","red","yellow","yellow")
            elif self.item == 7 or self.item == 8:
                if self.colorball_red_y > 0:
                    if self.controlball_area[self.colorball_red_y-1][self.colorball_red_x] == 1:
                        self.colorball_red_y = self.colorball_red_y - 1
                        self.canvasdata.delete("item_waku")
                        for i in range(25):
                            x = self.cx + self.COLORBALL_AREA_X[i]
                            y = self.cy + self.COLORBALL_AREA_Y[i]
                            if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                                self.canvasdata.create_rectangle(50*x,50*y,50*(x+1),50*(y+1),"yellow",5,"item_waku")
                        self.canvasdata.create_rectangle(
                            50*self.colorball_red_x,
                            50*self.colorball_red_y,
                            50*(self.colorball_red_x +1),
                            50*(self.colorball_red_y +1),"red",5,"item_waku"
                        )
    def key_d(self):
        if self.mode == 1:
            if self.item == 1 or self.item == 2:
                if self.hake_switch[2] == 1:
                    self.imuki = 3
                    self.canvasdata.delete("item_waku")
                    self.hake("yellow","yellow","red","yellow")
            elif self.item == 3 or self.item == 4:
                if self.mass_continued_num[2] > 0:
                    self.imuki = 3
                    self.canvasdata.delete("item_waku")
                    self.roll("yellow","yellow","red","yellow")
            elif self.item == 7 or self.item == 8:
                if self.colorball_red_x < 9:
                    if self.controlball_area[self.colorball_red_y][self.colorball_red_x+1] == 1:
                        self.colorball_red_x = self.colorball_red_x + 1
                        self.canvasdata.delete("item_waku")
                        for i in range(25):
                            x = self.cx + self.COLORBALL_AREA_X[i]
                            y = self.cy + self.COLORBALL_AREA_Y[i]
                            if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                                self.canvasdata.create_rectangle(50*x,50*y,50*(x+1),50*(y+1),"yellow",5,"item_waku")
                        self.canvasdata.create_rectangle(
                            50*self.colorball_red_x,
                            50*self.colorball_red_y,
                            50*(self.colorball_red_x +1),
                            50*(self.colorball_red_y +1),"red",5,"item_waku"
                        )
    def key_s(self):
        if self.mode == 1:
            if self.item == 1 or self.item == 2:
                if self.hake_switch[3] == 1:
                    self.imuki = 4
                    self.canvasdata.delete("item_waku")
                    self.hake("yellow","yellow","yellow","red")

            elif self.item == 3 or self.item == 4:
                if self.mass_continued_num[3] > 0:
                    self.imuki = 4
                    self.canvasdata.delete("item_waku")
                    self.roll("yellow","yellow","yellow","red")
            elif self.item == 7 or self.item == 8:
                
                if self.colorball_red_y < 9:
                    
                    if self.controlball_area[self.colorball_red_y+1][self.colorball_red_x] == 1:
                        
                        self.colorball_red_y = self.colorball_red_y + 1
                        self.canvasdata.delete("item_waku")
                        for i in range(25):
                            x = self.cx + self.COLORBALL_AREA_X[i]
                            y = self.cy + self.COLORBALL_AREA_Y[i]
                            if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                                self.canvasdata.create_rectangle(50*x,50*y,50*(x+1),50*(y+1),"yellow",5,"item_waku")
                        self.canvasdata.create_rectangle(
                            50*self.colorball_red_x,
                            50*self.colorball_red_y,
                            50*(self.colorball_red_x +1),
                            50*(self.colorball_red_y +1),"red",5,"item_waku"
                        )

    def key_1(self):
        '''
        オレンジはけ
        
        '''
        self.item_init()
        if self.orange_hake_count > 0:
            self.mode = 1
            self.item = 1
            self.canvasdata.create_rectangle(520,15,580,75,"brown",3,"item_icon_waku")

            if self.cx > 0:
                if self.mapdata.is_back_kuro(self.cy,self.cx -1) == True:
                    self.hake_switch[0] = 1
            if self.cy > 0:
                if self.mapdata.is_back_kuro(self.cy -1,self.cx) == True:
                    self.hake_switch[1] = 1
            if self.cx < 9:
                if self.mapdata.is_back_kuro(self.cy,self.cx +1) == True:
                    self.hake_switch[2] = 1
            if self.cy < 9:
                if self.mapdata.is_back_kuro(self.cy +1,self.cx) == True:
                    self.hake_switch[3] = 1
            if self.hake_switch[0] == 1:
                self.imuki = 1
                self.hake("red","yellow","yellow","yellow")
            elif self.hake_switch[1] == 1:
                self.imuki = 2
                self.hake("yellow","red","yellow","yellow")
            elif self.hake_switch[2] == 1:
                self.imuki = 3
                self.hake("yellow","yellow","red","yellow")
            elif self.hake_switch[3] == 1:
                self.imuki = 4
                self.hake("yellow","yellow","yellow","red")
    def key_2(self):
        '''
        くろはけ
        '''
        self.item_init()
        if self.kuro_hake_count > 0:
            self.mode = 1
            self.item = 2
            self.canvasdata.create_rectangle(620,15,680,75,"brown",3,"item_icon_waku")
            if self.cx > 0:
                if self.mapdata.is_back_orange(self.cy,self.cx -1) == True:
                    self.hake_switch[0] = 1
            if self.cy > 0:
                if self.mapdata.is_back_orange(self.cy -1,self.cx) == True:
                    self.hake_switch[1] = 1
            if self.cx < 9:
                if self.mapdata.is_back_orange(self.cy,self.cx +1) == True:
                    self.hake_switch[2] = 1
            if self.cy < 9:
                if self.mapdata.is_back_orange(self.cy +1,self.cx) == True:
                    self.hake_switch[3] = 1
            if self.hake_switch[0] == 1:
                self.imuki = 1
                self.hake("red","yellow","yellow","yellow")
            elif self.hake_switch[1] == 1:
                self.imuki = 2
                self.hake("yellow","red","yellow","yellow")
            elif self.hake_switch[2] == 1:
                self.imuki = 3
                self.hake("yellow","yellow","red","yellow")
            elif self.hake_switch[3] == 1:
                self.imuki = 4
                self.hake("yellow","yellow","yellow","red")
    def key_3(self):
        '''
        オレンジローラー
        '''
        self.item_init()
        if self.orange_roller_count > 0:
            self.item = 3
            self.mode = 1
            self.canvasdata.create_rectangle(520,115,580,175,"brown",3,"item_icon_waku")
            #左
            if self.cx > 0:
                if self.mapdata.is_back_kuro(self.cy, self.cx -1) == True:
                    self.mass_continued_num[0] = 1
                    while self.mapdata.is_back_kuro(self.cy, self.cx - self.mass_continued_num[0]) == True:
                        if self.cx - self.mass_continued_num[0] == 0:
                            break
                        if self.cx - self.mass_continued_num[0] -1 >= 0:
                            if self.mapdata.is_back_kuro(self.cy,self.cx -self.mass_continued_num[0] -1) == False:
                                break
                        self.mass_continued_num[0] = self.mass_continued_num[0] + 1
            #上
            if self.cy > 0:
                if self.mapdata.is_back_kuro(self.cy -1, self.cx) == True:
                    self.mass_continued_num[1] = 1
                    while self.mapdata.is_back_kuro(self.cy - self.mass_continued_num[1], self.cx) == True:
                        if self.cy - self.mass_continued_num[1] == 0:
                            break
                        if self.cy - self.mass_continued_num[1] -1 >= 0:
                            if self.mapdata.is_back_kuro(self.cy -self.mass_continued_num[1] -1,self.cx) == False:
                                break
                        self.mass_continued_num[1] = self.mass_continued_num[1] + 1
            #右
            if self.cx < 9:
                if self.mapdata.is_back_kuro(self.cy, self.cx +1) == True:
                    self.mass_continued_num[2] = 1
                    while self.mapdata.is_back_kuro(self.cy, self.cx + self.mass_continued_num[2]) == True:
                        if self.cx + self.mass_continued_num[2] == 9:
                            break
                        if self.cx + self.mass_continued_num[2]+1 <= 9:
                            if self.mapdata.is_back_kuro(self.cy,self.cx +self.mass_continued_num[2]+1) == False:
                                break
                        self.mass_continued_num[2] = self.mass_continued_num[2] + 1
            #下
            if self.cy < 9:
                if self.mapdata.is_back_kuro(self.cy +1, self.cx) == True:
                    self.mass_continued_num[3] = 1
                    while self.mapdata.is_back_kuro(self.cy + self.mass_continued_num[3], self.cx) == True:
                        if self.cy + self.mass_continued_num[3] == 9:
                            break
                        if self.cy + self.mass_continued_num[3] +1 <= 9:
                            if self.mapdata.is_back_kuro(self.cy +self.mass_continued_num[3] +1,self.cx) == False:
                                break
                        self.mass_continued_num[3] = self.mass_continued_num[3] + 1

            if self.mass_continued_num[0] > 0:
                self.imuki = 1
                self.roll("red","yellow","yellow","yellow")
            elif self.mass_continued_num[1] > 0:
                self.imuki = 2
                self.roll("yellow","red","yellow","yellow")
            elif self.mass_continued_num[2] > 0:
                self.imuki = 3
                self.roll("yellow","yellow","red","yellow")
            elif self.mass_continued_num[3] > 0:
                self.imuki = 4
                self.roll("yellow","yellow","yellow","red")
            else:
                self.item_init()
    def key_4(self):
        '''
        くろローラー
        '''
        self.item_init()
        if self.kuro_roller_count > 0:
            self.item = 4
            self.mode = 1
            self.canvasdata.create_rectangle(620,115,680,175,"brown",3,"item_icon_waku")
            #左
            if self.cx > 0:
                if self.mapdata.is_back_orange(self.cy, self.cx -1) == True:
                    self.mass_continued_num[0] = 1
                    while self.mapdata.is_back_orange(self.cy, self.cx - self.mass_continued_num[0]) == True:
                        if self.cx - self.mass_continued_num[0] == 0:
                            break
                        if self.cx - self.mass_continued_num[0] -1 >= 0:
                            if self.mapdata.is_back_orange(self.cy,self.cx -self.mass_continued_num[0] -1) == False:
                                break
                        self.mass_continued_num[0] = self.mass_continued_num[0] + 1
            #上
            if self.cy > 0:
                if self.mapdata.is_back_orange(self.cy -1, self.cx) == True:
                    self.mass_continued_num[1] = 1
                    while self.mapdata.is_back_orange(self.cy - self.mass_continued_num[1], self.cx) == True:
                        if self.cy - self.mass_continued_num[1] == 0:
                            break
                        if self.cy - self.mass_continued_num[1] -1 >= 0:
                            if self.mapdata.is_back_orange(self.cy -self.mass_continued_num[1] -1,self.cx) == False:
                                break
                        self.mass_continued_num[1] = self.mass_continued_num[1] + 1
            #右
            if self.cx < 9:
                if self.mapdata.is_back_orange(self.cy, self.cx +1) == True:
                    self.mass_continued_num[2] = 1
                    while self.mapdata.is_back_orange(self.cy, self.cx + self.mass_continued_num[2]) == True:
                        if self.cx + self.mass_continued_num[2] == 9:
                            break
                        if self.cx + self.mass_continued_num[2]+1 <= 9:
                            if self.mapdata.is_back_orange(self.cy,self.cx +self.mass_continued_num[2]+1) == False:
                                break
                        self.mass_continued_num[2] = self.mass_continued_num[2] + 1
            #下
            if self.cy < 9:
                if self.mapdata.is_back_orange(self.cy +1, self.cx) == True:
                    self.mass_continued_num[3] = 1
                    while self.mapdata.is_back_orange(self.cy + self.mass_continued_num[3], self.cx) == True:
                        if self.cy + self.mass_continued_num[3] == 9:
                            break
                        if self.cy + self.mass_continued_num[3] +1 <= 9:
                            if self.mapdata.is_back_orange(self.cy +self.mass_continued_num[3] +1,self.cx) == False:
                                break
                        self.mass_continued_num[3] = self.mass_continued_num[3] + 1

            if self.mass_continued_num[0] > 0:
                self.imuki = 1
                self.roll("red","yellow","yellow","yellow")
            elif self.mass_continued_num[1] > 0:
                self.imuki = 2
                self.roll("yellow","red","yellow","yellow")
            elif self.mass_continued_num[2] > 0:
                self.imuki = 3
                self.roll("yellow","yellow","red","yellow")
            elif self.mass_continued_num[3] > 0:
                self.imuki = 4
                self.roll("yellow","yellow","yellow","red")
            else:
                self.item_init()
    def key_5(self):
        '''
        小さいハンマー
        '''
        self.item_init()
        if self.small_hammer_count > 0:
            self.item = 5
            self.mode = 1
            self.canvasdata.create_rectangle(520,210,580,275,"brown",3,"item_icon_waku")
            self.hammer()
    def key_6(self):
        '''
        でかいハンマー
        '''
        self.item_init()
        if self.big_hammer_count > 0:
            self.mode = 1
            self.item = 6
            self.canvasdata.create_rectangle(620,215,680,275,"brown",3,"item_icon_waku")
            self.hammer()
            self.hammer2()
    def key_7(self):
        '''
        おれんじカラーボール
        '''
        self.item_init()
        if self.orange_colorball_count > 0:
            self.mode = 1
            self.item = 7
            self.canvasdata.create_rectangle(520,315,580,375,"brown",3,"item_icon_waku")
            self.controlball_switch = 1
            self.colorball_red_x = self.cx
            self.colorball_red_y = self.cy
            for i in range(25):
                x = self.cx + self.COLORBALL_AREA_X[i]
                y = self.cy + self.COLORBALL_AREA_Y[i]
                if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                    self.canvasdata.create_rectangle(50*x,50*y,50*(x+1),50*(y+1),"yellow",5,"item_waku")
                    self.controlball_area[y][x] = 1
            self.canvasdata.create_rectangle(50*self.cx,50*self.cy,50*(self.cx+1),50*(self.cy+1),"red",5,"item_waku")
    def key_8(self):
        '''
        くろカラーボール
        '''


        self.item_init()
        if self.kuro_colorball_count > 0:
            self.item = 8
            self.mode = 1
            self.canvasdata.create_rectangle(620,315,680,375,"brown",3,"item_icon_waku")
            self.controlball_switch = 1
            self.colorball_red_x = self.cx
            self.colorball_red_y = self.cy
            for i in range(25):
                x = self.cx + self.COLORBALL_AREA_X[i]
                y = self.cy + self.COLORBALL_AREA_Y[i]
                if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                    self.canvasdata.create_rectangle(50*x,50*y,50*(x+1),50*(y+1),"yellow",5,"item_waku")
                    self.controlball_area[y][x] = 1
            self.canvasdata.create_rectangle(50*self.cx,50*self.cy,50*(self.cx+1),50*(self.cy+1),"red",5,"item_waku")
    


    def key_return(self):
        if self.mode == 1:
            if self.item == 1:
                if self.imuki == 1:
                    self.orange_hake_sub(self.cy, self.cx -1)
                elif self.imuki == 2:
                    self.orange_hake_sub(self.cy -1, self.cx)
                elif self.imuki == 3:
                    self.orange_hake_sub(self.cy, self.cx +1)
                elif self.imuki == 4:
                    self.orange_hake_sub(self.cy +1, self.cx)
            elif self.item == 2:
                if self.imuki == 1:
                    self.kuro_hake_sub(self.cy, self.cx -1)
                elif self.imuki == 2:
                    self.kuro_hake_sub(self.cy -1, self.cx)
                elif self.imuki == 3:
                    self.kuro_hake_sub(self.cy, self.cx +1)
                elif self.imuki == 4:
                    self.kuro_hake_sub(self.cy +1, self.cx)
            elif self.item == 3:
                if self.imuki == 1:
                    if self.mass_continued_num[0] > 0:
                        for x in range(1,self.mass_continued_num[0] +1):
                            self.orange_roller_sub(self.cy,self.cx-x)
                        self.orange_roller_sub2()

                if self.imuki == 2:
                    if self.mass_continued_num[1] > 0:
                        for x in range(1,self.mass_continued_num[1] +1):
                            self.orange_roller_sub(self.cy-x,self.cx)
                        self.orange_roller_sub2()
                if self.imuki == 3:
                    if self.mass_continued_num[2] > 0:
                        for x in range(1,self.mass_continued_num[2] +1):
                            self.orange_roller_sub(self.cy,self.cx+x)
                        self.orange_roller_sub2()

                if self.imuki == 4:
                    if self.mass_continued_num[3] > 0:
                        for x in range(1,self.mass_continued_num[3] +1):
                            self.orange_roller_sub(self.cy+x,self.cx)
                        self.orange_roller_sub2()

            elif self.item == 4:
                if self.imuki == 1:
                    if self.mass_continued_num[0] > 0:
                        for x in range(1,self.mass_continued_num[0] +1):
                            self.kuro_roller_sub(self.cy,self.cx-x)
                        self.kuro_roller_sub2()

                if self.imuki == 2:
                    if self.mass_continued_num[1] > 0:
                        for x in range(1,self.mass_continued_num[1] +1):
                            self.kuro_roller_sub(self.cy-x,self.cx)
                        self.kuro_roller_sub2()
                if self.imuki == 3:
                    if self.mass_continued_num[2] > 0:
                        for x in range(1,self.mass_continued_num[2] +1):
                            self.kuro_roller_sub(self.cy,self.cx+x)
                        self.kuro_roller_sub2()

                if self.imuki == 4:
                    if self.mass_continued_num[3] > 0:
                        for x in range(1,self.mass_continued_num[3] +1):
                            self.kuro_roller_sub(self.cy+x,self.cx)
                        self.kuro_roller_sub2()

            elif self.item == 5:
                if self.cx - 1 >= 0:
                    self.hammer_sub(self.cy, self.cx -1)
                if self.cy - 1 >= 0:
                    self.hammer_sub(self.cy -1, self.cx)
                if self.cx + 1 <= 9:
                    self.hammer_sub(self.cy, self.cx +1)
                if self.cy + 1 <= 9:
                    self.hammer_sub(self.cy +1, self.cx)

                self.repaint()
                self.clear()
                self.item_init()
                self.small_hammer_count = self.small_hammer_count - 1
                self.item_count_repaint()

            elif self.item == 6:
                if self.cx - 1 >= 0:
                    self.hammer_sub(self.cy, self.cx -1)
                if self.cy - 1 >= 0:
                    self.hammer_sub(self.cy -1, self.cx)
                if self.cx + 1 <= 9:
                    self.hammer_sub(self.cy, self.cx +1)
                if self.cy + 1 <= 9:
                    self.hammer_sub(self.cy +1, self.cx)
                if self.cy - 1 >= 0 and self.cx - 1 >= 0:
                    self.hammer_sub(self.cy -1, self.cx -1)
                if self.cy - 1 >= 0 and self.cx + 1 <= 9:
                    self.hammer_sub(self.cy -1, self.cx +1)
                if self.cy + 1 <= 9 and self.cx + 1 <= 9:
                    self.hammer_sub(self.cy +1, self.cx +1)
                if self.cy + 1 <= 9 and self.cx - 1 >= 0:
                    self.hammer_sub(self.cy +1, self.cx -1)

                self.repaint()
                self.clear()
                self.item_init()
                self.big_hammer_count = self.big_hammer_count - 1
                self.item_count_repaint()
            
            elif self.item == 7:
                if self.mapdata.is_back_kuro(self.colorball_red_y,self.colorball_red_x) == True:
                    self.mapdata.back_to_orange(self.colorball_red_y,self.colorball_red_x)
                    self.repaint()
                    self.count = self.count + 1
                    self.clear()
                    self.item_init()
                    self.orange_colorball_count = self.orange_colorball_count - 1
                    self.item_count_repaint()

            elif self.item == 8:
                if self.mapdata.is_back_orange(self.colorball_red_y,self.colorball_red_x) == True:
                    self.mapdata.back_to_kuro(self.colorball_red_y,self.colorball_red_x)
                    self.repaint()
                    self.count = self.count - 1
                    self.clear()
                    self.item_init()
                    self.kuro_colorball_count = self.kuro_colorball_count - 1
                    self.item_count_repaint()
    
    def key_space(self):
        if self.clear_switch == 0:
            self.item_zero()
            self.item_count_repaint()
            self.item_init()
        elif self.clear_switch == 1:
            self.men = self.men + 1
            self.item_zero()
            self.item_count_repaint()
            self.item_init()
            self.clear_switch = 0
            self.canvasdata.delete("clear_tag")
        self.men_data()

    def key_event(self, e):
        key = e.keysym
        if key == "Up" and self.clear_switch == 0:
            self.key_up()
        elif key == "Down" and self.clear_switch == 0:
            self.key_down()
        elif key == "Right" and self.clear_switch == 0:
            self.key_right()
        elif key == "Left" and self.clear_switch == 0:
            self.key_left()
        elif key == "1" and self.clear_switch == 0:
            self.key_1()
        elif key == "2" and self.clear_switch == 0:
            self.key_2()
        elif key == "3" and self.clear_switch == 0:
            self.key_3()
        elif key == "4" and self.clear_switch == 0:
            self.key_4()
        elif key == "5" and self.clear_switch == 0:
            self.key_5()
        elif key == "6" and self.clear_switch == 0:
            self.key_6()
        elif key == "7" and self.clear_switch == 0:
            self.key_7()
        elif key == "8" and self.clear_switch == 0:
            self.key_8()
        elif key == "a":
            self.key_a()
        elif key == "w":
            self.key_w()
        elif key == "d":
            self.key_d()
        elif key == "s":
            self.key_s()
        elif key == "Return":
            self.key_return()
        elif key == "space":
            self.key_space()
    
    def move_finish(self):
        if self.mapdata.get_item(self.cy, self.cx) == 1:
            self.orange_hake_count += 1
        elif self.mapdata.get_item(self.cy, self.cx) == 2:
            self.kuro_hake_count += 1
        elif self.mapdata.get_item(self.cy, self.cx) == 3:
            self.orange_roller_count += 1
        elif self.mapdata.get_item(self.cy, self.cx) == 4:
            self.kuro_roller_count += 1
        elif self.mapdata.get_item(self.cy, self.cx) == 5:
            self.small_hammer_count += 1
        elif self.mapdata.get_item(self.cy, self.cx) == 6:
            self.big_hammer_count += 1
        elif self.mapdata.get_item(self.cy, self.cx) == 7:
            self.orange_colorball_count += 1
        elif self.mapdata.get_item(self.cy, self.cx) == 8:
            self.kuro_colorball_count += 1

        self.mapdata.back_to_orange(self.cy, self.cx)
        self.mapdata.delete_item(self.cy, self.cx)
        self.count = self.count + 1
        self.repaint()
        self.item_count_repaint()
        self.clear()

    def item_count_repaint(self):
        self.canvasdata.item_count_repaint(self.orange_hake_count,
            self.kuro_hake_count, self.orange_roller_count,
            self.kuro_roller_count, self.small_hammer_count,
            self.big_hammer_count, self.orange_colorball_count,
            self.kuro_colorball_count)

    def men_select(self, wmn):
        self.clear_switch = 0
        self.item_zero()
        self.item_count_repaint()
        self.item_init()
        self.canvasdata.delete("clear_tag")
        self.men = wmn
        self.men_data()

    def men_data(self):
        if self.men == 1:
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
            self.cx = 0
            self.cy = 4
            self.count = 26
            self.ot.set("1")
            self.repaint()
        if self.men == 2:
            self.mapdata = MapData([
                [0,0,0,1,1,1,1,0,0,0],
                [0,1,0,0,1,1,0,0,1,0],
                [0,0,1,0,0,0,0,1,0,0],
                [1,0,0,1,0,0,1,0,0,1],
                [1,1,0,0,0,1,0,0,1,1],
                [1,1,0,0,0,0,0,0,1,1],
                [1,0,0,1,0,0,1,0,0,1],
                [0,0,1,0,0,0,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,0],
                [0,0,0,1,1,1,1,0,0,0]
            ],[
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]
        ])
            self.cx = 5
            self.cy = 4
            self.count = 37
            self.ot.set("2")
            self.repaint()

    def item_zero(self):
        self.orange_hake_count = 0
        self.kuro_hake_count = 0
        self.orange_roller_count = 0
        self.kuro_roller_count = 0
        self.small_hammer_count = 0
        self.big_hammer_count = 0
        self.orange_colorball_count = 0
        self.kuro_colorball_count = 0

    def orange_hake_sub(self, y, x):
        self.mapdata.back_to_orange(y, x)
        self.count = self.count + 1
        self.repaint()
        self.clear()
        self.item_init()
        self.orange_hake_count = self.orange_hake_count - 1
        self.item_count_repaint()
    def kuro_hake_sub(self, y ,x):
        self.mapdata.back_to_kuro(y,x)
        self.count = self.count - 1
        self.repaint()
        self.item_init()
        self.kuro_hake_count = self.kuro_hake_count - 1
        self.item_count_repaint()
    def orange_roller_sub(self, y, x):
        self.mapdata.back_to_orange(y,x)
        self.count = self.count + 1
    def orange_roller_sub2(self):
        self.repaint()
        self.clear()
        self.item_init()
        self.orange_roller_count = self.orange_roller_count - 1
        self.item_count_repaint()
    def kuro_roller_sub(self, y, x):
        self.mapdata.back_to_kuro(y,x)
        self.count = self.count - 1
    def kuro_roller_sub2(self):
        self.repaint()
        self.clear()
        self.item_init()
        self.kuro_roller_count = self.kuro_roller_count - 1
        self.item_count_repaint()
    def hammer_sub(self, y, x):
        if self.mapdata.is_back_kuro( y, x) == True:
            self.mapdata.back_to_orange( y, x)
            self.count = self.count + 1
        elif self.mapdata.is_back_orange( y, x) == True:
            self.mapdata.back_to_kuro( y, x)
            self.count = self.count - 1

    def hake(self, c1, c2, c3, c4):
        self.canvasdata.hake(c1, c2, c3, c4,self.hake_switch,self.cx,self.cy)
    def roll(self, c1, c2, c3, c4):
        self.canvasdata.roll(c1, c2, c3, c4,self.mass_continued_num, self.cx, self.cy)
    def hammer(self):
        if self.cx > 0:
            self.canvasdata.create_rectangle(50*(self.cx-1),50*self.cy,50*self.cx,50*(self.cy+1),"red",3,"item_waku")
        if self.cy > 0:
            self.canvasdata.create_rectangle(50*self.cx,50*(self.cy-1),50*(self.cx+1),50*self.cy,"red",3,"item_waku")
        if self.cx < 9:
            self.canvasdata.create_rectangle(50*(self.cx+1),50*self.cy,50*(self.cx+2),50*(self.cy+1),"red",3,"item_waku")
        if self.cy < 9:
            self.canvasdata.create_rectangle(50*self.cx,50*(self.cy+1),50*(self.cx+1),50*(self.cy+2),"red",3,"item_waku")
    def hammer2(self):
        if self.cx > 0 and self.cy > 0:
            self.canvasdata.create_rectangle(50*(self.cx-1),50*(self.cy-1),50*self.cx,50*self.cy,"red",3,"item_waku")
        if self.cx < 9 and self.cy > 0:
            self.canvasdata.create_rectangle(50*(self.cx+1),50*(self.cy-1),50*(self.cx+2),50*self.cy,"red",3,"item_waku")
        if self.cx < 9 and self.cy < 9:
            self.canvasdata.create_rectangle(50*(self.cx+1),50*(self.cy+1),50*(self.cx+2),50*(self.cy+2),"red",3,"item_waku")
        if self.cx > 0 and self.cy < 9:
            self.canvasdata.create_rectangle(50*(self.cx-1),50*(self.cy+1),50*self.cx,50*(self.cy+2),"red",3,"item_waku")



    #アイテム周りの変数を初期化する関数
    def item_init(self):
        self.canvasdata.delete("item_waku")
        self.canvasdata.delete("item_icon_waku")
        self.mode = 0
        self.imuki = 0
        self.item = 0
        self.hake_switch = [0] *4
        self.mass_continued_num = [0] *4
        if self.controlball_switch == 1:
            self.controlball_area = [[0]*10 for j in range(10)]
            self.controlball_switch = 0
            print(self.controlball_area)

root = tk.Tk()
app = Application(master=root)
app.mainloop()