import random


def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    n_list = []
    for i in range(10):
        n_list.append((random.random()*5 + 30))
    print(n_list)
