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