from kMeans.centroid import Centroid
import math
import random
from helper.helperFunctions import *

#This creates all the centroids and returns a list of centroid objects
def create_centroids():
    centroids = []
    for i in range(3):
        centroids.append(Centroid())

    return centroids


# Get the highest w,x,y,z values of the iris group
def get_max_values(irises):
    maxW = 0
    maxX = 0
    maxY = 0
    maxZ = 0

    for iris in irises:
        coordinates = iris.get_coordinates()
        if coordinates[0] > maxW:
            maxW = coordinates[0]

        if coordinates[1] > maxX:
            maxX = coordinates[1]

        if coordinates[2] > maxY:
            maxY = coordinates[2]

        if coordinates[3] > maxZ:
            maxZ = coordinates[3]

    return [maxW, maxX, maxY, maxZ]


#Main kmeans algo
def kMeans(irises, centroids):

    # remove the closest irises from each centroid
    for centroid in centroids:
        centroid.wipe_irises()

    #For each centroid
    for iris in irises:
        closestCentroid = None
        minDistanc = 100
        for centroid in centroids:
            distance = calculate_distance(iris, centroid)
            if distance < minDistanc:
                minDistanc = distance
                closestCentroid = centroid

        closestCentroid.append_iris(iris)

    #Update the centroids positiosn
    moved = False
    for centroid in centroids:
        moved = centroid.update_center()

    # If the centroids moved, run the algo again
    if moved:
        centroids = kMeans(irises, centroids)

    return centroids


# MAIN PROGRAM
print("Starting k-means clustering algorithm...")
allIrises = parse_irises("data/iris.data")


highScore = 0
score = 0
epoch = 0
bestCentroids = []

#This loops the algorithm over and over again
while score < 1 and epoch < 100:
    centroids = create_centroids()
    irises, testIrises = train_test_split(allIrises, 0.2)

    # Get the max values of all the irises and put the centroids randomly in that 4D plane
    maxValues = get_max_values(irises)
    for centroid in centroids:
        w = random.uniform(0, maxValues[0])
        x = random.uniform(0, maxValues[1])
        y = random.uniform(0, maxValues[2])
        z = random.uniform(0, maxValues[3])

        centroid.set(w, x, y, z)

    #Finds the centroids using kmeans
    centroids = kMeans(irises, centroids)

    # Set the most common irises for each centroid (i.e. which iris came up the most in it's group)
    for centroid in centroids:
        centroid.set_most_common_iris()

    # Now find the accuracy of the algorithm
    correct = 0
    for iris in testIrises:
        closestCentroid = None
        minDistanc = 100
        for centroid in centroids:
            distance = calculate_distance(iris, centroid)
            if distance < minDistanc:
                minDistanc = distance
                closestCentroid = centroid

        if closestCentroid.get_most_common_iris() == iris.get_type():
            correct += 1

    #Compute the score of these centroids
    score = correct / len(testIrises)
    if score > highScore:
        highScore = score
        bestCentroids = centroids
    print("Epoch ", epoch, " Accuracy: ", score * 100, "%")
    for i in range(len(centroids)):
        print("Controid", i, "distorition:", centroids[i].get_distortion())
    epoch += 1


#Final Printout
print("\n\n-------------------------------------------------------------")
print("After ", epoch, " epochs, the individual Irises accuracies are as follows")

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
    closestCentroid = None
    minDistanc = 100
    total += 1
    for centroid in centroids:
        distance = calculate_distance(iris, centroid)
        if distance < minDistanc:
            minDistanc = distance
            closestCentroid = centroid

    if closestCentroid.get_most_common_iris() == iris.get_type():
        correct += 1

setosa_accuracy = correct/total*100
epoch += 1
print("Epoch #" + str(epoch))
print("For ", len(iris_setosa), " Iris-setosa in the training set, Accuracy = " + str(setosa_accuracy) + "%")


total = 0
correct = 0
for iris in iris_versicolor:
    closestCentroid = None
    minDistanc = 100
    total += 1
    for centroid in centroids:
        distance = calculate_distance(iris, centroid)
        if distance < minDistanc:
            minDistanc = distance
            closestCentroid = centroid

    if closestCentroid.get_most_common_iris() == iris.get_type():
        correct += 1

versicolor_accuracy = correct/total*100
print("For ", len(iris_versicolor), " Iris-versicolor in the training set, Accuracy = " + str(versicolor_accuracy) + "%")

total = 0
correct = 0
for iris in iris_virginica:
    closestCentroid = None
    minDistanc = 100
    total += 1
    for centroid in centroids:
        distance = calculate_distance(iris, centroid)
        if distance < minDistanc:
            minDistanc = distance
            closestCentroid = centroid

    if closestCentroid.get_most_common_iris() == iris.get_type():
        correct += 1

virginica_accuracy = correct/total*100
print("For ", len(iris_virginica), " Iris-virginica in the training set, Accuracy = " + str(virginica_accuracy) + "%")

print("\nThe centroid positions are:")
for centroid in bestCentroids:
    print(centroid.get_center())
print("")

print("Their distortions are:")
for i in range(len(bestCentroids)):
        print("Controid", i, "distorition:", bestCentroids[i].get_distortion())