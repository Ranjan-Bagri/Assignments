<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the derivative of a given single variable function on a given point


### Desciption:

If \\(y\\) is a function of \\(x\\), then the derivative of \\(y\\) is given by \\(y' = f'(x)\\)

\\[\therefore \frac{dy}{dx} = \frac{d}{dx} f(x) = \lim_{h\to 0} \frac{f(x+h)-f(x)}{h} \\]

For a resonably small value of \\(h(e.g:h=10^{-7})\\) the derivative of \\(y\\) at the point \\(x=a\\) will be

\\[\frac{dy}{dx} = \lim_{h\to 0} \frac{f(a+h)-f(a)}{h}\\]
\\[\approx \frac{f(a+h)-f(a)}{h}\\]
\\[[\because h\approx 0]\\]

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

[Try it online!](https://tio.run/##K6gsycjPM/7/PyU1TSFNo0LTiksBCIpSS0qL8hQqtLRMtE21gJSxrhkXF0hNSmpRZlmqRlppXrJOIlR1hq1hqq45mFlsC5LRSNTO0NSFsDSRDUzLyU8s0SjW1M/g4iooyswr0YCZp2Oqqfn/PwA "Python 3 – Try It Online")
