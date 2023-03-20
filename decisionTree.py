from helper.helperFunctions import *

MAXDEPTH = 4

# Gets the labels from a list of irises
def get_labels(irises):
    labels = []
    for iris in irises:
        if iris.get_type() not in labels:
            labels.append(iris.get_type())

    return labels

# This evaluates the split of the data set
def gini(groups, labels):
    n_instances = float(sum([len(group) for group in groups]))
    giniVal = 0.0

    #two groups, a left and right group
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue

        score = 0.0
        # Get all the labels in the group
        types = []
        for iris in group:
            types.append(iris.get_type())

        #Get the score for each label and add it to the gini value
        for label in labels:
            p = types.count(label) / size
            score += p * p

            giniVal += (1.0 - score) * (size / n_instances)
    return giniVal


#This splits the irises on a value. If an iris value (the index = the iris attribute) is less than the value, it goes to the left group, otherwise it goes to the right group
def split(index, value, irises):
    left, right = list(), list()

    for iris in irises:
        if iris.get_coordinates()[index] < value:
            left.append(iris)
        else:
            right.append(iris)

    return left, right

#Gets the most common iris in a group
def most_common_iris(irisGroup):
    outcomes = []
    for iris in irisGroup:
        outcomes.append(iris.get_type())

    return max(set(outcomes), key=outcomes.count)


# This is the main function that builds the tree
# Recursively builds each side of the tree based on optimal splits
def splitOnNode(node, max_depth, depth):
    left, right = node['groups']

    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = most_common_iris(left + right)
        return

    # check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = most_common_iris(left), most_common_iris(right)
        return

    # Left Child
    node['left'] = findSplit(left)
    splitOnNode(node['left'], max_depth, depth+1)

    # Riht Child
    node['right'] = findSplit(right)
    splitOnNode(node['right'], max_depth, depth+1)


# Finds a split in the data based on the best gini value. The returned groups are lists of the irises in each respective group
def findSplit(irises):
    class_values = get_labels(irises)
    b_index, b_value, b_score, b_groups = 999, 999, 999, None

    #Loops through the w,x,y,z values, finds optimal split based on gini score
    for index in range(4):
        for iris in irises:
            groups = split(index, iris.get_coordinates()[index], irises)
            giniVal = gini(groups, class_values)

            if giniVal < b_score:
                b_index, b_value, b_score, b_groups = index, iris.get_coordinates()[index], giniVal, groups

    return {'index':b_index, 'value':b_value, 'groups':b_groups} #This is the node (a dictionary)


# Build a decision tree
def build_tree(train, max_depth):
    root = findSplit(train)
    splitOnNode(root, max_depth, 1)
    return root

# Print a decision tree
def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), node['value'])))
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print('%s[%s]' % ((depth*' ', node)))


# Make a prediction with a decision tree, walks down the tree until it reaches a leaf node
def predict(tree, iris):
    if type(tree) == str:
        return tree
    if iris.get_coordinates()[tree['index']] < tree['value']:
        return predict(tree['left'], iris)
    else:
        return predict(tree['right'], iris)


# MAIN PROGRAM
allIrises = parse_irises("data/iris.data")

accuracy = 0
epoch = 0
class_values = get_labels(allIrises)

#Loop until it's reached 100% accuracy
while accuracy != 100 and epoch < 100:

    #Get a random train/test split
    irises, testIrises = train_test_split(allIrises, 0.2)

    #Build the tree from the training iris set
    tree = build_tree(irises, MAXDEPTH)

    iris_setosa = []
    iris_versicolor = []
    iris_virginica = []
    for iris in testIrises:
        if iris.get_type() == "Iris-setosa":
            iris_setosa.append(iris)
        elif iris.get_type() == "Iris-versicolor":
            iris_versicolor.append(iris)
        else:
            iris_virginica.append(iris)

    #Find the accuracy of the tree for each iris
    total = 0
    correct = 0
    for iris in iris_setosa:
        ans = predict(tree, iris)

        if ans == iris.get_type():
            correct += 1
        total += 1

    setosa_accuracy = correct/total*100
    epoch += 1
    print("Epoch #" + str(epoch))
    print("For ", len(iris_setosa), " Iris-setosa in the training set, Accuracy = " + str(setosa_accuracy) + "%")


    total = 0
    correct = 0
    for iris in iris_versicolor:
        ans = predict(tree, iris)

        if ans == iris.get_type():
            correct += 1
        total += 1

    versicolor_accuracy = correct/total*100
    print("For ", len(iris_versicolor), " Iris-versicolor in the training set, Accuracy = " + str(versicolor_accuracy) + "%")

    total = 0
    correct = 0
    for iris in iris_virginica:
        ans = predict(tree, iris)

        if ans == iris.get_type():
            correct += 1
        total += 1

    virginica_accuracy = correct/total*100
    print("For ", len(iris_virginica), " Iris-virginica in the training set, Accuracy = " + str(virginica_accuracy) + "%")

    if setosa_accuracy == 100.0 and versicolor_accuracy == 100.0 and virginica_accuracy == 100.0:
        accuracy = 100

print("Accuracy = " + str(correct/total*100) + "%")