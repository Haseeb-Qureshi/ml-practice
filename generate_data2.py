import csv
import numpy as np

NUM_SAMPLES = 5000
NUM_FEATURES = 1
CLASS_ODDS = 1

probs_given_class = np.random.uniform(low=0, high=1, size=NUM_FEATURES)
probs_given_not_class = np.random.uniform(low=0, high=1, size=NUM_FEATURES)

data = []
for i in range(NUM_SAMPLES):
    c = np.random.binomial(n=1, p=CLASS_ODDS/(CLASS_ODDS + 1))
    if c:
        x = np.random.binomial(n=1, p=probs_given_class, size=NUM_FEATURES)
    else:
        x = np.random.binomial(n=1, p=probs_given_not_class, size=NUM_FEATURES)

    data.append(np.concatenate((x, [c])))



with open("data2.csv", "w") as f:
    csv_writer = csv.writer(f)
    for record in data:
        csv_writer.writerow(record)
