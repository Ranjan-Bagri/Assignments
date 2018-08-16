#Q:4
#Determine the value of pi by Monte-Carlo simulation

#Instructor: Sk. Ismile
#author: Ranjan Bagri
#license: MIT

from random import * #built-in python module for random number generation

def pi(n): #defines a function with argument n.

# n is the number of iteration. We"ll get closer to accuracy in final output for higher values of n.
	
	s = 0.0
	
	c = 0.0
	
	while s<n: #Here the while loop is used to repeat the instructions mentioned below n number of times
		
		x = random() #assigns a random number(between 0 and 1) to x.
		
		# Here variable x and y are considered to be x and y co-ordinate of a point respectively.
		
		y = random() #assigns a random number(between 0 and 1) to x.
		
		if ((x**2+y**2)<1):  #using the formula x^2+y^2=r^2, where r=1
			
			c+=1 #increment of c when the above equation is satisfied
			
		s+=1 #increment as whole for continuing the while loop
		
	return (c/s)*4 #return the value of ratio between number of points inside circle and number of points inside square multiplied by area of square.

print "Approximate value of pi is %s"%pi(5000000) #call the function to execute its value while a certain numerical value is provided as an argument.
