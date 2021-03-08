import math
def prime(n):
	if n<=1:
		return False
	if n==2:	
		return True
	if n>2 and n%2==0:
		return False
	maxi=int(math.sqrt(n))+1
	for i in range(3,maxi,2):
		if n%i==0:
			return False
	return True
l=[2]
for i in range(3,10**5,2):
	if prime(i):
		l.append(i)
print(l)
