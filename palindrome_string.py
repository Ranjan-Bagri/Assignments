def palin_str(s):
	inp=s
	strs=inp[::1]
	rev=strs[::-1]
	if strs==rev:
		return "%s is a Palindrome string"%inp
	else:
		return "%s is not a Palindrome string"%inp

print(palin_str(input('Enter a string: ')))