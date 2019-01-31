"""
Problem 205: Dice Game
https://projecteuler.net/problem=205

Solution: We need to calculate P(peter > colin) where peter and colin
are discrete random variables:

peter ~ Unif(1,4)^9
colin ~ Unif(1,6)^6

In order to calculate this without using any distribution packages,
we can calculate the probability for each total outcome event (1 to 36)
for peter and colin.

Next, for each outcome x of peter, the chances of peter winning are
the probability of peter getting outcome x times the sum of colins
probabilities of all outcomes smaller than x. Then we're done!
"""
from collections import defaultdict
from itertools import product
import numpy as np


def dice_game():
    # Calculate the probability distribution of Peter
    peter = np.zeros(37)
    for p in product(range(1, 5), repeat=9):
        peter[sum(p)] += 1
    peter *= (1/4)**9

    # Calculate the probability distribution of Colin
    colin = np.zeros(37)
    for c in product(range(1, 7), repeat=6):
        colin[sum(c)] += 1
    colin *= (1/6)**6

    # Finally we can calculate the
    prob = 0
    for x in range(37):
        prob += peter[x] * sum(colin[:x])
    return(prob)


if __name__ == "__main__":
    print('{0:.7f}'.format(dice_game()))
