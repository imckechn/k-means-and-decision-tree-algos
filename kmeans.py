from kMeans.iris import Iris
from kMeans.centroid import Centroid
import math
import random

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


#This creates all the centroids and returns a list of centroid objects
def create_centroids():
    while True:
        #count = input("How many centroids would you like to create? ")
        count = "3"

        if count.isdigit():
            break

    count = int(count)
    centroids = []
    for i in range(count):
        centroids.append(Centroid())

    return centroids


# Calculates the distance between a centroid and an iris. Returns the distance
def calculate_distance(iris, centroid):
    iris_coordinates = iris.get_coordinates()
    centroid_coordinates = centroid.get_center()

    distance = 0
    for i in range(len(iris_coordinates)):
        distance += math.pow(iris_coordinates[i] - centroid_coordinates[i], 2)

    return math.sqrt(distance)


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


def kMeans(irises, centroids):
    print("Loops")

    # remove the points from each centroid
    for centroid in centroids:
        centroid.wipe_points()

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



print("Starting k-means clustering algorithm...")
irises = parse_irises("data/iris.data")
centroids = create_centroids()


# Get the max values of all the irises and put the centroids randomly in that 4D plane
maxValues = get_max_values(irises)
for centroid in centroids:
    w = random.uniform(0, maxValues[0])
    x = random.uniform(0, maxValues[1])
    y = random.uniform(0, maxValues[2])
    z = random.uniform(0, maxValues[3])

    centroid.set(w, x, y, z)

centroids = kMeans(irises, centroids)

print("Centroid centers after clustering:")
for centroid in centroids:
    print("Centroid: ", centroid.get_center())

    points = centroid.get_points()
    for point in points:
        print(point.get_type())
    print("")

