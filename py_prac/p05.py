print("파이썬")

print('Python')  

 

print("내 이름은 '홍길동'이야!")

print('내 이름은 "홍길동"이야!')


print("""큰따옴표 3개는

여러 줄의 문자열을 표현할 때

사용합니다.""")  

 
#여러 줄의 문자열 표현하기

print('''작은따옴표 3개도

여러 줄의 문자열을 표현할 때

사용합니다.''')  

 

print('여러 줄의 문자열을\n'

'개행문자를 사용하여 표현하는 것이\n'

'소스코드의 가독성은 더 좋습니다.')

#문자열끼리의 연산
i = "파이썬 "

j = "문자열"  

 

print(i + j)

print(i * 3)

#문자열에서 문자선택
py = "파이썬으로 코딩을 배우자!"  

print(py[0])

print(py[6])

print(py[-1])

print(len(py))

# 문자열 자르기
py = "우리집 강아지 이름은 멍멍이입니다."  

 
print(py[4])

print(py[4:7])

print(py[:4])

print(py[4:])

#특정 문자의 개수 및 위치
py = "python programming"  

print(py.count('p'))   

print(py.find('o'))

print(py.index('o'))  

print(py.find('z'))

# print(py.index('z'))

#대소문자 변환
py = "Python"  

 

print(py.upper())

print(py.lower())  

 

print(py)

#문자열 변경
py = "파이썬 공부는 너무 재밌어요!"  

 

print(py.replace("파이썬", "자바"))

print(py)

#문자열 나누기
py = "파이썬 공부는 너무 재밌어요!"  

 

print(py.split(' '))

print(py.split())  

 

print(py)