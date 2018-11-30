<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To sort the numbers of a given list in both ascending and descending order


### Desciption:

Sorting is a process of re-arranging the elements of a list in crtain order.

Let a list is given by \\([3,2.5,4.5,-1.2,5,0]\\)
By sorting this list ascending order we get 
\\[[-1.2, 0, 2.5, 3, 4.5, 5]\\]
Similarly in descending order, we get
\\[[5, 4.5, 3, 2.5, 0, -1.2]\\]

### Implementation:

<kbd>Input</kbd>

```python
list=[3,2.5,4.5,-1.2,5,0]

asc_sort=sorted(list)
print(asc_sort)

desc_sort=sorted(list,reverse=True)
print(desc_sort)
```
t
<kbd>Output</kbd>

```python
[-1.2, 0, 2.5, 3, 4.5, 5]
[5, 4.5, 3, 2.5, 0, -1.2]
```
