# author: Anya Zhang
# date: 11/27/22
# file: fifteen.py implements the game Fifteen Puzzles, can be played in terminal
# input: move or optional size
# output: fifteen tiles 

import numpy as np
from random import choice

class Fifteen:

    # create a list of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4): 
        self.tiles = [i for i in range(1,size**2)] + [0]
        self.size = size
        self.adj = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5, 8], [1, 4, 6, 9], [2, 5, 7, 10], [3, 6, 11], [4, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15], [8, 13], [9, 12, 14], [10, 13, 15], [11, 14]]
        #print(self.tiles)
    

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        count = 0
        num = 0
        while count < self.size * 2 + 1:
            if count % 2 == 0:
                print("+---+---+---+---+")
            # print the numbers
            else:
                s = '|'
                for i in self.tiles[num:num+self.size]:
                    if i == 0:
                        s += '   '
                    elif i > 9:
                        s += str(i) + ' '
                    else:
                        s += ' ' + str(i) + ' '
                    s += '|'
                print(s)
                num += self.size
            count += 1


    # return a string representation of the vector of tiles as a 2d array  
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    # 13 14 15  
    def __str__(self): 
        s = ''
        count = 0
        for tile in self.tiles:
            if tile == 0:
                s += '   '
            else:
                # convert int value to string
                t = str(tile)
                if tile > 9:
                    s += t + ' '
                else:
                    s += ' ' + t + ' '
            count += 1
            if count % self.size == 0:
                s += '\n'
        return s


    # exchange i-tile with j-tile  
    # tiles are numbered 1-15, the last tile is 0 (empty space) 
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j): 
        i_index = self.tiles.index(i)
        j_index = self.tiles.index(j)
        self.tiles[i_index] = j
        self.tiles[j_index] = i


    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor 
    def is_valid_move(self, move):  
        # # check if move is next to empty space, same row and next to each other
        # if self.tiles.index(move)//self.size == self.tiles.index(0)//self.size and abs(self.tiles.index(move) - self.tiles.index(0)) == 1:
        #     return True
        # # same col 
        # elif abs(self.tiles.index(move) - self.tiles.index(0)) == 4:
        #     return True
        # return False
        return self.tiles.index(move) in self.adj[self.tiles.index(0)]


    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose 
    # if i of move in self.adj
    def update(self, move): 
        # move_index = self.tiles.index(move)
        # empty_index = self.tiles.index(0)
        # if move_index in self.adj[empty_index]:
        if self.is_valid_move(move):
            self.transpose(0, move)


    # shuffle tiles
    def shuffle(self, moves = 30):
        empty_index = self.tiles.index(0)
        for i in range(moves):
            move_index = choice(self.adj[empty_index])
            self.tiles[empty_index], self.tiles[move_index] = self.tiles[move_index], self.tiles[empty_index]
            empty_index = move_index


    # verify if the puzzle is solved
    def is_solved(self):
        return self.tiles == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass


    # solve the puzzle (optional)
    def solve(self):
        pass
    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    #print(game.draw())
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    #print("everything works")
    
    '''You should be able to play the game if you uncomment the code below'''

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')  