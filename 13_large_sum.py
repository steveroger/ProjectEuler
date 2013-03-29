# Project Euler Question 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

f = open('13_large_sum.txt', 'r') # The number is stored in this file
sum = 0

for line in f:
	line = long(line.replace('\n', ''))
	sum += line
print str(sum)[0:10]