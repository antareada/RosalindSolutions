bigRabbits = [0, 1, 1]
smallRabbits = [1, 0, 1]
mortalRabbits = []

n = input()
m = input()

n = int(n)
m = int(m)
print(n, '\n', m)

def countRabbits(rabbits):
	for i in range(3, n + 1):
		R = rabbits[i - 2] + rabbits[i - 1]
		rabbits.append(R)

def mortal(mortalRabbits):
	for k in range(0, n):
		kf = smallRabbits[k]
		if (k + m) <= n:
			j = 1
			for i in range(k + m + 1, n + 1):
				mortal = bigRabbits[i - 1] - bigRabbits[j] * kf
				mortalRabbits.append(mortal)
				j += 1

countRabbits(bigRabbits)

mortalRabbits = bigRabbits[0:m]
print('mortalRabbits:\n', mortalRabbits)

countRabbits(smallRabbits)
mortal(mortalRabbits)

print('bigRabbits:\n', bigRabbits)
print('smallRabbits:\n', smallRabbits)
print('mortalRabbits:\n', mortalRabbits)

