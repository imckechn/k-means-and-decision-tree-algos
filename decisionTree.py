from helper.helperFunctions import *
from helper.helperFunctions import Iris
import math

def entropy():
    events = 3
    p = 1/events # Equal chance a iris could be from all three groups

    entropy = -sum([p * math.log(p, 2) for p in [p, p, p]])
    return entropy

def gini(groups, classes):
    n_instances = float(sum([len(group) for group in groups]))
    # sum weighted Gini index for each group
    giniVal = 0.0
    for group in groups:
        size = float(len(group))
        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [iris.get_type() for iris in group].count(class_val) / size
            score += p * p
            # weight the group score by its relative size
            giniVal += (1.0 - score) * (size / n_instances)
    return giniVal


def split(index, value, irises):
    left, right = list(), list()
    for iris in irises:
        if iris.get_coordinates()[index] < value:
            left.append(iris)
        else:
            right.append(iris)
    return left, right

def to_terminal(group):
    outcomes = [iris.get_type() for iris in group]
    return max(set(outcomes), key=outcomes.count)


def splitOnNode(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    # process left child
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = findSplit(left)
        splitOnNode(node['left'], max_depth, min_size, depth+1)

    # process right child
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = findSplit(right)
        splitOnNode(node['right'], max_depth, min_size, depth+1)


def findSplit(irises):
    class_values = list(set(iris.get_type() for iris in irises))

    b_index, b_value, b_score, b_groups = 999, 999, 999, None

    for index in range(4):
            for iris in irises:
                groups = split(index, iris.get_coordinates()[index], irises)
                giniVal = gini(groups, class_values)

                if giniVal < b_score:
                    b_index, b_value, b_score, b_groups = index, iris.get_coordinates()[index], giniVal, groups
    return {'index':b_index, 'value':b_value, 'groups':b_groups}


# Build a decision tree
def build_tree(train, max_depth, min_size):
    root = findSplit(train)
    splitOnNode(root, max_depth, min_size, 1)
    return root

# Print a decision tree
def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))


# MAIN PROGRAM
allIrises = parse_irises("data/iris.data")
irises, testIrises = train_test_split(allIrises, 0.2)


# Make a prediction with a decision tree
def predict(node, iris):
    if iris.get_coordinates()[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], iris)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], iris)
        else:
            return node['right']

accuracy = 0
while (accuracy < 75):

    tree = build_tree(irises, 5, 1)
    class_values = list(set(iris.get_type() for iris in irises))

    #  predict with a stump
    stump = {'index': 0, 'right': 1, 'value': 6.642287351, 'left': 0}

    correct = 0
    total = 0

    for iris in testIrises:
        prediction = predict(stump, iris)

        if class_values[prediction] == iris.get_type():
            correct += 1
        total += 1

    accuracy = correct/total * 100
    print("Accuracy: ", correct/total * 100)