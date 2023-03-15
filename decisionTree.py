from helper.helperFunctions import *
from helper.helperFunctions import Iris
import math

def entropy():
    events = 3
    p = 1/events # Equal chance a iris could be from all three groups

    entropy = -sum([p * math.log(p, 2) for p in [p, p, p]])
    return entropy





# MAIN PROGRAM
allIrises = parse_irises("data/iris.data")
irises, testIrises = train_test_split(allIrises, 0.2)


