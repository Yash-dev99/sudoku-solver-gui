
import pygame as pg
import time
from logic import sudoku,Text,Button

#Global Constant
window_Height=700
window_Width=700
Window=pg.display.set_mode((window_Height,window_Width))
flag=False  #Flag for next in backtracking
sol=None    #going to be a genaretor
Timer_flag=False
Start_time=0

#Color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Blue=(0,0,255)
Orange=(255,69,0)

def Event_handler(Sudoku,solve_button,strike):
    """
    This Function Handel all the event thing
    Argument: Null
    return: Null
    """
    global flag
    global Timer_flag
    global Start_time
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            quit()

        if event.type==pg.KEYDOWN and not flag:
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
                if Sudoku.possible(Sudoku.active_pos_x,Sudoku.active_pos_y,event.key-48):
                    Sudoku.change_val(event.key-48)
                else:
                    strike.strike()
                if not Timer_flag:
                    Timer_flag=True
                    Start_time=time.time()
            if event.key==pg.K_RETURN:
                global sol
                if sol!=None:
                    flag=True
                else:
                    sol=Sudoku.solve()
                    flag=True
        if event.type == pg.MOUSEBUTTONUP:
            outFlag=False
            for i in range(9):
                for j in range(9):
                    if(Sudoku.Cellsbutton[i][j].On_button()):
                        Sudoku.change_active_pos_arrow(i,j)
                        outFlag=True
                        break
                if outFlag:
                    break

            if solve_button.On_button():
                sol=solve_button.active()
                flag=True

def GameOver():
    """
    Function for Game Over
    """
    Text("Game Over",window_Width//2,window_Height//2,Window).Message_display()
    pg.display.update()
    while True:
        for event in pg.event.get():
            if event.type==pg.KEYDOWN:
                if event.type==pg.QUIT:
                    pg.quit()
                    quit()
                if event.key==pg.K_RETURN:
                    mainloop()


class Strikes:
    """
    Display Strikes XX
    """

    def __init__(self):
        self.strikes=0

    def strike(self):
        self.strikes+=1

    def display(self):
        Text("X"*self.strikes,window_Width//2,50,Window,color=Red,Font_size=20).Message_display()

    def check(self):
        if self.strikes>3:
            GameOver()



def Time_format(time):
    """
    Formate Second in H:M:S
    """
    time=int(time)
    seconds=time%60
    time//=60
    minutes=time%60
    time//=60
    houres=time%60
    return "%d:%02d:%02d" %(houres,minutes,seconds)


def mainloop():
    print("start")
    """
    Main loop of this gui
    """
    global flag
    global Timer_flag
    global sol
    global Start_time

    flag=False
    sol=None
    Timer_flag=False
    Start_time=0

    pg.display.set_caption("SUDOKU SOLVER")
    title=Text("Sudoku_Solver",50,20,Window,Font_size=12)
    Sudoku=sudoku(150,Window,active_color=Orange,board=[[0 for i in range(9)]for j in range(9)])
    authour=Text("Made by Yash Kumar Singh",600,650,Window,Font_size=12)
    solve_button=Button("Solve",(20,650),0,20,Sudoku.solve,Window)
    timer=Text("",650,20,Window,Font_size=12)
    strike=Strikes()
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
        strike.display()
        if Timer_flag:
            timer.change_text(Time_format(time.time()-Start_time))
        timer.Message_display()
        strike.check()
        if flag:
            if next(sol):
                flag=False

        Event_handler(Sudoku,solve_button,strike)


        pg.display.update()
        pg.time.Clock().tick(60)

