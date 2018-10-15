import csv
import os
import time
from ast import literal_eval
import progressbar
from kernel import Game
from agents import Player, QPlayer


os.system("cls")
if input("Would you like to train AI vs AI? (yes/no): ") == "no":
    p1 = QPlayer()
    p2 = Player()
    p1.epsilon = 0
    with open("q_base.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        mydict = dict(reader)
        mydict = {literal_eval(key): float(value) for key,
                  value in mydict.items()}
    p1.q_table = mydict
    while True:
        game = Game(p1, p2)
        game.play_game()
        os.system("cls")
        game.display_field()
        if game.no_space_left():
            print("It`s draw")
        else:
            print("The winner is {}".format(game.winner))
        if input("One more game?: ") == "yes":
            continue
        else:
            break
else:
    p1 = QPlayer()
    p2 = QPlayer()
    bar = progressbar.ProgressBar(
        maxval=200000, widgets=[progressbar.Bar(
         '■', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    for i in range(200000):
        bar.update(i)
        game = Game(p1, p2)
        game.play_game()
    bar.finish()
    with open("q_base.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(p1.q_table.items())
    print("Training complete, the program will automatically close in 5 sec")
    time.sleep(5)
