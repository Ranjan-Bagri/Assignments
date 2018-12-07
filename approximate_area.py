from random import *
r=float(input('radius='))

def area(n):
	square=0
	circle=0
	while square<n:
		x=random()*r
		y=random()*r
		square_area=((2*r)**2)
		if ((x**2+y**2)<=(r**2)):
			circle+=1
		square+=1
	return (circle/square)*square_area

print(area(500000))