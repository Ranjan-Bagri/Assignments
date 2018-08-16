#Q:7
#Determine the volume of a sphere of given radius by Monte-Carlo simulation

#Instructor: Sk. Ismile
#Author: Ranjan Bagri
#license: MIT

from random import * #built-in python module for random number generation 

r = float(input('radius=')) #radius of the given sphere whose volume to be determined

def volume(n): #defines a function with argument n.

# n is the number of iteration. We"ll get closer to accuracy in final output for higher values of n.
	
	s = 0.0
	
	c = 0.0
	
	while s<n: #Here the while loop is used to repeat the instructions mentioned below n number of times
		
		x = random()*r #assigns a random number(between 0 and 1) multiplied by the radius to x.
		
		# Here variable x and y are considered to be x and y co-ordinate of a point respectively.
		
		y = random()*r #assigns a random number(between 0 and 1) multiplied by the radius to y.
		
		z = random()*r #assigns a random number(between 0 and 1) multiplied by the radius to z.
		
		sa = ((2*r)**3) #volume of a cube having side of length 2r
		
		if ((x**2+y**2+z**2)<=(r**2)): #using the formula x^2+y^2+z^2=r^2
			
			c+=1 #increment of c when the above equation is satisfied
			
		s+=1 #increment as whole for continuing the while loop
		
	return (c/s)*sa #return the value of ratio between number of points inside sphere and number of points inside cube multiplied by volume of cube.

print "Approximate volume of the sphere is %s"%volume(500000) #call the function to execute its value while a certain numerical value is provided as an argument.
