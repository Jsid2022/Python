import copy
import random

# Took little help from Internet in this one!

class Hat:

    def __init__(self, yellow="", blue="", red="", green="", test=""):
        """Make Instances for class Hat."""
        self.yellow = yellow
        self.blue = blue
        self.red = red
        self.green = green
        self.test = test
        self.contents = []
        if test:
            for i in range(test):
                self.contents.append('test')
        if yellow:
            for i in range(yellow):
                self.contents.append('yellow')
        if red:
            for i in range(red):
                self.contents.append('red')
        if blue:
            for i in range(blue):
                self.contents.append('blue')
        if green:
            for i in range(green):
                self.contents.append('green')

    def draw(self, draw_numbers):
        """Draw balls from hat."""
        draw_list = []
        if draw_numbers > len(self.contents):
            while len(self.contents) != 0:
                random_draw = random.choice(self.contents)
                draw_list.append(random_draw)
                self.contents.remove(random_draw)
        else:
            while len(draw_list) != draw_numbers:
                random_draw = random.choice(self.contents)
                draw_list.append(random_draw)
                self.contents.remove(random_draw)
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Calculate the probability"""
    M = 0
    for exp in range(num_experiments):
        does_match = True
        my_hat = copy.deepcopy(hat)
        balls = my_hat.draw(num_balls_drawn)
        eb_list = []
        for k, v in expected_balls.items():
            eb_list.extend([k] * v) 
        for ball in eb_list:
            if ball in balls:
                balls.remove(ball)
            else: does_match = False
        if does_match == True:
            M += 1

    probab = M / num_experiments
    return probab

# hat = Hat(blue=3,red=2,green=6)
# print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))  # OK.
# # hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# print(hat.draw(2))
# print(hat.contents)
# print(experiment(hat, 33, 3, 33))
# print(hat.contents)
# print(experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100))  # OK.
