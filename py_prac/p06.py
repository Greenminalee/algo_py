#튜플
tuple1 = (1, 2, 3)

tuple2 = 1, 2, 3


tuple3 = (1,)

tuple4 = (1)


print(tuple1)

print(tuple2)


print(tuple3)

print(tuple4)


tuple1 = (1, 2, 3)

tuple2 = tuple(["원", "투", "쓰리"])

 

# 튜플 요소 선택하기

print(tuple1[0])

print(tuple2[-1])  

 

# 튜플 자르기

print(tuple1[1:])

print(tuple2[:2])  

 

# 튜플끼리의 연산

print(tuple1 + tuple2)

print(tuple1 * 2)


#패킹 언패킹
# 패킹(packing)

tuple1 = 10, "열", True  

 

# 언패킹(unpacking)

a, b, c = tuple1

# a, b, c, d = tuple1

# a, b = tuple1  

 

print(a)

print(b)

print(c)  

#특정요소 포함여부
tuple1 = 10, "열", True  

 

print(10 in tuple1)

print("아홉" in tuple1)

print("아홉" not in tuple1)