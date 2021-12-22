a = 0
b = 1
c = a + b
fibsize = int(input('Supply the Fibonacci serie size: '))
if fibsize == 1:
	print(a, end=' ')
elif fibsize == 2:
	print(a, end=' ')
	print(b, end=' ')
else:
	print(a, end=' ')
	print(b, end=' ')
	for k in range(1, fibsize-1):
	    print(c, end=' ')
	    a = b
	    b = c
	    c = a + b
print('')

