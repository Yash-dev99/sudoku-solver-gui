
import pygame as pg
import time


#Global Constant
window_Height=700
window_Width=700
Window=pg.display.set_mode((window_Height,window_Width))




#Color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)


def Event_handler():
    """
    This Function Handel all the event thing
    Argument: Null
    return: Null
    """
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            quit()
class sudoku:
    """
    This class will handel everything related to sudoku
    """
    def __init__(self,offset,board=[[0 for i in range(9)] for j in range(9)],size=50,color=Black,active_color=Red):
        self.offset=offset
        self.board=board
        self.size=size
        self.color=color
        self.active_color=active_color

    def display(self):
        """
        Display sudoku on screen
        """
        #Making Lines

        #Putting Numbers
        offset=self.offset
        size=self.size
        board=self.board

        def pos(index):
            return index*size+offset

        for i in range(9):
            for j in range(9):
                text(str(board[i][j]),pos(i),pos(j),Font_size=size).Message_display()
class text:
    """
    making text a object
    """

    def __init__(self,text,text_x,text_y,color=Black,Font='freesansbold.ttf',Font_size=115):
        self.text=text
        self.Font=Font
        self.Font_size=Font_size
        self.color=color
        self.x=text_x
        self.y=text_y


    def Message_display(self):
        """
        Display Text on Window
        contain Default
        Argument: text(str),Font(str),Font_size(int)
        return: Null
        """

        textSurface = pg.font.Font(self.Font,self.Font_size).render(self.text, True,self.color)
        TextSurf, TextRect =textSurface, textSurface.get_rect()
        TextRect.center = (self.x,self.y)
        Window.blit(TextSurf, TextRect)


def mainloop():
    """
    Main loop of this gui
    """
    pg.display.set_caption("SUDOKU SOLVER")
    title=text("Sudoku_Solver",50,20,Font_size=12)
    Sudoku=sudoku(150)
    while True:
        """
        1. Displaying Things
        2. Taking Event
        3. updating
        """
        Window.fill(White)
        title.Message_display()
        Sudoku.display()

        Event_handler()


        pg.display.update()
        pg.time.Clock().tick(60)
if __name__=="__main__":
    pg.init()
    mainloop()

