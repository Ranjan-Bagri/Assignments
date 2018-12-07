def factorial(n):
    f = 1
    for i in range(2,n+1):
        f*=i
    return f

num=int(input('Enter a integer: '))
print('Factorial of %s is %s'%(num,factorial(num)))
