class MapData:
    def __init__(self, back, item):
        self.back = back
        self.item = item
    
    def get_item(self, y, x):
        return self.item[y][x]
    
    def is_back_kuro(self, y, x):
        if self.back[y][x] == 0:
            return True
        else:
            return False
    def is_back_orange(self, y, x):
        if self.back[y][x] == 1:
            return True
        else:
            return False
    
    def is_back_renga(self, y, x):
        if self.back[y][x] == 2:
            return True
        else:
            return False
        
    def back_to_orange(self, y, x):
        self.back[y][x] = 1

    def back_to_kuro(self, y, x):
        self.back[y][x] = 0

    def delete_item(self, y, x):
        self.item[y][x] = 0