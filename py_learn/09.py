# https://www.acmicpc.net/problem/2588

n1 = int(input())
n2 = int(input())	

n3 = n1 * int((n2 % 10))
n4 = n1 * int((n2 % 100) / 10)
n5 = n1 * int((n2 % 1000) / 100)

print(n3)
print(n4)
print(n5)
print(n5 * 100 + n4 * 10 + n3)
