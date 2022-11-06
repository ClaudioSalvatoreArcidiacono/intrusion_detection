# Intrusion Detection

The topic of cyber security is becoming more and more relevant in the last years. In this repository, I have decided to play with data from the [KDD Cup 1999](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html) competition.

This dataset contains synthetic data on cyber attacks on military networks. More details on the data used are available in the [data](data.md) section.

Even if the dataset contains labels, I have decided to not use them for modelling in order to better simulate a more realistic usecase where labels are unavailable. Moreover, I will not try to classify each intrusion in its cyber attack class, but I grouped all anomalies into a single class and I framed the problem as a binary classification problem.

When modelling, I decided to split the classification problem into two. The first one focusing in detecting DDOS attacks, because they are extremely frequent in our dataset, and the second one in detecting all other cyber attacks because they are very rare.

When evaluating, I will evaluate the model on those two different problems separately.
