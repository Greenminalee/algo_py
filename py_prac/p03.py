i = 1

while i < 11: # 조건식

    print("파이썬 " + str(i))

    i = i + 1 # 탈출 조건


str = "helloWorld"

for ch in str:
	print(ch, end='')

for i in range(1, 10):
	if (i == 9):
			break
	for j in range(2, 9):
		if (j == 5):
			continue
		print(i , " x " , j , " = " , i * j)