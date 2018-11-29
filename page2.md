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