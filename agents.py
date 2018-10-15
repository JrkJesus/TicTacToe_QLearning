import random
import kernel


class Player:
    def __init__(self):
        self.variety = "Human"

    def available_moves(self, field):
        return [i + 1 for i in range(0, 9) if field[i] == " "]

    def turn(self, field):
        return int(input((
               "It`s {0} turn. Choose position (1-9): ").format(
                kernel.symbol)))

    def new_game(self, symbol):
        pass

    def reward(self, amount, field):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.variety = "RandomPlayer"

    def new_game(self, symbol):
        pass

    def turn(self, field):
        return random.choice(self.available_moves(field))

    def reward(self, amount, field):
        pass


class QPlayer(Player):
    def __init__(self, epsilon=0.9, alpha=0.3, gamma=0.9):
        self.variety = "QPlayer"
        self.q_table = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def new_game(self, symbol):
        self.prev_field = (" ",) * 9
        self.prev_turn = None

    def getQ(self, state, action):
        if self.q_table.get((state, action)) is None:
            self.q_table[(state, action)] = 0.5
        return self.q_table.get((state, action))

    def turn(self, field):
        self.last_field = tuple(field)
        actions = self.available_moves(field)
        if random.random() < self.epsilon:
            self.prev_turn = random.choice(actions)
            return self.prev_turn
        q_values = [self.getQ(self.last_field, a) for a in actions]
        qMax = max(q_values)
        if q_values.count(qMax) > 1:
            best_turns = [action for action in range(len(
                         actions)) if q_values[action] == qMax]
            action = random.choice(best_turns)
        else:
            action = q_values.index(qMax)
        self.prev_turn = actions[action]
        return actions[action]

    def reward(self, amount, field):
        if self.prev_turn:
            self.learn(self.last_field, self.prev_turn, amount, tuple(field))

    def learn(self, state, action, reward, result_state):
        prev_value = self.getQ(state, action)
        new_q = max([self.getQ(result_state,
                               a) for a in self.available_moves(state)])
        self.q_table[(state, action)] = prev_value + self.alpha * (
                                  (reward + self.gamma*new_q) - prev_value)
