import math
import random

class Softmax(object):
    def __init__(self, temperature, counts, values):
        self.temperature = temperature
        self.counts = counts
        self.values = values

    def initialize(self, n_arms):
        self.counts = [0.0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def _categorical_draw(self, probs):
        z = random.random()
        cum_prob = 0.0
        for i in range(len(probs)):
            prob = probs[i]
            cum_prob += prob
            if cum_prob > z:
                return i

        return len(probs) - 1

    def select_arm(self):
        z = sum([math.exp(v / self.temperature) for v in self.values])
        probs = [math.exp(v / self.temperature) / z for v in self.values]

        return self._categorical_draw(probs)

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1

        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]

        new_value = ((n-1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value

class AnnealingSoftmax(object):
    def __init__(self, counts, values):
        self.counts = counts
        self.values = values

    def initialize(self, n_arms):
        self.counts = [0.0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def _categorical_draw(self, probs):
        z = random.random()
        cum_prob = 0.0
        for i in range(len(probs)):
            prob = probs[i]
            cum_prob += prob
            if cum_prob > z:
                return i

        return len(probs) - 1

    def select_arm(self):
        t = sum(self.counts) + 1
        temperature = 1 / math.log(t + 0.0000001)

        z = sum([math.exp(v / temperature) for v in self.values])
        probs = [math.exp(v / temperature) / z for v in self.values]

        return self._categorical_draw(probs)

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1

        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]

        new_value = ((n-1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
