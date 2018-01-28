import random

class BernoulliArm(object):
    def __init__(self, probability):
        self.probability = probability

    def draw(self):
        if random.random() > self.probability:
            return 0.0

        return 1.0


# means = [0.1, 0.1, 0.1, 0.9]
# n_arms = len(means)
# random.shuffle(means)
#
# arms = map(lambda mu: BernoulliArm(mu), means)
