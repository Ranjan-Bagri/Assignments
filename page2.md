  <script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the sum of all multiplliers of 3 less than 100

### Description:

If the set of first \\(100\\) natural numbers is represented by \\((a_1,a_2,a_3,\cdots,a_{100})\\), then the sum of all multipliers of \\(3\\) less than \\(100\\) will be
\\[s=\sum_{i=0}^{99} a_{i+3} \\]

### Implementation:

<kbd>Input</kbd>

```python
l=list(range(100))
sum=0
for i in l:
	if (i%3==0):
		sum+=i
print(sum)
```

<kbd>Output</kbd>

```python
1683
```


[Download]

or

[Try it online!](https://tio.run/##DcoxDoAgDADAGV7RxaSNSw2bSR/jINoECwEcfD0yXnLl63e2MEaSpK1jPew6cWMm8u19hH3MFRTUIO3eaQTUJYgwTbk5VlFfqlrHCRrjBw "Python 3 – Try It Online")
