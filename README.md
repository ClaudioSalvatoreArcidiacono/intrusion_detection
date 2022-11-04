# Intrusion Detection

In this repository an unsupervised intrusion detection model is developed and wrapped around an API server.

In order to train and evaluate the model, data from the 1999 edition of the KDD challenge have been used. Data will not be

## Downloading the data

Run in in a terminal shell from the project folder the following code:

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

