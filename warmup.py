from sys import stdin
import numpy as np

CI_CONSTANT = 1.96

N = int(stdin.readline())
data_list_string = stdin.readline().split()
data_list_int = [int(i) for i in data_list_string]

### OUTPUT ###
#Mean (format:0.0) on the first line
mean = np.mean(data_list_int)
print ('{0:.1f}'.format(mean))
#Median (format: 0.0) on the second line
print ('{0:.1f}'.format(np.median(data_list_int)))
#Mode(s) (Numerically smallest Integer in case of multiple integers)
counts = {data_list_int[0]: 1}
for i in data_list_int[1:len(data_list_int)]:
	if i in counts:
		counts[i] = counts[i]+1
	else:
		counts[i] = 1
max_count = 0
mode = 0
for k in counts.keys():
	if counts[k] > max_count:
		mode = k
		max_count = counts[k]
	if counts[k] == max_count and k < mode:
		mode = k
print (mode)
#Standard Deviation (format:0.0) 
sd = np.std(data_list_int)
print ('{0:.1f}'.format(sd))
#Lower and Upper Boundary of Confidence Interval (format: 0.0) with a space between them.
mean = np.mean(data_list_int)
lower = mean - CI_CONSTANT * sd / np.sqrt(N)
upper = mean + CI_CONSTANT * sd / np.sqrt(N)

print ('{0:.1f} {1:.1f}'.format(lower,upper))