import pygame as pg
import time
from gui import text

#Color
White=(255,255,255)
Black=(0,0,0)
Red=(255,0,0)
Blue=(0,0,255)

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
        def pos(index):
            return index*size+offset

        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    string=''
                else:
                    string=str(board[i][j])
                if (i,j)==(self.active_pos_x,self.active_pos_y):
                    text(string,pos(i),pos(j),Font_size=size,color=self.active_color).Message_display()
                else:
                    text(string,pos(i),pos(j),Font_size=size).Message_display()

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

    def solve(self,row,col):
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
