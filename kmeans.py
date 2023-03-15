from kMeans.iris import Iris
from kMeans.centroid import Centroid

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

def create_centroids():
    while True:
        count = input("How many centroids would you like to create? ")

        if count.isdigit():
            break

    count = int(count)
    centroids = []
    for i in range(count):
        centroids.append(Centroid())

    return centroids


def calculate_distance(iris, centroid):


print("Starting k-means clustering algorithm...")
irises = parse_irises("data/iris.data")
centroids = create_centroids()

