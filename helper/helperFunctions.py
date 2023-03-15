import random
from helper.iris import Iris

# This imports all the irises into an array of iris objects
def parse_irises(fileLoc):
    irises = []
    try:
        with open(fileLoc) as file:
            lines = [line.rstrip() for line in file]

    except:
        print("File not found")
        return []

    for line in lines:
        elements = line.split(",")
        irises.append(Iris(elements[4], elements[0], elements[1], elements[2], elements[3]))

    return irises


#Split the data set into a training set and a test set, test_size needs to be a float for the percentage
def train_test_split(irises, test_size):
    random.shuffle(irises)
    train_size = int(len(irises) * (1 - test_size))
    train = irises[:train_size]
    test = irises[train_size:]

    return train, test
