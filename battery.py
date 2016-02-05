# Michael Wattendorf
# 3 February 2016
# hackerrank Battery challenge
##########################################################
# traningdata is of the form
# time_charging, time_batteryLasted
# GOAL: predict time_batteryLasted given time_charging

from sys import stdin
import numpy as np
#import matplotlib.pyplot as plt 
from sklearn import linear_model

time_charging = []
time_batteryLasted = []

with open("trainingdata.txt") as f:
	for line in f:
		lineAsList = line.strip('\n').split(',')
		time_charging.append(float(lineAsList[0]))
		time_batteryLasted.append(float(lineAsList[1]))

#plt.scatter(time_charging,time_batteryLasted)
#plt.show()
# visual inspection shows a cutoff around 4 hours of charging
# that leads to a steady battery life of around 8 hours.
# I'll split the data then into two cases: full charge, less than full charge

# Full charge category:
min_fullCharge = 100
for i in range(0,len(time_batteryLasted)-1):
	if (time_batteryLasted[i] >= 8.00):
		if (time_charging[i] < min_fullCharge):
			min_fullCharge = time_charging[i]
#print min_fullCharge

# Less than full charge
# inspection shows this is very close to a linear function
X_less = []
Y_less = []
for i in range(0,len(time_batteryLasted)-1):
	if (time_charging[i] < min_fullCharge):
		X_less.append(time_charging[i])
		Y_less.append(time_batteryLasted[i])

clf = linear_model.LinearRegression()
X_less = np.array(X_less)
Y_less = np.array(Y_less)
clf.fit(X_less[:,np.newaxis],Y_less)

for line in stdin:
	x = float(line)
	if x < min_fullCharge:
		print ("{0:.2f}".format(float(clf.predict(x)[0])))
	else:
		print ("8.00\n")