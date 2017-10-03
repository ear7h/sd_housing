import csv
import numpy as np
import matplotlib.pyplot as plt

listings = []

with open('composition.csv') as data:
	reader = csv.DictReader(data, delimiter=',')
	for row in reader:
		listings.append(row)

def hasPrice(listing):
	return listing['price'] != 'NA'

# sanity check
# for listing in listings:
# 	if hasPrice(listing):
# 		print(listing['price'])

all_prices = [float(listing['price']) for listing in listings if hasPrice(listing)]

plt.boxplot(all_prices, whis='range')
plt.show()

plt.hist(all_prices, 100)
plt.show()
