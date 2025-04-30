#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:27:24 2025

@author: elizabethdewar-kudsi
"""

import statistics
import matplotlib.pyplot as plt
import csv


# turn csv file into list

def csv_to_list(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_list.append(row)
    return data_list


file_path = 'your_file.csv'  # Replace with the actual path to your CSV file

t = csv_to_list(file_path)
r = []
num = []
for x in range(2, len(t) + 1):
    num.append(x)
    r.append(statistics.stdev(t[:x]))

# Create plot
plt.plot(num, r, "k.")

# Customize plot
plt.xlabel("number of measurments")
plt.ylabel("standard deviation")

plt.grid(True)
# Show plot
plt.show()
