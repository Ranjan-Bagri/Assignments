#Q:4
#Determine the value of pi by Monte-Carlo simulation

#Instructor: Sk. Ismile
#author: Ranjan Bagri
#license: MIT

from random import *

def pi(n):
	
	s = 0.0
	
	c = 0.0
	
	while s<n:
		
		x = random()
		
		y = random()
		
		if ((x**2+y**2)<1):
			
			c= c+1
			
		s=s+1
		
	return (4*c)/s

print pi(5000000)