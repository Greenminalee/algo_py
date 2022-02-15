# 딕셔너리 선언하기
dict1 = {'하나': 1, '둘': 'two', '파이': 3.14}

dict2 = dict({'하나': 1, '둘': 'two', '파이': 3.14})

dict3 = dict([('하나', 1), ('둘', 'two'), ('파이', 3.14)])

dict4 = dict(하나=1, 둘='two', 파이=3.14)


print(dict1)

print(dict2)

print(dict3)

print(dict4)


dict1 = {'하나': 1, 2: 'two', 3.14: 'pi'}

dict2 = {('ten', 10): ['열', 10.0]}


print(dict1)

print(dict2)

#딕셔너리 사용하기
dict1 = dict({'자바': 80, 'PHP': 90, 'HTML': 70})


print(dict1['자바'])

print(dict1.get('자바'))


# print(dict1['파이썬'])

print(dict1.get('파이썬'))

#딕셔너리에 요소 추가하거나 제거하기

dict1 = dict({'자바': 80, 'PHP': 90, 'HTML': 70})

dict1['파이썬'] = 100

print(dict1)


del dict1['PHP']

print(dict1)


dict1['자바'] = 100

print(dict1)


dict1.clear()

print(dict1)


#딕셔너리의 정보 얻기

dict1 = dict({'자바': 80, 'PHP': 90, 'HTML': 70})  

 

print(dict1.keys())

print(dict1.values())

print(dict1.items())  

 

print('HTML' in dict1)

print('파이썬' in dict1)

