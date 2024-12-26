import math

L = [12, 3, 8, 125, 10, 98, 54, 199]
log_L= [math.log(x) for x in L]
L[4]=0
print(L)
print(math.log(L[4]))