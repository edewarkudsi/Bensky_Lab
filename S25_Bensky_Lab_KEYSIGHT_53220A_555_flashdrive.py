#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:27:24 2025

@author: elizabethdewar-kudsi
"""

import statistics
import matplotlib.pyplot as plt

def read_values(file_path):
    values = []
    with open(file_path, 'r', encoding='latin1') as file:
        for line in file:
            try:
                values.append(float(line.strip()))
            except ValueError:
                continue  # skip any non-numeric lines
    return values


file_path = '/Users/elizabethdewar-kudsi/Library/CloudStorage/OneDrive-CalPoly/Bensky_Lab/DataLog_20250423_112604.csv'

values = read_values(file_path)

r = []
num = []
for x in range(2, len(values) + 1):
    num.append(x)
    r.append(statistics.stdev(values[:x]))

plt.plot(num, r, "k.")
plt.xlabel("Number of Measurements")
plt.ylabel("Standard Deviation")
plt.xlim([0,1000])
plt.grid(True)
plt.show()