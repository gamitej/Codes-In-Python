#T.C---->> O(log(n))
#power using recursion 
def power(a,b):
	if b==0:
		return 1
	res=power(a,b//2)
	if b%2!=0:
		return res*res*a
	else:
		return res*res
print(power(2,32))

# power using bit values
def power(a,b):
	res=1
	while b>0:
		if b&1:
			res*=a
		a=a*a
		b>>=1
	return res
print(power(2,32))

# for large (a,b) values
def power(a,b,modd):
	a%=modd
	res=1
	while b>0:
		if b&1:
			res=res*a%modd
		a=a*a%modd
		b>>=1
	return res
print(power(2,32,10**9+7))
