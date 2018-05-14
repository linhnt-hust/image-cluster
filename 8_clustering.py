# /usr/bin/env python
# -*- coding: UTF-8 -*-

import csv
import os
import shutil

import numpy as np
from sklearn.cluster import SpectralClustering, AgglomerativeClustering


def result(filenames, labels):
    n_clusters = max(labels)
    for i in xrange(n_clusters + 1):
        if not os.path.exists('./result/' + str(i)):
            os.makedirs('./result/' + str(i))
    for label, txtname in zip(labels, filenames):
        # name = txtname[0:txtname.rfind('.')] + '.jpg'
        shutil.copyfile('./data/' + txtname,
                './result/' + str(label) + '/' + txtname)

def result1(filenames, labels):
    n_clusters = max(labels)
    for i in xrange(n_clusters + 1):
        if not os.path.exists('./result1/' + str(i)):
            os.makedirs('./result1/' + str(i))
    for label, txtname in zip(labels, filenames):
        # name = txtname[0:txtname.rfind('.')] + '.jpg'
        shutil.copyfile('./data/' + txtname,
                './result1/' + str(label) + '/' + txtname)


def input_data():
    filenames = []
    with open('./result.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if filenames == []:
                filenames = [row[0]]
                data = np.array(row[1:])
            else:
                filenames.append(row[0])
                data = np.vstack((data, np.array(row[1:])))
    return filenames, data


if __name__ == '__main__':
    filenames, data = input_data()
    # n_clusters is a number of clusters
    SC = SpectralClustering(n_clusters=6, eigen_solver='arpack', affinity='cosine')
    AC = AgglomerativeClustering(linkage="ward", n_clusters=6)
    labels1 = SC.fit_predict(data)
    labels = AC.fit_predict(data)
    result1(filenames, labels1)
    result(filenames, labels)
