import pygame as pg
import time

#Color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Blue=(0,0,255)
Orange=(255,69,0)

class Button:
    """
    Button class, Since pygame not have
    """

    def __init__(self,text,pos,Length,Width,function,Window,text_color=Black,color_on_arrow=Orange,color=Red):
        self.color_on_arrow=color_on_arrow
        self.color=color
        self.pos=pos
        self.Length=max(Length,len(text)*Width)
        self.Width=max(Width,10)
        self.function=function
        self.text=Text(text,pos[0]+self.Length//2,pos[1]+self.Width//2,Window,color=text_color,Font_size=self.Width)
        self.Window=Window


    def active(self):
        """
        Activated the button function
        """
        return self.function()

    def display(self):
        """
        Display The Button
        """
        #Code for on button
        pos=self.pos
        if self.On_button():
            color=self.color_on_arrow
        else:
            color=self.color

        #Code for button and text display
        pg.draw.rect(self.Window,color,(pos[0],pos[1],self.Length,self.Width))
        self.text.Message_display()

    def On_button(self):
        """
        Return Bool that arrow is on button or not
        """
        mouse_pos=pg.mouse.get_pos()
        pos=self.pos
        return pos[0]<=mouse_pos[0]<=pos[0]+self.Length  and  pos[1]<=mouse_pos[1]<=pos[1]+self.Width



class Text:
    """
    making text a object
    """

    def __init__(self,text,text_x,text_y,window,color=Black,Font='freesansbold.ttf',Font_size=115):
        self.text=text
        self.Font=Font
        self.Font_size=Font_size
        self.color=color
        self.x=text_x
        self.y=text_y
        self.window=window


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
        self.window.blit(TextSurf, TextRect)


    def change_text(self,text):
        """
        Change the attribute of text
        """
        self.text=text



class sudoku:
    """
    This class will handel everything related to sudoku
    """

    def __init__(self,offset,window,board=[[0 for i in range(9)] for j in range(9)],size=50,color=Black,active_color=Red,active_pos=(0,0)):
        self.offset=offset
        self.board=board
        self.size=size
        self.color=color
        self.active_color=active_color
        self.active_pos_x=active_pos[0]
        self.active_pos_y=active_pos[1]
        self.Window=window
        self.Cellsbutton=[[Button("",(self.pos(i)-self.size//2,self.pos(j)-self.size//2),self.size,self.size,self.change_active_pos_arrow,self.Window) for i in range(9)] for j in range(9)]


    def pos(self,index):
        """
        Position for board's Cell
        """
        return index*self.size+self.offset


    def display(self):
        """
        Display sudoku on screen
        """
        #Making Lines
        offset=self.offset-self.size//2
        for i in range(10):
            if i%3==0:
                color=Red
                border=5
            else:
                color=Blue
                border=1

            pg.draw.line(self.Window,color,(offset+self.size*(i),offset),(self.size*i+offset,offset+self.size*9),border)
            pg.draw.line(self.Window,color,(offset,offset+self.size*(i)),(offset+self.size*9,self.size*i+offset),border)


        #Puts Numbers
        offset=self.offset
        size=self.size
        board=self.board
        #Just a local funtion for positions

        pg.draw.rect(self.Window,self.active_color,((self.active_pos_x+1)*size+offset//2,(self.active_pos_y+1)*size+offset//2,size,size))
        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    string=''
                else:
                    string=str(board[i][j])
                Text(string,self.pos(i),self.pos(j),self.Window,Font_size=size).Message_display()

    def change_active_pos(self,cx,cy):
        """
        Changes position of Active cell
        parameter: change
        return: None
        """
        self.active_pos_x+=cx
        self.active_pos_y+=cy
        self.active_pos_x=max(min(8,self.active_pos_x),0)
        self.active_pos_y=max(min(8,self.active_pos_y),0)

    def change_active_pos_arrow(self,y,x):
        """
        Teleportating active position
        """
        self.active_pos_x=x
        self.active_pos_y=y

    def change_val(self,val):
        """
        Change the value of active cell
        parameter: val
        return: None
        """
        self.board[self.active_pos_x][self.active_pos_y]=val

    def possible(self,x,y,val):
        """
        Check whether it is possible to put that number in board
        parameter: position of cell, value
        return: bool
        """
        if val==0:
            return True
        for i in range(9):
            if self.board[x][i]==val or self.board[i][y]==val:
                return False
        startrow=x-x%3
        startcol=y-y%3
        for i in range(3):
            for j in range(3):
                if self.board[startrow+i][startcol+j]==val:
                    return False
        return True

    def solve(self,row=0,col=0):
        """
        BackTracking algorithm with is a genrator, so we can print every recursion
        parameter: row, col
        return : bool
        """
        if row==9 and col==8:
            yield True
            return
        if row==9:
            row=0
            col+=1
        if(self.board[row][col]>0):
            yield from self.solve(row+1,col)
            return
        for i in range(1,10):
            if (self.possible(row,col,i)):
                self.board[row][col]=i
                if(yield from self.solve(row+1,col)):
                    yield True
                    return
            self.board[row][col]=0
        yield False
        return

    def make_question(self):
        """
        Make new Sudoku Question

        """
        pass
