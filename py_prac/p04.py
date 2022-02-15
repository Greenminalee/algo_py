primes = [2, 3, 5, 7]  

 

for p in primes:

    print(p)  

print(len(primes))

print(primes[1])

list1 = [1, 2, 3, 4, 5]  

 

print(list1[3])

print(list1[1:3])

print(list1[:3])

print(list1[3:])

print(list1)


 

copy = list1

copy.append(6)  

 
print(copy)
print(list1)

copy = list1[:]

copy.append(7)
print(copy)
print(list1)


# 리스트끼리 연산
list1 = [1, 2, 3]

list2 = list((4, 5, 6))

 

print(list1 + list2)

print(list1 * 3)  

 

list1.extend(list2)

print(list1)

list1 = [1, 2, 3, 4, 5]  


list1.remove(2)

print(list1)


list1 = [1, 2, 3, 4, 5]  

 

list1.insert(3, 9)

print(list1)  

 

list1.pop(4)

print(list1)

list1 = [1, 2, 3, 4, 5]
list2 = [3, 1, 4, 5, 10]
list1.reverse()
print(list1)
list2.sort()
print(list2)

#중첩 리스트
matrix = [[1, 2, 3], ["하나", "둘", "셋"]]  

 

print(matrix[0])
print(matrix[0][0])
print(matrix[1][2])