<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## derivative


### Desciption:


### Implementation:

<kbd>Input</kbd>

```python
def f(x):
    return x**4+5*x**3-6

def derive(func,a):
    h=1e-7
    s=func(a+h)-func(a)
    return float(s)/h

print(derive(f,5))
```

<kbd>Output</kbd>

```python
875.0000256441126
```
