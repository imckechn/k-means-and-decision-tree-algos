from helper.helperFunctions import *

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

# Make a prediction with a decision tree
def predict(tree, iris):
    if type(tree) == str:
        return tree

    if iris.get_coordinates()[tree['index']] < tree['value']:
        return predict(tree['left'], iris)
    else:
        return predict(tree['right'], iris)

accuracy = 0
epoch = 0
while accuracy != 100:
    irises, testIrises = train_test_split(allIrises, 0.2)

    tree = build_tree(irises, 4, 1)
    class_values = list(set(iris.get_type() for iris in irises))

    total = 0
    correct = 0
    for iris in testIrises:
        ans = predict(tree, iris)

        if ans == iris.get_type():
            correct += 1
        total += 1

    accuracy = correct/total*100
    epoch += 1

    print("Random iris collection #" + str(epoch) + " Accuracy = " + str(accuracy) + "%")

print("Accuracy = " + str(correct/total*100) + "%")