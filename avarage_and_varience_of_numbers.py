#Q:5
#Determine the avarage and varience for given set of numbers (2,-3,5,7,8)

#Instructor: Sk. Ismile
#author: Ranjan Bagri
#license: MIT

x = [2,-3,5,7,8] #creates a list

l = len(x) #number of elements or length of the list

s = sum(x) #sum of all numbers in the list

avg = float(s)/l #avarage

print "Avarage of all numbers is %s\n"%avg

q = sum([(i**2) for i in x]) #sum of squares of all numbers

var = float(q)/l - avg**2 #varience following the equation

# (sum(x^2)/n)-(avarage^2)
print "Varience is %s"%var