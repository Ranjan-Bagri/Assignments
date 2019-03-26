<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the factorial of a given number


### Desciption:
Factorial of a non-negative integer \\(n\\), denoted by \\(n!\\), is the product of all positive integers less than or equal to \\(n\\).
\\[n!=n(n-1)(n-2)\cdots3.2.1\\]

for example
\\[5!=5\times 4\times 3\times 2\times 1\\]

So \\(n!\\) can be written as a recurrence relation for \\(n\geq 1\\)
\\[n!=n.(n-1)!\\]

The value of \\(0!\\) is \\(1\\), according to the convention for an empty product.

### Implementation:

<kbd>Input</kbd>

```python
def factorial(n):
    f = 1
    for i in range(2,n+1):
        f*=i
    return f

num=int(input('Enter a integer: '))
print('Factorial of %s is %s'%(num,factorial(num)))
```

<kbd>Output</kbd>

```python
Enter a integer: 5
Factorial of 5 is 120
```


[Download](py/factorial.py)

or

[Try it online!](https://tio.run/##TY6xDsIwDET3fIWXKjF0KYilUkf4jwiSYok6kesMfH0IBSQ8WHfy6Z3zU@@Jj7XeQoTor5qE/MMxjgbaRJhg@KgkQEAM4nkO7tDzfviGtvNuos1I0CIM0Rguy0SsjjgXdfbMGgR8Q2iYg4xgEU2Wd8JefsWQInQr0Nq27VxD9H9PlQURaz29AA "Python 3 – Try It Online")
