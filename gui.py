
import pygame as pg
import time


#Global Constant
window_Height=700
window_Width=700
Window=pg.display.set_mode((window_Height,window_Width))

#Color
White=(255,255,255)
Black=(0,0,0)

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



def Message_display(text,text_x,text_y,color=Black,Font='freesansbold.ttf',Font_size=115):
    """
    Display Text on Window
    contain Default
    Argument: text(str),Font(str),Font_size(int)
    return: Null
    """
    textSurface = pg.font.Font(Font,Font_size).render(text, True,color)
    TextSurf, TextRect =textSurface, textSurface.get_rect()
    TextRect.center = (text_x,text_y)
    Window.blit(TextSurf, TextRect)


def mainloop():
    """
    Main loop of this gui
    """
    pg.display.set_caption("SUDOKU SOLVER")
    while True:
        """
        1. Displaying Things
        2. Taking Event
        3. updating
        """
        Window.fill(White)
        Message_display("Sudoku_Solver",50,20,Font_size=12)
        Event_handler()
        pg.display.update()
        pg.time.Clock().tick(60)
if __name__=="__main__":
    pg.init()
    mainloop()

