fib = [0, 1, 1]

n = input()
k = input()

n = int(n)
k = int(k)

for i in range(3, n + 1):
	fibR = fib[i - 2] * k + fib[i - 1]
	fib.append(fibR)

print(fib[n])