import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import progressbar
from kernel import Game
from agents import RandomPlayer, QPlayer


p1 = QPlayer()
p2 = RandomPlayer()
bar = progressbar.ProgressBar(
    maxval=200000, widgets=[progressbar.Bar(
     '■', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
win_count_q = 0
win_count_r = 0
y_axis_q = []
y_axis_r = []
x_axis = []
for i in range(1, 40000):
    bar.update(i)
    game = Game(p1, p2)
    game.play_game()
    if game.winner == "X":
        win_count_q += 1
    if game.winner == "O":
        win_count_r += 1
    x_axis.append(i)
    y_axis_q.append(win_count_q / i * 100)
    y_axis_r.append(win_count_r / i * 100)
bar.finish()
p1.epsilon = 0
for i in range(40000, 65000):
    game = Game(p1, p2)
    game.play_game()
    if game.winner == "X":
        win_count_q += 1
    if game.winner == "O":
        win_count_r += 1
    x_axis.append(i)
    y_axis_q.append(win_count_q / i * 100)
    y_axis_r.append(win_count_r / i * 100)
dpi = 100
fig = plt.figure(dpi=dpi, figsize=(1920/dpi, 1080/dpi))
mpl.rcParams.update({'font.size': 14})
plt.axis([1, 65000, 0, 100])
plt.title("Winrate. After 40k games epsilon = 0")
plt.xlabel("Games")
plt.ylabel("Winrate, %")
ax = plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(10000))
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
plt.plot(x_axis, y_axis_q, color="blue", linestyle="solid", label="Q AI")
plt.plot(x_axis, y_axis_r, color="red", linestyle="dashed", label="Random AI")
plt.legend(loc="upper right")
fig.savefig("winrate.png")
