from tkinter import *
from tkinter import messagebox
import random


def newgame():
    global player
    player = random.choice(players)
    to_play.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                to_play.config(text=(players[1] + ' turn'))
            elif check_winner() is True:
                to_play.config(text=(players[0] + ' Won'))
                messagebox.showinfo(title="Game Over", message="X Won")
            elif check_winner() == "Tie":
                to_play.config(text=("Tie!"))
                messagebox.showinfo(title="Game Over", message="Tie")
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                to_play.config(text=(players[0] + ' turn'))
            elif check_winner() is True:
                to_play.config(text=(players[1] + ' Won'))
                messagebox.showinfo(title="Game Over", message="O Won")
            elif check_winner() == "Tie":
                to_play.config(text=("Tie!"))
                messagebox.showinfo(title="Game Over", message="Tie")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#228B22")
            buttons[row][1].config(bg="#228B22")
            buttons[row][2].config(bg="#228B22")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#228B22")
            buttons[1][column].config(bg="#228B22")
            buttons[2][column].config(bg="#228B22")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#228B22")
        buttons[1][1].config(bg="#228B22")
        buttons[2][2].config(bg="#228B22")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#228B22")
        buttons[1][1].config(bg="#228B22")
        buttons[2][0].config(bg="#228B22")
        return True
    elif empty_spaces() is True:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#708090")
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return True
    else:
        return False


players = ['x', 'o']
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]


window = Tk()
to_play = Label(window, text=player + ' turn', font=('consolas,40'))
to_play.pack(side="top")
# window.geometry("600x580")
window.title("Tic Tac Toe")
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)
window.config(background="#F4EAD5")
newgame_button = Button(window, text="New Game", command=newgame)
newgame_button.config(font=('Ink free', 15, 'bold'))
newgame_button.config(bg='#228B22')
newgame_button.config(fg="#FAF9F6")
newgame_button.config(activebackground="#32CD32")
newgame_button.config(activeforeground="#F4EAD5")
newgame_button.pack(side="bottom", pady=30)
frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame, text="", font=('consolas,60'), width=17, height=7,
            command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()
