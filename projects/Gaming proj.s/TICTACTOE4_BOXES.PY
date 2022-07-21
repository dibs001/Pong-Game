from tkinter import *
import random
def next_turn(row,column):
    global player
    if btn[row][column]['text']=="" and check_winner() is False:
        if player==players[0]:
            btn[row][column]['text']=player
            if (check_winner() is False):
                player=players[1]
                lbl.config(text=players[1]+"'s turn")
            elif (check_winner() is True):
                lbl.config(text=(players[0]+" wins"))
            elif(check_winner()=='Tie'):
                lbl.config(text=("Tie!"))
        else:
            btn[row][column]['text'] = player
            if (check_winner() is False):
                player = players[0]
                lbl.config(text=players[0] + "'s turn")
            elif (check_winner() is True):
                lbl.config(text=(players[1] + " wins"))
            elif (check_winner() == 'Tie'):
                lbl.config(text=("Tie!"))
def check_winner():
    for row in range(4):
        if btn[row][0]['text']==btn[row][1]['text']==btn[row][2]['text']==btn[row][3]['text']!="":
            btn[row][0].config(bg="green")
            btn[row][1].config(bg="green")
            btn[row][2].config(bg="green")
            btn[row][3].config(bg="green")
            return True
    for column in range(4):
        if btn[0][column]['text']==btn[1][column]['text']==btn[2][column]['text']==btn[3][column]['text']!="":
            btn[0][column].config(bg="green")
            btn[1][column].config(bg="green")
            btn[2][column].config(bg="green")
            btn[3][column].config(bg="green")
            return True

    if btn[0][0]['text']==btn[1][1]['text']==btn[2][2]['text']==btn[3][3]['text']!="":
        btn[0][0].config(bg="green")
        btn[1][1].config(bg="green")
        btn[2][2].config(bg="green")
        btn[3][3].config(bg="green")
        return True
    elif btn[0][3]['text']==btn[1][2]['text']==btn[2][1]['text']==btn[3][0]['text']!="":
        btn[0][3].config(bg="green")
        btn[1][2].config(bg="green")
        btn[2][1].config(bg="green")
        btn[3][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(4):
            for column in range(4):
                btn[row][column].config(bg="yellow")
        return "Tie!"
    else:
        return False
def empty_spaces():
    spaces=16
    for row in range(4):
        for column in range(4):
            if btn[row][column]['text']!="":
                spaces-=1
    if spaces==0:
        return False
    else:
        return True

def new_game():
    global player
    player=random.choice(players)
    lbl.config(text=player+"'s turn")
    for row in range(4):
        for column in range(4):
            btn[row][column].config(text="",bg="#F0F0F0")

window=Tk()
window.title("Tic-Tac-Toe")
players=["x","o"]
player=random.choice(players)
btn=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
lbl=Label(text=player+"'s turn",font=('cambria',40))
lbl.grid(row=2,column=8)
reset_btn=Button(text='Restart',font=('cambria',20),command=new_game)
reset_btn.grid(row=5,column=8)
frame=Frame(window)
frame.grid(row=6,column=8)
for row in range(4):
    for column in range(4):
        btn[row][column]=Button(frame,text="",font=('cambria',40),width=5,height=2,
                           command=lambda row=row, column=column:next_turn(row,column))
        btn[row][column].grid(row=row,column=column)
window.geometry('800x800')
window.resizable(False,False)
window.mainloop()