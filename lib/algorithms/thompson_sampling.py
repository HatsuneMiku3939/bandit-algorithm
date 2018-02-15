import random

class ThompsonSampling(object):
    def __init__(self, success_counts, fail_counts, values):
        self.success_counts = success_counts
        self.fail_counts = fail_counts
        self.values = values

    def initialize(self, n_arms):
        self.success_counts = [0.0 for col in range(n_arms)]
        self.fail_counts = [0.0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def _max_index(self, x):
        m = max(x)
        return x.index(m)

    def select_arm(self):
        n_arms = len(self.values)
        theta = list(range(n_arms))
        for arm in range(n_arms):
            theta[arm] = random.betavariate(self.success_counts[arm] + 1, self.fail_counts[arm] + 1)

        return self._max_index(theta)

    def update(self, chosen_arm, reward):
        if reward == 1:
            self.success_counts[chosen_arm] += 1
        else:
            self.fail_counts[chosen_arm] += 1

        n = self.success_counts[chosen_arm] + self.fail_counts[chosen_arm]
        value = self.values[chosen_arm]

        new_value = ((n-1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
