from __future__ import division

import sys

from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import Ridge, LinearRegression
from sklearn import cross_validation
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import LinearSVC

from data_science.data_acquisition import *
from data_science.linear_regression import *


def main():
    # rows = read_csv('/Users/mstepan/repo/incubator/algorithms-py/data_set/Advertising.csv')
    # print_statistics('Advertising',
    # rows,
    # ['TV', 'Radio', 'Newspaper'],
    # 'Sales')

    print_statistics('Income2',
                     read_csv('/Users/mstepan/repo/incubator/algorithms-py/data_set/Income2.csv'),
                     ['Education', 'Seniority'],
                     'Income')

    # rows = read_csv('/Users/mstepan/repo/incubator/algorithms-py/data_set/winequality-white.csv')
    # print_statistics('Wine',
    #                  rows,
    #                  [
    #                      "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    #                      "chlorides", "free sulfur dioxide", "total sulfur dioxide",
    #                      "density", "pH",
    #                      "sulphates", "alcohol"
    #                  ],
    #                  "quality")

    print("\nMain completed...")
    print("Python %s on %s" % (sys.version, sys.platform))


def print_statistics(title, rows, x_labels, y_label):
    print("--------------------------- %s ---------------------------" % title)

    x_train_base = combine_x(rows, x_labels)

    # 60% - train set, 40%  - test data
    x_train, x_test, y_train, y_test = \
        cross_validation.train_test_split(x_train_base, rows[y_label], test_size=0.4, random_state=0)

    print("training size: %s, features(p): %s, %s\n" % (len(x_train), len(x_train[0]), x_labels))

    # Ridge(), LinearRegression(), Lasso(alpha=0.1), ElasticNet(alpha=0.1, l1_ratio=0.7)
    pipeline = make_pipeline(
        # VarianceThreshold(),

        # non linear
        # PolynomialFeatures(2),

        # feature selection
        # SelectKBest(f_regression, k=2),

        # estimation methods
        # LinearSVC(penalty="l1", dual=False),
        LinearRegression()
    )

    pipeline.fit(x_train, y_train)

    # alpha = pipeline._final_estimator.intercept_
    # betas = pipeline._final_estimator.coef_
    #
    # table_data = [{'Coefficient': alpha,
    # 'Std. error': float('NaN'),
    # 't-statistic': float('NaN'),
    #                'p-value': float('NaN')}]
    #
    # for index, x_type in enumerate(x_labels):
    #     x_single = rows[x_type]
    #     beta = betas[index]
    #
    #     table_data.append({'Coefficient': beta,
    #                        'Std. error': standard_error(pipeline, x_train, y_train, x_single),
    #                        't-statistic': t_stat(pipeline, beta, x_train, y_train, x_single),
    #                        'p-value': p_value(pipeline, alpha, betas, beta, x_train, y_train, x_single)})
    #
    # print(pd.DataFrame(table_data, index=['Intercept'] + x_labels))
    print()

    rse_value = rse(pipeline, x_train, y_train)
    print("RSE: %.2f" % rse_value)
    print("F-stat: %.2f" % f_stat(pipeline, x_train, y_train))
    print("MSE: %.2f" % mse(pipeline, x_test, y_test))
    print("R^2: %.1f%%" % (r_squared(pipeline, x_test, y_test) * 100))

    print("")

    plot_residual_errors(pipeline, x_train, y_train, rse_value)

    print("Method: %s" % pipeline)


def plot_residual_errors(pipeline, x_train, y_train, rse_value):
    """
    Plot residuals vs fitted values (y predicted).
    If absolute value for residual error > 3 - this is possible outlier
    """
    plt.scatter(
        [pipeline.predict(x_values) for x_values in x_train],
        [(y_i - pipeline.predict(x_i)) / rse_value for x_i, y_i in zip(x_train, y_train)],
        label="Samples")
    plt.xlabel("Fitted values (y_i)")
    plt.ylabel("studentized residuals")
    plt.grid(True)

    plt.show()


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