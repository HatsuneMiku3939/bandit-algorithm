import random

class BernoulliArm(object):
    def __init__(self, probability):
        self.probability = probability

    def draw(self):
        if random.random() > self.probability:
            return 0.0

        return 1.0
