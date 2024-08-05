import random
from colored import fg, attr
class Mastermind:
    COLORS = {"R": fg("red"), "B": fg("blue"), "G": fg("green"), "Y": fg("yellow")}
    ColoresPosiciones = {"correcto": fg("green"), "desubicado": fg("yellow")}
    def __init__(self):
        self.board = [[' ']*4 + [' '] for _ in range(12)]
        self.secret_code = []
    def display_board(self):
        for row in self.board:
            guess = ' '.join([self.COLORS.get(color, '') + 'O' + attr('reset') for color in row[:4]])
            Posicion = ''.join(row[4])
            print(f"{guess} | {Posicion}")
    def update_board(self, turn, guess, Posicion):
        self.board[turn][:4] = guess
        self.board[turn][4] = Posicion

   
