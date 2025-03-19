#Kirpich aka Deros. All rights reserved.
#======================================


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class Square():
    def __init__(self, color:str, border_width:float, filled:bool, side_size_a:float):
        self.color = color
        self.border_width = border_width
        self.filled = filled
        self.side_a = side_size_a
    
    def info(self):
        print(f'Color:{self.color}\nBorder width:{self.border_width}\nFilled:{self.filled}\nSide size a:{self.side_a}\n')
    
    def draw(self):
        fig = plt.figure() 
        ax = fig.add_subplot(111) 
        ax.add_patch( Rectangle((0, 0), self.side_a, self.side_a, fill = self.filled, ec = self.color, lw = self.border_width) ) 
        plt.show()
    
    def __del__(self):
        print('Square has been deleted')

class Quadrilateral(Square):
    def __init__(self, color, border_width, filled, side_size_a, side_size_b, side_size_c, side_size_d):
        super().__init__(color, border_width, filled, side_size_a)
        self.side_a = side_size_a
        self.side_b = side_size_b
        self.side_c = side_size_c
        self.side_d = side_size_b
    
    def info(self):
        super().info()
        print(f'Side b:{self.side_b}\nSide c:{self.side_c}\nSide d:{self.side_d}')
    
    def draw(self):
        fig, ax = plt.subplots()
        xlist = [0, 0, self.side_b, self.side_d, 0]
        ylist = [0, self.side_a, self.side_c, 0, 0]
        ax.plot(xlist, ylist,fill = self.filled color = self.color)
        ax.grid()
        plt.show()


def left():
    fst = Square('red', 12, True, 1)
    fst.info()
    fst.draw()

def right():
    sec = Quadrilateral('green', 12, True, 1, 2, 4, 1)
    sec.draw()
    sec.info()


def main():
    usr_inp = input('1 or 2')
    if usr_inp == '1':
        left()
    elif usr_inp == '2':
        right()

if __name__ == '__main__':
    main()
