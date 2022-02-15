set1 = {1, 2, 3}

set2 = set("Python")

set3 = set("Hello")  

 

print(set1)

print(set2)

print(set3)

#빈 세트(empty set)
set1 = {}
set2 = set()  

print(type(set1))
print(type(set2))

#세트에 요소 추가하거나 제거하기
set1 = {1, 2, 3}  

set1.add(4)

print(set1)  

set1.update((5, 6))

print(set1)  

set1.remove(2)

print(set1)

#집합 연산
set1 = {1, 2, 3, 4, 5}

set2 = set((1, 3, 5, 7, 9))  

 

print(set1)

print(set2)  

 
print(set1 | set2) # 합집합

print(set1 & set2) # 교집합

print(set1 - set2) # 차집합

print(set1 ^ set2) # 여집합 = 합집합 - 교집합

