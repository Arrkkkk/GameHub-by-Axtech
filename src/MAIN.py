import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from typing import get_type_hints
import random
import time
from tkinter import messagebox
from tkinter import simpledialog
import PYTHONCSProject
import os
from tkinter import font
from random import randint

#===============================================================================================================

playing=False

#Function for the Bounce Ball Game
def BB():
    def ExttApp():
        rot.destroy()
    global playing
    rot = Toplevel()
    rot.title("Bounce game by Rajit")
    rot.geometry("500x570")
    rot.resizable(0, 0)
    rot.wm_attributes("-topmost", 1)
    canvas = Canvas(rot, width=500, height=500, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
    canvas.pack(padx=10, pady=10)
    Sett  = Label(rot,height=0, width=0, text='Press spacebar to Pause   ',font='Calibri')
    Sett.pack(side="left")
    score = Label(rot,height=0, width=15, text="Score: 00", font="Calibri")
    score.pack(side="left")
    ExitApp = Button(rot,height=0, width=15, text="Quit...", font="Calibri",command=ExttApp)
    ExitApp.pack(side="left")

    rot.update()\

    class Ball:
        def __init__(self, canvas, color, paddle, bricks, score):
            self.bricks = bricks
            self.canvas = canvas
            self.paddle = paddle
            self.score = score
            self.bottom_hit = False
            self.hit = 0
            self.id = canvas.create_oval(10, 10, 25, 25, fill=color, width=1)
            self.canvas.move(self.id, 230, 461)
            start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
            random.shuffle(start)
            self.x = start[0]
            self.y = -start[0]
            self.canvas.move(self.id, self.x, self.y)
            self.canvas_height = canvas.winfo_height()
            self.canvas_width = canvas.winfo_width()

        def brick_hit(self, pos):
            for brick_line in self.bricks:
                for brick in brick_line:
                    brick_pos = self.canvas.coords(brick.id)
                    try:
                        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                                canvas.bell()
                                self.hit += 1
                                self.score.configure(text="Score: " + str(self.hit))
                                self.canvas.delete(brick.id)
                                return True
                    except:
                        continue
            return False
        
            
        def paddle_hit(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                    return True
                return False

        def draw(self):
            self.canvas.move(self.id, self.x, self.y)
            pos = self.canvas.coords(self.id)
            start = [4, 3.8, 3.6, 3.4, 3.2, 3, 2.8, 2.6]
            random.shuffle(start)
            if self.brick_hit(pos):
                self.y = start[0]
            if pos[1] <= 0:
                self.y = start[0]
            if pos[3] >= self.canvas_height:
                self.bottom_hit = True
            if pos[0] <= 0:
                self.x = start[0]
            if pos[2] >= self.canvas_width:
                self.x = -start[0]
            if self.paddle_hit(pos):
                self.y = -start[0]

            
    class Paddle:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
            self.canvas.move(self.id, 200, 485)
            self.x = 0
            self.pausec=0
            self.canvas_width = canvas.winfo_width()
            self.canvas.bind_all("<Left>", self.turn_left)
            self.canvas.bind_all("<Right>", self.turn_right)
            self.canvas.bind_all("<space>", self.pauser)
            

        def draw(self):
            pos = self.canvas.coords(self.id)
            #print(pos)
            if pos[0] + self.x <= 0:
                self.x = 0
            if pos[2] + self.x >= self.canvas_width:
                self.x = 0
            self.canvas.move(self.id, self.x, 0)

        def turn_left(self, event):
            self.x = -3.5

        def turn_right(self, event):
            self.x = 3.5

        def pauser(self,event):
            self.pausec+=1
            if self.pausec==2:
                self.pausec=0
        

    class Bricks:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_oval(5, 5, 25, 25, fill=color, width=2)




    def start_game(event):
        global playing
        if playing is False:
            playing = True
            score.configure(text="Score: 00")
            canvas.delete("all")
            BALL_COLOR = ["red", "yellow", "white"]
            BRICK_COLOR = ["ghostwhite", "dark slate gray", "rosy brown", "light goldenrod yellow", "floral white", "salmon",
                        "light steel blue", "snow", "pale violet red", "orchid", "tan", "MistyRose2",
                        "DodgerBlue4", "wheat2", "RosyBrown2", "bisque3", "DarkSeaGreen1",'old lace','gainsboro','red','blue','violet','turquoise']
            random.shuffle(BALL_COLOR)
            paddle = Paddle(canvas, "blue")
            bricks = []
            for i in range(0, 7):
                b = []
                for j in range(0, 19):
                    random.shuffle(BRICK_COLOR)
                    tmp = Bricks(canvas, BRICK_COLOR[0])
                    b.append(tmp)
                bricks.append(b)

            for i in range(0, 7):
                for j in range(0, 19):
                    canvas.move(bricks[i][j].id, 25 * j, 25 * i)

            ball = Ball(canvas, BALL_COLOR[0], paddle, bricks, score)
            rot.update_idletasks()
            rot.update()

            time.sleep(1)
            while 1:
                if paddle.pausec !=1:
                    try:
                        canvas.delete(m)
                        del m
                    except:
                        pass
                    if not ball.bottom_hit:
                        ball.draw()
                        paddle.draw()
                        rot.update_idletasks()
                        rot.update()
                        time.sleep(0.01)
                        if ball.hit==105:
                            canvas.create_text(250, 250, text="YOU WON !!", fill="yellow", font="Consolas 24 ")
                            rot.update_idletasks()
                            rot.update()
                            playing = False
                            break
                    else:
                        canvas.create_text(250, 250, text="      GAME OVER!\nPress Enter to Restart", fill="red", font="Consolas 24 ")
                        rot.update_idletasks()
                        rot.update()
                        playing = False
                        break
                else:
                    try:
                        if m==None:pass
                    except:
                        m=canvas.create_text(250, 250, text="PAUSED!!", fill="green", font="Consolas 24 ")
                    rot.update_idletasks()
                    rot.update()


    rot.bind_all("<Return>", start_game)
    canvas.create_text(250, 250, text="Press Enter to start Game!!", fill="red", font="Consolas 18")
    j=canvas.find_all()
    rot.mainloop()

#===============================================================================================================

#Function for the tic tac toe game
def tttG():
    class Player():
        def __init__(self,name,marker):
            self.name = name
            self.marker = marker

    class Game:
        p1 = Player('Player','X')
        p2 = Player('Computer','O')
        is_p1_turn = True
        game_over = False

        def __init__(self):
            self.rot = Toplevel()
            self.rot.geometry('318x400')
            self.rot.title('Tic Tac Toe')
            self.rot.maxsize(318,400)
            self.rot.minsize(318,400)
            self.count = 0
            self.welcome_screen()
            self.rot.mainloop()
        
        def welcome_screen(self):
            self.welcome_frame = Frame(self.rot,bg='#DCE0E1')
            self.welcome_frame.pack(fill=BOTH,expand=True)

            Label(self.welcome_frame, text='Select the Game Mode',
                    bg='#DCE0E1', fg='#000000',
                    font=('',20)).pack(padx=10,pady=40)

            Button(self.welcome_frame, text='Player vs Computer',
                    bg='magenta', fg='#000000',
                    command=lambda: self.player_info_screen(1)).pack(padx=30,pady=30)
            
            Button(self.welcome_frame, text='Player vs Player',
                    bg='magenta', fg='#000000',
                    command=lambda: self.player_info_screen(2)).pack(padx=30)
            Button(self.welcome_frame, text='Quit',
                    bg='magenta', fg='#000000',
                    command=lambda: self.rot.destroy()).pack(padx=30,pady=30)    

        def player_info_screen(self,player_number):
            self.welcome_frame.pack_forget()
            self.game_mode = player_number

            self.player_info_frame = Frame(self.rot,bg='#DCE0E1')
            self.player_info_frame.pack(fill=BOTH,expand=True)

            Label(self.player_info_frame,text='Enter the Player Info',
                    bg='#DCE0E1', fg='#000000',
                    font=('',20)).pack(pady=30)
            
            entryList=[]
            for i in range(self.game_mode):
                l = Label(self.player_info_frame, bg='#DCE0E1')
                l.pack(pady=5)

                Label(l,text=f'Player {i+1}',bg='#DCE0E1',fg='#000000',font=('',12)).pack(side=LEFT,padx=20)
                entryList.append(Entry(l,bg='#DCE0E1',fg='#000000'))
                entryList[i].pack(side=LEFT)
                entryList[i].insert(0,f'Player {i+1}')

            Label(self.player_info_frame,text="Press Toss Button To Know Who's Turn is First",
                    bg='#DCE0E1', fg='#000000',
                    font=('',10)).pack(pady=20)

            self.toss_bt = Button(self.player_info_frame,text='Toss',command=lambda: self.toss(entryList))
            self.toss_bt.pack()
        
        def toss(self,lst):
            self.toss_bt['state'] = DISABLED
            if randint(1,100) % 2 == 0:
                self.is_p1_turn = True
            else:
                self.is_p1_turn = False

            if self.game_mode == 2:
                self.p1.name = lst[0].get()
                self.p2.name = lst[1].get()
            else:
                self.p1.name = lst[0].get()
                self.p2.name = 'Computer'
            
            self.toss_frame = Frame(self.player_info_frame,bg='#DCE0E1')
            self.toss_frame.pack(fill=BOTH,expand=True)

            if self.is_p1_turn:
                Label(self.toss_frame,text=f'{self.p1.name} Wins\n Select Your Marker',
                        bg='#DCE0E1', fg='#000000',
                        font=('',10)).pack(pady=10)
                
                l=Label(self.toss_frame,bg='#DCE0E1')
                l.pack()
                Button(l, text='X', command=lambda: self.players_marker('X','O')).pack(side=LEFT,padx=20)
                Button(l, text='O', command=lambda: self.players_marker('O','X')).pack(side=LEFT,padx=20)
            elif self.game_mode == 2:
                Label(self.toss_frame,text=f'{self.p2.name} Wins',
                        bg='#DCE0E1', fg='#000000',
                        font=('',10)).pack(pady=10)
                
                l=Label(self.toss_frame,bg='#DCE0E1')
                l.pack()
                Button(l, text='X', command=lambda: self.players_marker('O','X')).pack(side=LEFT,padx=20)
                Button(l, text='O', command=lambda: self.players_marker('X','O')).pack(side=LEFT,padx=20)
            else:
                Label(self.toss_frame,text=f"{self.p2.name} Wins And Selects the 'O' marker",
                        bg='#DCE0E1', fg='#000000',
                        font=('',10)).pack(pady=15)
                self.is_p1_turn = False
                self.rot.after(1000,self.set_comp_move)
        
        def set_comp_move(self):
            self.play_game()
            self.rot.after(1000,self.computer_move)

        def players_marker(self,marker1,marker2):
            self.p1.marker = marker1
            self.p2.marker = marker2
            self.play_game()

        def play_game(self):
            self.player_info_frame.pack_forget()
            self.game_window()

        def game_window(self):
            self.game_window_frame = Frame(self.rot, bg='#DCE0E1')
            self.game_window_frame.pack(fill=BOTH,expand=True)

            self.l1 = Label(self.game_window_frame,text='',font=('',20),bg='#DCE0E1', fg='#000000')
            self.l1.grid(row=0,column=0,columnspan=3,sticky=E+W,pady=20)

            if self.is_p1_turn:
                self.l1.config(text=self.p1.name + "'s Turns")
            else:
                self.l1.config(text=self.p2.name + "'s Turns")

            b1 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(1))
            b2 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(2))
            b3 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(3))
            b4 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(4))
            b5 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(5))
            b6 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(6))
            b7 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(7))
            b8 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(8))
            b9 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(9))
            
            b1.grid(row=1,column=0)
            b2.grid(row=1,column=1)
            b3.grid(row=1,column=2)
            b4.grid(row=2,column=0)
            b5.grid(row=2,column=1)
            b6.grid(row=2,column=2)
            b7.grid(row=3,column=0)
            b8.grid(row=3,column=1)
            b9.grid(row=3,column=2)

            self.gb_List = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

            Label(self.game_window_frame,text='Tic Tac Toe',font=('',20),
                    bg='#DCE0E1', fg='#000000').grid(row=4,column=0,columnspan=3,pady=10,sticky=EW)
        
        def on_click(self,index):
            if self.game_mode == 1:
                self.player_vs_computer_rule(index)
            else:
                self.player_vs_player_rule(index) 
        
        def player_vs_computer_rule(self,index):
            self.gb_List[index-1]['text'] = self.p1.marker
            self.gb_List[index-1]['state'] = DISABLED
            self.l1.config(text=self.p2.name + "'s Turn")
            self.count += 1
            self.check_result(self.p1)

            if self.count != 9 and not self.game_over:
                self.rot.after(500,self.computer_move)

        def player_vs_player_rule(self,index):
            if self.is_p1_turn:
                self.gb_List[index-1]['text'] = self.p1.marker
                self.gb_List[index-1]['state'] = DISABLED
                self.count += 1
                self.check_result(self.p1)
                self.l1.config(text=self.p2.name + "'s Turn")
                self.is_p1_turn=False
            else:
                self.gb_List[index-1]['text'] = self.p2.marker
                self.gb_List[index-1]['state'] = DISABLED
                self.count += 1
                self.check_result(self.p2)
                self.l1.config(text=self.p1.name + "'s Turn")
                self.is_p1_turn=True


        def computer_move(self):
            run = True
            while run:
                box_num = randint(0,8)
                if self.gb_List[box_num]['state'] == DISABLED:
                    continue
                else:
                    run = False
                    self.count += 1
                    self.gb_List[box_num]['text'] = self.p2.marker
                    self.gb_List[box_num]['state'] = DISABLED
                    self.check_result(self.p2)
                    self.l1.config(text=self.p1.name + "'s Turns")
        
        def check_result(self,player):
            for i in range(3):
                # vertical matching
                if self.gb_List[i*3]['text'] == self.gb_List[i*3+1]['text'] == self.gb_List[i*3+2]['text'] == player.marker:
                    self.gb_List[i*3]['bg']=self.gb_List[i*3+1]['bg']=self.gb_List[i*3+2]['bg'] = 'green'
                    self.rot.after(500,lambda: self.display_massage('Congratulations!!',f'{player.name} wins this Game'))
                    
                # Horizondal matching            
                if self.gb_List[i]['text'] == self.gb_List[i+3]['text'] == self.gb_List[i+6]['text'] == player.marker:
                    self.gb_List[i]['bg']=self.gb_List[i+3]['bg']=self.gb_List[i+6]['bg'] = 'green'
                    self.rot.after(500,lambda: self.display_massage('Congratulation!!',f'{player.name} wins this Game'))
                    
            # Diagonal matching
            if self.gb_List[0]['text'] == self.gb_List[4]['text'] == self.gb_List[8]['text'] == player.marker:
                self.gb_List[0]['bg']=self.gb_List[4]['bg']=self.gb_List[8]['bg'] = 'green'
                self.rot.after(500,lambda: self.display_massage('Congratulation!!',f'{player.name} wins this Game'))
                
            if self.gb_List[2]['text'] == self.gb_List[4]['text'] == self.gb_List[6]['text'] == player.marker:
                self.gb_List[2]['bg']=self.gb_List[4]['bg']=self.gb_List[6]['bg'] = 'green'
                self.rot.after(500,lambda: self.display_massage('Congratulation!!',f'{player.name} wins this Game'))
            
            if self.count == 9 and not self.game_over:
                self.rot.after(500,lambda: self.display_massage('Draw','No one Wins'))
        
        def display_massage(self,massage_header,massage):
            self.game_over = True
            self.game_window_frame.pack_forget()
            
            self.massage_frame = Frame(self.rot, bg='#DCE0E1')
            self.massage_frame.pack(fill=BOTH,expand=True)

            Label(self.massage_frame,text=massage_header+'\n'+massage,
                    bg='#DCE0E1', fg='#000000',
                    font=('',15)).pack(pady=30)
            
            Button(self.massage_frame,text='Rematch',bg='#FFF000', fg='#000000',command=self.rematch).pack(pady=5)
            Button(self.massage_frame,text='Main Menu',bg='#FFF000', fg='#000000',command=self.main_menu).pack(pady=5)
            Button(self.massage_frame,text='Exit',bg='#FFF000', fg='#000000',command=self.rot.destroy).pack(pady=5)
            
        def main_menu(self):
            self.game_over = False
            self.count = 0
            self.massage_frame.pack_forget()
            self.welcome_frame.pack(fill=BOTH,expand=True)
        
        def rematch(self):
            self.game_over = False
            self.count = 0
            self.massage_frame.pack_forget()
            self.toss_bt['state'] = NORMAL
            self.toss_frame.pack_forget()
            self.player_info_frame.pack(fill=BOTH,expand=True)

    if __name__ == "__main__":
        Game()

#===============================================================================================================

#Function for the 2048 game
def opdialog():
    class Game(tk.Tk):
        board = []
        nts = [2,2,2,2,2,2,4]
        score = 0
        highscore = 0
        scorestring = 0
        hss = 0
        
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            self.scorestring = tk.StringVar(self)
            self.scorestring.set("0")
            self.hss = tk.StringVar(self)
            self.hss.set("0")
            self.create_widgets()
            self.canvas = tk.Canvas(self, width=410, height=410, borderwidth=5, highlightthickness=0)
            self.canvas.pack(side="top", fill="both", expand="false")
            self.new_game()
            
        def addNewTile(self):
            index = random.randint(0,6)
            x = -1
            y = -1
            while self.isFull() == False:
                x = random.randint(0,3)
                y = random.randint(0,3)
                if (self.board[x][y] == 0):
                    self.board[x][y] = self.nts[index]
                    x1 = y*105
                    y1 = x*105
                    x2 = x1 + 105 - 5
                    y2 = y1 + 105 - 5
                    num = self.board[x][y]
                    if num == 2:
                        self.square[x,y] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="", width=0)
                        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="#f78a8a", text="2")
                    elif num == 4:
                        self.square[x,y] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#b8dbe5", tags="rect",  outline="", width=0)
                        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="#f78a8a", text="4")
                
                    
                    break
                
        def isFull(self):
            for i in range(0,4):
                for j in range(0,4):
                    if (self.board[i][j] == 0):
                        return False
            return True
            
        def printboard(self):
            cellwidth = 105
            cellheight = 105
            self.square = {}

            for column in range(4):
                for row in range(4):
                    x1 = column*cellwidth
                    y1 = row*cellheight
                    x2 = x1 + cellwidth - 5
                    y2 = y1 + cellheight - 5
                    num = self.board[row][column]
                    if num == 0:
                        self.print0(row, column, x1, y1, x2, y2)
                    elif num == 2:
                        self.print2(row, column, x1, y1, x2, y2)
                    elif num == 4:
                        self.print4(row, column, x1, y1, x2, y2)
                    elif num == 8:
                        self.print8(row, column, x1, y1, x2, y2)
                    elif num == 16:
                        self.print16(row, column, x1, y1, x2, y2)
                    elif num == 32:
                        self.print32(row, column, x1, y1, x2, y2)
                    elif num == 64:
                        self.print64(row, column, x1, y1, x2, y2)
                    elif num == 128:
                        self.print128(row, column, x1, y1, x2, y2)
                    elif num == 256:
                        self.print256(row, column, x1, y1, x2, y2)
                    elif num == 512:
                        self.print512(row, column, x1, y1, x2, y2)
                    elif num == 1024:
                        self.print1024(row, column, x1, y1, x2, y2)
                    elif num == 2048:
                        self.print2048(row, column, x1, y1, x2, y2) 

        def print0(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#f5f5f5", tags="rect", outline="")
        def print2(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="#494949", text="2")
        def print4(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#b8dbe5", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="#494949", text="4")
        def print8(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#71b1bd", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="white", text="8")
        def print16(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#27819f", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="white", text="16")
        def print32(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#0073b9", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="white", text="32")
        def print64(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#7fa8d7", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 36), fill="white", text="64")
        def print128(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#615ea6", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 32), fill="white", text="128")
        def print256(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#2f3490", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 32), fill="white", text="256")
        def print512(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#1c1862", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 32), fill="white", text="512")
        def print1024(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#9c005d", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 30), fill="white", text="1024")
        def print2048(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#c80048", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Calibri", 30), fill="white", text="2048")


        def create_widgets(self):
            self.buttonframe = tk.Frame(self)
            self.buttonframe.grid(row=2, column=0, columnspan=4)
            tk.Button(self.buttonframe, text = "New Game",command=self.new_game).grid(row=0, column=0)
            tk.Button(self.buttonframe, text = "Options..",command=self.exit_).grid(row=0,column=5)
            tk.Label(self.buttonframe, text = "Score:").grid(row=0, column=1)
            tk.Label(self.buttonframe, textvariable=self.scorestring).grid(row=0, column=2)
            tk.Label(self.buttonframe, text = "Record:").grid(row=0, column=3)
            tk.Label(self.buttonframe, textvariable=self.hss).grid(row=0, column=4)        
            self.buttonframe.pack(side="top")



        def keyPressed(self,event):
            shift = 0
            if event.keysym == 'Down':
                for j in range(0,4):
                    shift = 0
                    for i in range(3,-1,-1):
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if i - 1 >= 0 and self.board[i-1][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i-1][j] = 0
                            elif i - 2 >= 0 and self.board[i-1][j] == 0 and self.board[i-2][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i-2][j] = 0
                            elif i == 3 and self.board[2][j] + self.board[1][j] == 0 and self.board[0][j] == self.board[3][j]:
                                self.board[3][j] *= 2
                                self.score += self.board[3][j]
                                self.board[0][j] = 0
                            if shift > 0:
                                self.board[i+shift][j] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            elif event.keysym == 'Right':
                for i in range(0,4):
                    shift = 0
                    for j in range(3,-1,-1):
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if j - 1 >= 0 and self.board[i][j-1] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j-1] = 0
                            elif j - 2 >= 0 and self.board[i][j-1] == 0 and self.board[i][j-2] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j-2] = 0
                            elif j == 3 and self.board[i][2] + self.board[i][1] == 0 and self.board[0][j] == self.board[3][j]:
                                self.board[i][3] *= 2
                                self.score += self.board[i][3]
                                self.board[i][0] = 0
                            if shift > 0:
                                self.board[i][j+shift] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            elif event.keysym == 'Left':
                for i in range(0,4):
                    shift = 0
                    for j in range(0,4):
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if j + 1 < 4 and self.board[i][j+1] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j+1] = 0
                            elif j + 2 < 4 and self.board[i][j+1] == 0 and self.board[i][j+2] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j+2] = 0
                            elif j == 0 and self.board[i][1] + self.board[i][2] == 0 and self.board[i][3] == self.board[i][0]:
                                self.board[i][0] *= 2
                                self.score += self.board[i][0]
                                self.board[i][3] = 0
                            if shift > 0:
                                self.board[i][j-shift] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            elif event.keysym == 'Up':
                for j in range(0,4):
                    shift = 0
                    for i in range(0,4):
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if i + 1 < 4 and self.board[i+1][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i+1][j] = 0
                            elif i + 2 < 4 and self.board[i+1][j] == 0 and self.board[i+2][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i+2][j] = 0
                            elif i == 0 and self.board[1][j] + self.board[2][j] == 0 and self.board[3][j] == self.board[0][j]:
                                self.board[0][j] *= 2
                                self.score += self.board[0][j]
                                self.board[3][j] = 0
                            if shift > 0:
                                self.board[i-shift][j] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            self.scorestring.set(str(self.score))
            if self.score > self.highscore:
                self.highscore = self.score
                self.hss.set(str(self.highscore))
            
            
        def new_game(self):
            self.score = 0
            self.scorestring.set("0")
            self.board = []
            self.board.append([0,0,0,0])
            self.board.append([0,0,0,0])
            self.board.append([0,0,0,0])
            self.board.append([0,0,0,0])
            while True:
                x = random.randint(0,3)
                y = random.randint(0,3)
                if (self.board[x][y] == 0):
                    self.board[x][y] = 2
                    break

            index = random.randint(0,6)
            while self.isFull() == False:
                x = random.randint(0,3)
                y = random.randint(0,3)
                if (self.board[x][y] == 0):
                    self.board[x][y] = self.nts[index]
                    break
            self.printboard()
        
        def exit_(self):
            response=messagebox.askquestion("2048 Game by Rajit Says","Are you sure you wanna exit? You will lose your record",icon='warning')
            print(response)
            if response=='yes':
                tk.Button(self.buttonframe, text = "Exit....",command=self.destroy).grid(row=0, column=6)
                        
        #Returns True if board is full & has no more moves
        def isOver(self):
            for i in range(0,4):
                for j in range(0,4):
                    if (self.board[i][j] == 2048):
                        time.sleep(2)
                        self.youWon()
            for i in range(0,4):
                for j in range(0,4):
                    if (self.board[i][j] == 0):
                        return False
            for i in range(0,4):
                for j in range(0,3):
                    if (self.board[i][j] == self.board[i][j+1]):
                        return False
            for j in range(0,4):
                for i in range(0,3):
                    if self.board[i][j] == self.board[i+1][j]:
                        return False
            gameover = [["G", "A", "M", "E",],["O", "V", "E", "R"], ["", "\U0001F614", "\U0001F614", ""],  ["", "", "", ""]]
            cellwidth = 105
            cellheight = 105
            self.square = {}

            for column in range(4):
                for row in range(4):
                    x1 = column*cellwidth
                    y1 = row*cellheight
                    x2 = x1 + cellwidth - 5
                    y2 = y1 + cellheight - 5
                    self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="")
                    self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Algerian", 50), fill="#494949", text=gameover[row][column])
            time.sleep(0.5)
            return True
        def youWon(self):
            gameover = [["Y", "O", "U", "",],["W", "O", "N", "!"], ["", "", "", ""],  ["", "", "", ""]]
            cellwidth = 105
            cellheight = 105
            self.square = {}
            for column in range(4):
                for row in range(4):
                    x1 = column*cellwidth
                    y1 = row*cellheight
                    x2 = x1 + cellwidth - 5
                    y2 = y1 + cellheight - 5
                    self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e0f2f8", tags="rect", outline="")
                    self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Algerian", 50), fill="#494949", text=gameover[row][column])
            

    if __name__ == "__main__":
        app = Game()
        app.bind_all('<Key>', app.keyPressed)
        app.wm_title("2048 Game by Rajit")
        app.minsize(420,450)
        app.maxsize(420,450)
        app.mainloop()

#===============================================================================================================

def st():
    pas=simpledialog.askstring("Hello","Enter the password to open source code")
    if pas == 'QWERTY#':
        os.system("main.py")
        exit()
    elif pas!='QWERTY#':
        messagebox.showerror("Module Says","Sorry Incorrect Password")
            

#===============================================================================================================

#Function for the game rock paper scissors
coscore=0
score=0
def Rp():
    # main window object
    root = Toplevel()

    def ExitAppRPS():
        root.destroy()

    # Title of GUI window
    root.title('RPS')

    # Size of window
    root.geometry('800x680')

    # Creating canvas
    canvas = Canvas(root, width=800, height=680)
    canvas.grid(row=0, column=0)

    # Creating labels on GUI window
    l1 = Label(root, text='Player', font=('Algerian', 25))
    l2 = Label(root, text='Computer', font=('Algerian', 25))
    l3 = Label(root, text='Vs', font=('Algerian', 40))

    # Placing all the labels on window
    l1.place(x=80, y=20)
    l2.place(x=560, y=20)
    l3.place(x=370, y=230)

    # Default image
    img_p = Image.open("assets/images/default.png")
    img_p = img_p.resize((300, 300))

    # Flipping image from left to right
    img_c = img_p

    # Loading images to put on canvas
    img_p = ImageTk.PhotoImage(img_p)
    img_c = ImageTk.PhotoImage(img_c)

    # Rock image
    rock_p = Image.open('assets/images/rock.jpeg')
    rock_p = rock_p.resize((300, 300))

    # Flipping image from left to right
    rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)

    # Loading images to put on canvas
    rock_p = ImageTk.PhotoImage(rock_p)
    rock_c = ImageTk.PhotoImage(rock_c)

    # Paper image
    paper_p = Image.open('assets/images/paper.jpeg')
    paper_p = paper_p.resize((300, 300))

    # Flipping image from left to right
    paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)

    # Loading images to put on canvas
    paper_p = ImageTk.PhotoImage(paper_p)
    paper_c = ImageTk.PhotoImage(paper_c)

    # Scissor image
    scissor_p = Image.open('assets/images/scissor.jpeg')
    scissor_p = scissor_p.resize((300, 300))

    # Flipping image from left to right
    scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)

    # Loading images to put on canvas
    scissor_p = ImageTk.PhotoImage(scissor_p)
    scissor_c = ImageTk.PhotoImage(scissor_c)

    # Selection image
    img_s = Image.open("assets/images/Selection.jpg")
    img_s = img_s.resize((300, 130))
    img_s = ImageTk.PhotoImage(img_s)

    # Putting image on canvas on specific coordinates
    canvas.create_image(0, 100, anchor=NW, image=img_p)
    canvas.create_image(500, 100, anchor=NW, image=img_c)
    canvas.create_image(0, 400, anchor=NW, image=img_s)
    canvas.create_image(500, 400, anchor=NW, image=img_s)

    coscore=0
    score=0
    # game function
    def game(player):
        canvas.delete('score')
        canvas.delete('coscore')
        global score
        global coscore
        select = [1, 2, 3]
        
        # Randomly selects option for computer
        computer = random.choice(select)

        # Setting image for player on canvas
        if player == 1:
        
            # Puts rock image on canvas
            canvas.create_image(0, 100, anchor=NW, image=rock_p)
        elif player == 2:
            
            # Puts paper image on canvas
            canvas.create_image(0, 100, anchor=NW, image=paper_p)
        else:
            
            # Puts scissor image on canvas
            canvas.create_image(0, 100, anchor=NW, image=scissor_p)

        # Setting image for computer on canvas
        if computer == 1:
            
            # Puts rock image on canvas
            canvas.create_image(500, 100, anchor=NW, image=rock_c)
        elif computer == 2:
            
            # Puts paper image on canvas
            canvas.create_image(500, 100, anchor=NW, image=paper_c)
        else:
            
            # Puts scissor image on canvas
            canvas.create_image(500, 100, anchor=NW, image=scissor_c)

        # Obtaining result by comparison
        if player == computer: # Case of DRAW
            canvas.delete('result')
            res = 'Draw'
            score+=0
            coscore+=0
            
        # Case of player's win
        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
            canvas.delete('result')
            res = 'You won'
            score += 1
            coscore+=0
        
        # Case of computer's win
        else:
            canvas.delete('result')
            res = 'Computer won'
            score += 0
            coscore = coscore + 1

        # Putting result on canvas
        canvas.create_text(200, 640, text='Result:- ' + res,fill="black", font=('Algerian', 25), tag='result')
        canvas.create_text(590, 640, text='Score:- ' + str(score),fill="black", font=('Algerian', 25), tag='score')
        canvas.create_text(590, 600, text='Computer Score:- ' + str(coscore),fill="black", font=('Algerian', 25), tag='coscore')
        
    score=score
    coscore=coscore
    # Function for clear button
    def clear():

        # Removes result from canvas
        canvas.delete('result')
        canvas.delete('score')
        canvas.delete('coscore')
        # Puts default image on canvas
        canvas.create_image(0, 100, anchor=NW, image=img_p)
        canvas.create_image(500, 100, anchor=NW, image=img_c)


    # Button for selecting rock
    rock_b = Button(root, text=' Play Rock', command=lambda: game(1))
    rock_b.place(x=30, y=550)

    # Button for selecting paper
    paper_b = Button(root, text='Play Paper', command=lambda: game(2))
    paper_b.place(x=123, y=550)

    # Button for selecting scissor
    scissor_b = Button(root, text='Play Scissor', command=lambda: game(3))
    scissor_b.place(x=215, y=550)

    # Button for clear
    clear_b = Button(root, text='CLEAR', font=('Times', 10, 'bold'),width=10, command=clear).place(x=370, y=28)
    Qu = Button(root, text='Quit', font=('Times', 10, 'bold'),width=10, command=ExitAppRPS).place(x=370, y=200)

    #sc=Label(root, text=('Score:- ' + str(score)), font=('Algerian', 25))
    #sc.place(x=500,y=600)
    root.mainloop()
score=score
coscore=coscore

#===============================================================================================================

rt = Tk()
rt.title("Axtech Game Console")
rt.geometry("600x670")
rt.resizable(0, 0)
rt.wm_attributes("-topmost", 1)
canvas = Canvas(rt, width=600, height=600, bd=0, highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)
img_p = Image.open("assets/images/Logo.jpg")
img_p = img_p.resize((560, 580))
img_p = ImageTk.PhotoImage(img_p)
canvas.create_image(10, 10, anchor=NW, image=img_p)
Bb  = Button(height=50, width=16, text='Bounce Ball Game',font='Calibri',command=BB)
Bb.pack(side="left")
Rb  = Button(height=50, width=5, text='2048',font='Calibri',command=lambda:opdialog())
Rb.pack(side="left")
Rps = Button(height=50, width=16, text='Rock Paper Scissor',font='Calibri',command=lambda:Rp())
Rps.pack(side="left")
ttt = Button(height=50, width=10, text='Tic Tac Toe',font='Calibri',command=lambda:tttG())
ttt.pack(side="left")
settings = Button(height=50, width=3, text='⋮',command=lambda:st())
settings.pack(side='left')
Ext = Button(height=50, width=7, text='Quit',font='Calibri',command=rt.destroy)
Ext.pack(side="left")
rt.update()

#================================================================================================================
if __name__ == '__main__':
    rt.mainloop()
