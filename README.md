# k-means-and-decision-tree-algos
By Ian McKechnie on March 20, 2023

This project compares the learning rates and accuracy between K-means and a decision tree for the Iris data set found here:
https://archive.ics.uci.edu/ml/datasets/iris

## To Run
1. Clone the repo
2. Navigate to the directory
3. Run `python3 kmeans.py`
4. Run `python3 decisionTree.py`

## Notes

I did not pick an N for kmeans, rather I ran epochs until it reachest either 100% accuracy or it reaches 100 epochs. I did this because sometimes it can get 100% accurate in 2 epochs (N) and sometimes it would run the full 100 times and only be 96 percent accurate. It's extremely fast so I put the 100 limit and it still completes in under 2 seconds.

The decion tree has a max depth of 4. It's specified in a variable called MAXDEPTH declared at the top of the file

# Results

### Kmeans
***Epoch = N***

Epoch  0  Accuracy:  26.666666666666668 %

Controid 0 distorition: 0

Controid 1 distorition: 545.0587499999998

Controid 2 distorition: 0

Epoch  1  Accuracy:  53.333333333333336 %

Controid 0 distorition: 92.6101388888889

Controid 1 distorition: 0

Controid 2 distorition: 27.640208333333344

Epoch  2  Accuracy:  53.333333333333336 %

Controid 0 distorition: 21.601860465116278

Controid 1 distorition: 0

Controid 2 distorition: 90.95714285714287

Epoch  3  Accuracy:  100.0 %

Controid 0 distorition: 45.04226415094341

Controid 1 distorition: 9.857857142857144

Controid 2 distorition: 11.09794871794872



-------------------------------------------------------------

After  4  epochs, the highest accuracy was:  100.0 %

The centroid positions are:

[6.633962264150941, 2.984905660377359, 5.3830188679245285, 1.913207547169811]

[5.749999999999999, 2.7571428571428567, 4.196428571428572, 1.3035714285714284]

[5.005128205128206, 3.3923076923076927, 1.458974358974359, 0.25384615384615383]


Their distortions are:

Controid 0 distorition: 45.04226415094341

Controid 1 distorition: 9.857857142857144

Controid 2 distorition: 11.09794871794872


*** Note this a good randomplacement of the centoids. It's possible to get a worse placement and have a lower accuracy. ***

### Decision Tree
Epoch #1

For  6  Iris-setosa in the training set, Accuracy = 100.0%

For  13  Iris-versicolor in the training set, Accuracy = 92.3076923076923%

For  11  Iris-virginica in the training set, Accuracy = 81.81818181818183%

Epoch #2

For  12  Iris-setosa in the training set, Accuracy = 100.0%

For  10  Iris-versicolor in the training set, Accuracy = 100.0%

For  8  Iris-virginica in the training set, Accuracy = 87.5%

Epoch #3

For  10  Iris-setosa in the training set, Accuracy = 100.0%

For  10  Iris-versicolor in the training set, Accuracy = 90.0%

For  10  Iris-virginica in the training set, Accuracy = 90.0%

Epoch #4

For  8  Iris-setosa in the training set, Accuracy = 100.0%

For  11  Iris-versicolor in the training set, Accuracy = 81.81818181818183%

For  11  Iris-virginica in the training set, Accuracy = 90.9090909090909%

Epoch #5

For  6  Iris-setosa in the training set, Accuracy = 100.0%

For  14  Iris-versicolor in the training set, Accuracy = 78.57142857142857%

For  10  Iris-virginica in the training set, Accuracy = 100.0%

Epoch #6

For  15  Iris-setosa in the training set, Accuracy = 100.0%

For  5  Iris-versicolor in the training set, Accuracy = 80.0%

For  10  Iris-virginica in the training set, Accuracy = 100.0%

Epoch #7

For  16  Iris-setosa in the training set, Accuracy = 100.0%

For  8  Iris-versicolor in the training set, Accuracy = 100.0%

For  6  Iris-virginica in the training set, Accuracy = 100.0%

Accuracy = 100.0%

*** Note, depending on the train test split, the accuracy can be lower or it could take a different number of epochs to achieve perfect accuracy. ***

## Analysis of the Algorithms

How I have my programs set up, they will run until they achieve a 100% accuracy rate where the entire test set is predicted correctly. Kmeans will run multiple times because the depending on where the centroids are randomly placed sometimes, they settle in positions that result in a prediction rate lower than 100% accurate. The Decision Tree on the other must run multiple times because depending on what the randomly selected training set is the tree sometimes branches on values that result in an algorithm that is not 100% accurate. This means the decision tree would benefit from a larger dataset as then the train test split would not affect the tree’s accuracy as much. So, by being able to perform multiple loops on each I was able to get both to 100% accuracy. A caveat to this is that they would require a different number of runs. I found on average that the decision tree required less time to reach 100% accuracy but was slower in doing so. So, for this data set and my implementation I think kmeans was more effective due to the speed the algorithm. I think the pros to the kmeans is it is conceptually easier to understand and faster to develop. The con to kmeans is its accuracy depends on where the initial centroids are placed. If they have bad initial and they settle in a bad place, the algorithm will not accurately predict the test set. Also, I knew how many centroids to initialize at the start since the data is labeled. The data exists in 4d space so I cannot visualize it to see how many clusters there are. So, I would have to perform trial and error to guess the centroid number had I not known. The pros to the decision tree is that it scales better. My issue with it is the data size is too small so depending on the random sample size from the data my tree could be wrong. So, a larger size would improve accuracy for it while run time for testing would not be affected as much. This is also a double-edged sword and one of its cons, too small of a data set and it overfits the data by branching on bad values resulting in it being less accurate for the test set. I also observed it being slower to create the tree than a kmeans epoch so initial training time is a con.