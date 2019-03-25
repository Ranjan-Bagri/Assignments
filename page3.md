  <script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To check a given number Armstrong number or not

### Description:

An Armstrong number is \\(n\\) digit based number such that the sum of its digits raised to power \\(n\\) is the number itself.
Hence the number \\(153\\) is an Armstrong number because
\\[153=1^3+5^3+3^3=1+125+27=153\\]
Similarly,
\\[370=3^3+7^3+0^3\\]
\\[371=3^3+7^3+1^3\\]
\\[407=4^3+0^3+7^3\\]

### Implementation:

<kbd>Input</kbd>

```python
def armstrong(x):
        k = str(x)
        res = 0
        
        for i in range(0,len(k)):
                res += int(k[i])**3

        if (res==x):
        	return "%s is an Armstrong Number"%x
        else:
        	return "%s is not an Armstrong Number"%x

print(armstrong(153))
print(armstrong(155))
```

<kbd>Output</kbd>

```python
153 is an Armstrong Number
155 is not an Armstrong Number
```

[Try it online!](https://tio.run/##dZBBCoMwEEXX9RSDICS2C4u4KWThBXqB0oWlow3qRCYR7OnTFNrURZ3VzOP/z2emp3sYKr2/YwsNj9axoU4s8pTAZ3pQEHBgETHaAIt4x6U1DBo0ATfUoSgOA5Lo5SptHbFXQepEf9FXmedlEkW6BREESq177BjdzARpZkFbaAjqb184z@MNOc2WqMbB4qaXjNvyJxO/O/1ecaxKKf/QSkrvXw "Python 3 – Try It Online")
