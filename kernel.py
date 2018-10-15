import random
import os


class Game:
    def __init__(self, playerX, playerO):
        self.field = [" "] * 9
        self.playerX = playerX
        self.playerO = playerO
        self.playerX_turn = random.choice([True, False])
        self.winner = ""

    def display_field(self):
        row = " {} | {} | {}"
        separator = "\n---+---+---\n"
        print(((row + separator) * 2 + row).format(*self.field))

    def isWin(self, symbol):
        for a, b, c in [(0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (2, 4, 6), (0, 4, 8)]:
            if symbol == self.field[a] == self.field[b] == self.field[c]:
                return True
        return False

    def no_space_left(self):
        return not any([" " in self.field])

    def play_game(self):
        global symbol
        self.playerX.new_game("X")
        self.playerO.new_game("O")
        while True:
            if self.playerX_turn:
                player = self.playerX
                symbol = "X"
                other_player = self.playerO
            else:
                player = self.playerO
                symbol = "O"
                other_player = self.playerX
            if player.variety == "Human":
                os.system("cls")
                self.display_field()
            turn_position = player.turn(self.field)
            if self.field[turn_position - 1] != " ":
                player.reward(-100, self.field)
                break
            self.field[turn_position - 1] = symbol
            if self.isWin(symbol):
                self.winner = symbol
                player.reward(1, self.field)
                other_player.reward(-1, self.field)
                break
            if self.no_space_left():
                player.reward(0.5, self.field)
                other_player.reward(0.5, self.field)
                break
            other_player.reward(0, self.field)
            self.playerX_turn = not self.playerX_turn
