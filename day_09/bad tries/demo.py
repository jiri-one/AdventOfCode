def factorial(x):
	if x == 0:
		return 1
	elif x > 0:
		return x * factorial(x - 1)

print(factorial(5))