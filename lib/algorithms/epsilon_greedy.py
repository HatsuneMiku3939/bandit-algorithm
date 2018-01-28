import random

class EpsilonGreedy(object):
    def __init__(self, epsilon, counts, values):
        self.epsilon = epsilon
        self.counts = counts
        self.values = values

    def initialize(self, n_arms):
        self.counts = [0.0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def _max_index(self, x):
        m = max(x)
        return x.index(m)

    def select_arm(self):
        if random.random() > self.epsilon:
            return _max_index(self.values)

        return random.randrange(len(self.values))

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1

        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]

        new_value = ((n-1) / float(n)) * values + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
