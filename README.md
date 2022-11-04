# Intrusion Detection

In this repository an unsupervised intrusion detection model is developed and wrapped around an API server.

In order to train and evaluate the model, data from the 1999 edition of the KDD challenge have been used.

## Dataset

### Getting the data

Data will not be published to git. In order to download the data run in in a terminal shell from the project folder the following commands:

```bash
# Download data, 10 percent only
wget -N http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
# Download headers
wget -N http://kdd.ics.uci.edu/databases/kddcup99/kddcup.names
# Move data to folder
mv kddcup* data
# Unzip
echo n | gunzip data/kddcup.data_10_percent.gz
```

### Dataset Description

> This is the data set used for The Third International Knowledge Discovery and Data Mining Tools Competition, which was held in conjunction with KDD-99 The Fifth International Conference on Knowledge Discovery and Data Mining. The competition task was to build a network intrusion detector, a predictive model capable of distinguishing between `bad` connections, called intrusions or attacks, and `good` normal connections. This database contains a standard set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment.

source: [KDD Cup 1999 Data](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
