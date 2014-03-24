bigRabbits = [0, 1, 1]
smallRabbits = [1, 0, 1]
lists = []
lists.append(bigRabbits)


n = input()
m = input()

n = int(n)
m = int(m)
print(n, '\n', m)

def countRabbits(rabbits):
	for i in range(3, n):
		R = rabbits[i - 2] + rabbits[i - 1]
		rabbits.append(R)

def mortal(m, lists):
	for i in range(0, n):
		j = 1  # количество итераций по вычитанию одного списка
		while j <= smallRabbits[i]:
			listTemp = listNull
			listTemp[m + i + 1:n] = bigRabbits[m + i + 1:n]
			lists.append(listTemp)
			j += 1

countRabbits(bigRabbits)
countRabbits(smallRabbits)

listNull = []
for i in range(0, n):
	listNull.append(0)


print(listNull)

print('bigRabbits:\n', bigRabbits)
print('smallRabbits:\n', smallRabbits)


mortal(m, lists)
for i in range(0, n):
	print(lists[i])