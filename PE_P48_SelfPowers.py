## Author: James Norcross
## Date: 2/24/15
## Description: Finds the last ten digits in the sum 1^1 + 2^2 + 3^3 + ... + 1000^1000

total = 0

for i in range(1,1001):
    total += i**i

last10digits = total % 10**10
print ("The last ten digits of the sum are %s") % str(last10digits)
print 'done'
