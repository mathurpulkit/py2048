# library imports here
import random  # for random placing of 2
import copy  # for deepcopy
import keyboard  # for key capture without echoing it on screen
import time  # for sleeping the thread so that key captures aren't too fast,
# it's a problem with keyboard library
import os  # for clear screen
import argparse  # for command line argument processing
import math

# global constants start here
upkey = ['W', 'w', 'up']  # up is for up arrow key, tested and works in windows
downkey = ['S', 's', 'down']
leftkey = ['A', 'a', 'left']
rightkey = ['D', 'd', 'right']


class Gameboard:  # class Gameboard
    validkey = upkey + downkey + leftkey + rightkey  # valid keypresses on keyboard

    def __init__(self, size, win):  # initialises the class
        self.gameboard = [[0 for i in range(size)] for j in range(size)]  # faster way of declaring
        # and initialising a matrix
        self.score = 0  # keeps game score
        self.size = size  # stores size of board
        self.win = win  # the winning number
        random.seed()  # getting one random 2 on the board
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        random.seed()
        self.gameboard[x][y] = 2
        return

    def clrscr(self):  # used for clearing the screen after every move
        if os.name == "posix":
            # Unix/Linux/MacOS/BSD/etc
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            os.system('CLS')

    def printboard(self):  # prints the gameboard
        for x in self.gameboard:
            for y in x:
                print(y, end="    ")
            print("\n")
        return

    def gmove(self, move):  # return 0 for no process move, 1 for move processed, 2 for lose, 3 for win
        if move in self.validkey:
            # move is processed and a random 2 is placed on the board
            bcopy = copy.deepcopy(self.gameboard)
            iswin = self.sweep(move)
            if iswin == 1:
                return 3
            if bcopy != self.gameboard:
                while True:
                    random.seed()
                    x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
                    if self.gameboard[x][y] == 0:
                        self.gameboard[x][y] = 2
                        break
            else:
                return 0
            if self.islose() != 0:  # if lost, returns 2 for indicating loss
                return 2
        else:
            return 0
        return 1

    def sweep(self, dir):
        """used for the actual move processing, i.e sweep effect in the game"""
        iswin = 0  # checks if player has won
        if dir in upkey:
            for x in range(self.size):
                y = []
                for z in range(self.size):  # strips all zeroes
                    if self.gameboard[z][x] != 0:
                        y.append(self.gameboard[z][x])
                for z in range(len(y) - 1):  # joins any possible tiles
                    if y[z] == y[z + 1]:
                        y[z] = 2 * y[z]
                        y[z + 1] = 0
                        self.score += y[z]
                        if y[z] == self.win:
                            iswin = 1
                try:  # it removes zeros again from the array after joining
                    for i in range(self.size // 2):
                        y.remove(0)
                except:
                    pass
                for i in range(len(y), self.size):  # appends zeroes at end depending on size
                    y.append(0)
                for z in range(self.size):
                    self.gameboard[z][x] = y[z]
            return iswin
        elif dir in leftkey:  # logic used is largely similar to W
            rownum = 0  # used as iterator in for loop
            for x in self.gameboard:
                y = []
                for z in range(self.size):
                    if x[z] != 0:
                        y.append(x[z])
                for z in range(len(y) - 1):
                    if y[z] == y[z + 1]:
                        y[z] = 2 * y[z]
                        y[z + 1] = 0
                        self.score += y[z]
                        if y[z] == self.win:
                            iswin = 1
                try:  # it removes zeros from the array
                    for i in range(self.size // 2):
                        y.remove(0)
                except:
                    pass
                for i in range(len(y), self.size):
                    y.append(0)
                self.gameboard[rownum] = y
                rownum += 1
            return iswin
        elif dir in downkey:  # logic used largely similar to W
            for x in range(self.size):
                y = []
                for z in range(self.size):
                    if self.gameboard[z][x] != 0:
                        y.append(self.gameboard[z][x])
                for z in range(len(y) - 1, 0, -1):
                    if y[z] == y[z - 1]:
                        y[z] = 2 * y[z]
                        y[z - 1] = 0
                        self.score += y[z]
                        if y[z] == self.win:
                            iswin = 1
                try:  # it removes zeros from the array
                    for i in range(self.size // 2):
                        y.remove(0)
                except:
                    pass
                for i in range(self.size - len(y)):
                    self.gameboard[i][x] = 0
                for z in range(self.size - len(y), self.size):
                    self.gameboard[z][x] = y[z - self.size + len(y)]
            return iswin
        elif dir in rightkey:  # logic used largely similar to W
            rownum = 0  # used as iterator in for loop
            for x in range(self.size - 1, -1, -1):
                x = self.gameboard[rownum]
                y = []
                for z in range(self.size):
                    if x[z] != 0:
                        y.append(x[z])
                for z in range(len(y) - 1, 0, -1):
                    if y[z] == y[z - 1]:
                        y[z] = 2 * y[z]
                        y[z - 1] = 0
                        self.score += y[z]
                        if y[z] == self.win:
                            iswin = 1
                try:  # it removes zeros from the array
                    for i in range(self.size // 2):
                        y.remove(0)
                except:
                    pass
                z = []
                for i in range(len(y), self.size):
                    z.append(0)
                self.gameboard[rownum] = z + y
                rownum += 1
            return iswin
        return iswin

    def islose(self):  # checks if player has lost
        for x in self.gameboard:  # if any block is empty, it returns zero as player hasn't lost
            if 0 in x:
                return 0
        for x in self.gameboard:  # does a horizontal check
            temp = 0
            for y in x:  # goes to each element and checks if it is adjacent to the same tile
                if temp == y:  # which means a move is possible
                    return 0
                else:
                    temp = y
        l = self.size - 1
        while l >= 0:  # does a vertical check
            temp = 0
            for x in range(self.size):
                if temp == self.gameboard[x][l]:
                    return 0
                else:
                    temp = self.gameboard[x][l]
            l = l - 1
        return 1
    # player lost check ends here


# class Gameboard ends here


def main(size, win):
    gboard = Gameboard(size, win)  # object gboard is the game board
    gboard.clrscr()
    gboard.printboard()
    if gboard.size == 1:  # edge case for board size of 1*1
        if gboard.win == 2:
            print("You Win")
            print("Your Score is: ", gboard.score)
            exit(0)
        else:
            print("You Lose")
            print("Your Score is: ", gboard.score)
            exit(0)
    while True:
        curmove = keyboard.read_key()  # it reads the key but doesn't display it on screen
        ans = gboard.gmove(curmove)
        gboard.clrscr()
        gboard.printboard()
        if ans == 2:
            print("You Lose")
            print("Your Score is: ", gboard.score)
            exit(0)
        elif ans == 3:
            print("You Win")
            print("Your Score is: ", gboard.score)
            exit(0)
        elif ans == 0:
            print("Invalid Move")
        time.sleep(0.25)  # sleeps the thread so that too many keypresses aren't captured easily


def parser():  # argument parser takes command line inputs
    my_parser = argparse.ArgumentParser(description='Gets board size and win condition')
    my_parser.add_argument('--n', type=int, help='Size of board', default=5)
    my_parser.add_argument('--w', type=int, help='Winning number', default=2048)
    progargs = my_parser.parse_args()
    return progargs


progargs = parser() # gets the argument values
main(progargs.n, pow(2, round(math.log2(progargs.w))))
