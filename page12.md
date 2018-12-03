<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To check if a given number is palindrome or not


### Desciption:
A palindromic number is a number that remains the same when its digits are reversed.

For example,

\\(16461\\) will give the exact same number as it was before reversing, but \\(16578\\) will not.

### Implementation:

<kbd>Input</kbd>

```python
def palin_num(num):
	inp=str(num)
	nums=inp[::1]
	rev=nums[::-1]
	if nums==rev:
		return "%s is a Palindrome Number"%inp
	else:
		return "%s is not a Palindrome Number"%inp

i=int(input('Enter a number: '))
print(palin_num(i))
```

<kbd>Output</kbd>

```python
Enter a number: 3443
3443 is a Palindrome Number
```
