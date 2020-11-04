
import pygame as pg
import time
from logic import *

#Global Constant
window_Height=700
window_Width=700
Window=pg.display.set_mode((window_Height,window_Width))
flag=False  #Flag for next in backtracking
sol=None    #going to be a genaretor


#Color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Blue=(0,0,255)
Orange=(255,69,0)

def Event_handler(Sudoku,solve_button):
    """
    This Function Handel all the event thing
    Argument: Null
    return: Null
    """
    global flag
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            quit()

        if event.type==pg.KEYDOWN:
            # Arrow key handler
            if event.key==pg.K_DOWN:
                Sudoku.change_active_pos(0,1)
            elif event.key==pg.K_UP:
                Sudoku.change_active_pos(0,-1)
            elif event.key==pg.K_LEFT:
                Sudoku.change_active_pos(-1,0)
            elif event.key==pg.K_RIGHT:
                Sudoku.change_active_pos(1,0)
            # Changing val
            if 48<=event.key<=58:
                Sudoku.change_val(event.key-48)
            if event.key==pg.K_RETURN:
                global sol
                if sol!=None:
                    flag=True
                else:
                    sol=Sudoku.solve(0,0)
                    flag=True
        if event.type == pg.MOUSEBUTTONUP:
            if solve_button.On_button():
                solve_button.active()

class Text:
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

class Button:
    """
    Button class, Since pygame not have
    """
    def __init__(self,text,pos,Length,Width,function,text_color=Black,color_on_arrow=Orange,color=Red):
        self.color_on_arrow=color_on_arrow
        self.color=color
        self.pos=pos
        self.Length=max(Length,len(text)*Width)
        self.Width=max(Width,10)
        self.function=function
        self.text=Text(text,pos[0]+self.Length//2,pos[1]+self.Width//2,color=text_color,Font_size=self.Width)

    def active(self):
        global sol
        global flag
        flag=True
        sol=self.function(0,0)

    def display(self):
        pos=self.pos
        if self.On_button():
            color=self.color_on_arrow
        else:
            color=self.color
        pg.draw.rect(Window,color,(pos[0],pos[1],self.Length,self.Width))
        self.text.Message_display()
    def On_button(self):
        mouse_pos=pg.mouse.get_pos()
        pos=self.pos
        return pos[0]<=mouse_pos[0]<=pos[0]+self.Length  and  pos[1]<=mouse_pos[1]<=pos[1]+self.Width





def mainloop():
    """
    Main loop of this gui
    """
    pg.display.set_caption("SUDOKU SOLVER")
    title=Text("Sudoku_Solver",50,20,Font_size=12)
    Sudoku=sudoku(150,Window,active_color=Orange)
    authour=Text("Made by Yash Kumar Singh",600,650,Font_size=12)
    solve_button=Button("Solve",(20,650),0,20,Sudoku.solve)
    global flag
    global sol
    while True:
        """
        1. Displaying Things
        2. Taking Event
        3. updating
        """
        Window.fill(White)
        title.Message_display()
        authour.Message_display()
        Sudoku.display()
        solve_button.display()
        if flag:
            if next(sol):
                flag=False

        Event_handler(Sudoku,solve_button)


        pg.display.update()
        pg.time.Clock().tick(60)
if __name__=="__main__":
    pg.init()
    mainloop()

