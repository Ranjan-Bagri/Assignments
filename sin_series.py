import math

def sin(x,n):
	sine=0
	y=x*(math.pi/180)
	for i in range(n):
		sign=(-1)**i
		sine+=(((y**(2*i+1))/(math.factorial(2*i+1)))*sign)
	return sine

x=int(input('Enter the value in degree: '))
n=int(input('Enter the number of terms: '))

print(round(sin(x,n),3))