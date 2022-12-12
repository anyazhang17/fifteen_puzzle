# author: Anya Zhang
# date: 11/29/22
# file: game.py implements the fifteen game GUI
# input: clicks from user
# output: game board with GUI buttons

from tkinter import *
import tkinter as tk
import tkinter.font as font
from fifteen import Fifteen
from random import choice

# if clicked and valid move, swap the label and bg color with empty space tile
# i is index of the button clicked
def clickButton(i, buttons, labels):
    # find empty index
    for index in range(len(tiles.tiles)):
        if tiles.tiles[index] == 0:
            empty = index
    # if not a valid move/not adjacent tile, don't swap anything
    value = tiles.tiles[i]
    if tiles.is_valid_move(value):
        tiles.update(value)
    else:
        return
    #print(tiles.tiles)
    # swapping
    labels[i].set('')
    buttons[i].configure(bg='white')
    labels[empty].set(str(value))
    buttons[empty].configure(bg='coral')

# def shuffle(tiles):
    # tiles.shuffle()
    # # empty list of buttons and labels and update the tiles
    # b = []
    # l = []
    # i = 0
    # for row in range(0, 4):
    #     for col in range(0, 4):
    #         value = tiles.tiles[i]
    #         add_button(value, i, row, col, b, l)
    #         i += 1

def shuffle(count, number):
    for index in range(len(tiles.tiles)):
        if tiles.tiles[index] == 0:
            empty = index
    if count < number:
        adj = tiles.adj[empty]
        adj = choice(adj)
        value = tiles.tiles[adj]
        tiles.transpose(0, value)
        labels[adj].set('')
        buttons[adj].configure(bg='white')
        labels[empty].set(str(value))
        buttons[empty].configure(bg='coral')    
        gui.after(100, lambda: shuffle(count+1, number))


def add_button(value, i, row, col, buttons, labels):
    # add button
    text = StringVar()
    text.set(str(value))
    name = value
    button = Button(gui, textvariable=text, name=str(name),
                      bg='coral', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(i, buttons, labels))
    
    # different button for empty space tile
    if value == 0:
        text.set('')
        gui.nametowidget(name).configure(bg='white')
    # add new buttons and labels to list of buttons and labels
    buttons.append(button)
    labels.append(text)
    # add buttons to the window
    button.grid(row=row, column=col)
    
    
    
if __name__ == '__main__':    

    # make tiles
    tiles = Fifteen()
    # make a window
    gui = Tk()
    gui.title("Fifteen")
    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make tile buttons
    buttons = []
    labels = []
    i = 0
    for row in range(0, 4):
        for col in range(0, 4):
            value = tiles.tiles[i]
            add_button(value, i, row, col, buttons, labels)
            i += 1

    # make shuffle button
    shuffle_text = StringVar()
    name = "shuffle"
    shuffle_text.set(name)
    button = Button(gui, textvariable=shuffle_text, name=name,
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : shuffle(0, 100))
    button.grid(row=4, column=1, columnspan = 2, sticky = tk.W+tk.E)
    button.config( height = 1, width = 10 )

    # update the window
    gui.mainloop()