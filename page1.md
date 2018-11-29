  <script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the sum and average of a list of numbers


### Description:

If a set of \\(n\\) numbers is represented by \\((a_1,a_2,\cdots,a_n)\\), then the sum of \\(n\\) numbers will be
\\[s= a_1+a_2+\cdots+a_n\\]
\\[= \sum_{i=1}^{n} a_i\\]
where \\(n\in N\\)

And the average of the all numbers of the list will be
\\[a=\frac{s}{n}=\frac{\sum_{i=1}^{n} a_i}{n}\\]

### Implementation:

<kbd>Input</kbd>

```python
list=[22,12,-3,4,-56,78]
sum=sum(list)
print(sum)

n=len(list)
avg=sum/n
print(avg)
```

<kbd>Output</kbd>

```python
57
9.5
```

