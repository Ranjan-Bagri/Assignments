from math import sqrt,cos,radians

def estimate_pi(length,n):
	radius = float((length)/(sqrt(2-2*(cos(radians(360/n))))))
	diameter = 2*radius
	c = (length*n)
	return float(c/diameter)
	
print((estimate_pi(1,500000)))