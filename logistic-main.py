from __future__ import division

import sys

from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

from data_science.data_acquisition import *


def main():
    rows = read_csv('/Users/mstepan/repo/incubator/algorithms-py/data_set/Iris.csv')

    x_labels = ["Sepal length", "Sepal width", "Petal length", "Petal width"]
    y_label = "Species"

    x_train_base = combine_x(rows, x_labels)

    # divide train/test set as 60/40
    x_train, x_test, y_train, y_test = \
        cross_validation.train_test_split(x_train_base, rows[y_label], test_size=0.4, random_state=0)

    rf = RandomForestClassifier(n_estimators=1000,
                                criterion="entropy",
                                max_features="auto",
                                bootstrap=True,
                                n_jobs=8,
                                random_state=1)
    rf.fit(x_train, y_train)

    print("categories: %s" % rf.classes_)

    for one_sample, expected_category in zip(x_test, y_test):

        max_probability = 0.0
        actual_category = None

        probabilities = []

        for category_index in range(3):
            category_probability = rf.predict_proba(one_sample)[:, category_index]

            probabilities.append(category_probability)

            if category_probability > max_probability:
                max_probability = category_probability
                actual_category = rf.classes_[category_index]

        if actual_category != expected_category:
            print("Categories are not same, expected = %s, actual = %s, probs = %s" %
                  (expected_category, actual_category, probabilities))

    print("Python %s on %s" % (sys.version, sys.platform))


def combine_x(rows, x_labels):
    x_train = []

    for index in range(len(rows[x_labels[0]])):
        x_i_values = []

        for x_type in x_labels:
            x_i_values.append(rows[x_type][index])

        x_train.append(x_i_values)

    return x_train


if __name__ == "__main__":
    main()