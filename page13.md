<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To check if a string is Palindrome or not


### Desciption:
A palindromic string is a string that remains the same when its characters are reversed.

For example,

The word \\('eye'\\) will give the exact same word as it was before reversing, but \\('box'\\) will not.

### Implementation:

<kbd>Input</kbd>

```python
def palin_str(s):
	inp=s
	strs=inp[::1]
	rev=strs[::-1]
	if strs==rev:
		return "%s is a Palindrome string"%inp
	else:
		return "%s is not a Palindrome string"%inp

print(palin_str(input('Enter a string: ')))
```

<kbd>Output</kbd>

```python
Enter a string: eye
eye is a Palindrome string
```


[Download](py/palindrome_string.py)

or

[Try it online!](https://tio.run/##dY4xC8IwEIXn5FcchdJmcBC3QEZ3dxEp9KqBeg25q9BfHy86OIjbe/e@97i0yX2hQykjTpCGOdKVJffsvDWRUmBr1HNQffZ@f7Em4zPUk9pd9XGCNxE00JLmsmaCpmWIDAOc6uiYlwdWLtKtaXXMGpwZf3la5H/HJtXSf9/U4yp9dyTBrLUP66FzzpWCG74A "Python 3 – Try It Online")
