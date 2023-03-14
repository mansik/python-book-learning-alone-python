# 02-4 숫자와 문자열의 다양한 기능 : foramt(), upper(), lower(), strip(), find(), in 연산자, split(), f-문자열

# foramt() 함수 : 1. 숫자를 문자열로 변환{}, 2. 정수로 변환 {:d}, 3. 부동 소수점 형태로 변환 {:f}
# 문자열의 format() 함수
"{}".format("문자열")
"{}".format(10)
"{}{}".format(10, 20)
"this is {0} and {1}".format(10, 20)
"this is {1} and {0}".format(10, 20)
'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg')
"this is '{0:5}' and '{1:5}'.".format(1, "문자열") # 5칸을 생성후 format()의 인자값이 숫자이면 오른쪽 정렬, 문자이면 왼쪽정렬
"this is '{0:5}' and '{1:5}'.".format("1", "문자열") # 5칸을 생성후 format()의 인자값이 숫자이면 오른쪽 정렬, 문자이면 왼쪽정렬

# format() 함수로 문자열을 표현
print("'{:10}' 와 '{:10}'".format(123, "문자열")) #10칸을 생성후 format()의 인자값이 숫자이면 오른쪽 정렬, 문자이면 왼쪽정렬
print("'{:10}' 와 '{:10}'".format("123", "문자열")) #10칸을 생성후 format()의 인자값이 숫자이면 오른쪽 정렬, 문자이면 왼쪽정렬

# format() 함수로 숫자를 문자열로 변환
a = "{}".format(10)
print(type(a), a)

# format() 함수의 다양한 형태
a = "{}만 원".format(50_000)
b = "파이썬 열공하여 연봉 {}만 원 만들기".format(5000)
c = "{} {} {}".format(1000, 2000, 3000)
d = "{} {} {}".format(1, "문자열", True)
e = "this is {0} and {1} and {2}".format(1, "문자열", True)
f = "this is {2} and {1} and {0}".format(1, "문자열", True)
g = "this is '{0:5}' and '{1:5}'.".format(1, "문자열") # 5칸을 생성후 format()의 인자값이 숫자이면 오른쪽 정렬, 문자이면 왼쪽정렬
h = "this is '{0:5}' and '{1:5}'.".format("1", "문자열") # 5칸을 생성후 format()의 인자값이 숫자이면 오른쪽 정렬, 문자이면 왼쪽정렬

print("# format() 함수의 다양한 형태")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


# IndexError 예외
"{}{}".format(1, 2, 3, 4) # 오류발생 안함, 결과 : 1, 2
# "{}{}{}".format(1, 2) # IndexError 예외 발생

# format() 함수의 다양한 기능
# 정수 {:d}, 부동 소수점 : {:f}

# 정수
a = "{:d}".format(52) 

# 특정 칸에 출력
b = "{:5d}".format(52) # 5칸을 만들고 format()의 인자값이 숫자이므로 오른쪽에 정렬,"   52"
c = "{:10d}".format(52) # 10칸을 만들고 format()의 인자값이 숫자이므로 오른쪽에 정렬,

# 빈칸을 0으로 채우기
d = "{:05d}".format(52) 
e = "{:05d}".format(-52) # 음수

print("# format() 함수의 다양한 기능")
print("# {:d}.format(52)")
print(a)
print("# 특정 칸에 출력")
print(b)
print(c)
print("# 빈칸을 0으로 채우기")
print(d)
print(e)


# 기호와 함께 출력하기
print("# 기호와 함께 출력하기")
print("{:+d}".format(52), "{:+d}.format(52)") # "+52"
print("{:+d}".format(-52)) # "-52"
print("{: d}".format(52), "{: d}") # " 52", 양수일 경우 기호 부분 공백
print("{: d}".format(-52)) # "-52"
print("{:+5d}".format(52), "{:+5d}") # "  +52"
print("{:+5d}".format(-52)) # "  -52"
print("{:+05d}".format(52), "{:+05d}") # "+0052", 빈칸을 0으로 채움
print("{:+05d}".format(-52)) # "-0052"
print("{:=+5d}".format(52), "{:=+5d}") # "+  52", 기호를 맨앞에 표시
print("{:=+5d}".format(-52)) # "-  52", 기호를 맨앞에 표시


# 부동 소수점 출력의 다양한 형태, 소수점이하 6자리를 보여줌
print("{:f}".format(52.273), "{:f}") # "52.273000"
print("{:15f}".format(52.273), "{:15f}") # "      52.273000"
print("{:+15f}".format(52.273), "{:+15f}") # "     +52.273000"
print("{:+015f}".format(52.273), "{:+015f}") # "+0000052.273000"

# 소수점 아래 자리수 지정하기
print("{:15.3f}".format(52.273), "{:15.3f}") # "         52.273", 15칸을 만들고, 그안에 소수점자리 3자리까지 표현
print("{:15.1f}".format(52.273), "{:15.1f}") # 15칸을 만들고, 그안에 소수점자리 1자리까지 표현
print("{:15.0f}".format(52.273), "{:15.0f}") # 15칸을 만들고, 그안에 소수점자리 0자리까지 표현
print("{:.3f}".format(52.273), "{:.3f}") # "52.273", 소수점자리 3자리까지 표현


# 의미 없는 소수점 제거하기
print("{:g}".format(52.0), "{:g}")
print("{:g}".format(52.10))



# 대소문자 바꾸기: upper(), lower(), 비파괴적 함수(원본은 바뀌지 않는다.)
a = "Hello Python!!"
b = a.upper()
print("a:", a)
print("b:", b)

c = a.lower()
print("a:", a)
print("c:", c)
print(a.lower())


# 문자열 양옆의 공백 제거하기: strip(), lstrip(), rstrip(), 비파괴적 함수
a = """
안녕하세요
문자열 입니다
"""
print("-"*10)
print(a)
print("-"*10)
b = a.strip()
print(a)
print("-"*10)
print(b)
print("-"*10)


# 문자열의 구성 파악하기: isXX() , 결과는 True, False
# isalnum(): 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인한다.
# isalpha(): 문자열이 알파벳으로만 구성되어 있는지 확인한다.
# isidentifier(): 문자열이 식별자로 사용할 수 있는 것인지 확인한다.
# isdecimal(): 문자열이 정수 형태인지 확인한다.
# isdigit(): 문자열이 숫자로 인식될 수 있는 것인지 확인한다.
# isspace(): 문자열이 공백으로만 구성되어 있는지 확인한다.
# islower(): 문자열이 소문자로만 구성되어 있는지 확인한다.
# isupper(): 문자열이 대문자로만 구성되어 있는지 확인한다.

print("TrainA10".isalnum())
print("10".isdigit())

# 문자열 찾기: find(), rfind()
## find(): 왼쪽부터 처음 등장하는 위치를 찾는다.
## rfind(): 오른쪽부터 찾아서 처음 등장하는 위치를 찾는다.

a = "안녕안녕하세요".find("안녕")
print(a)

b = "안녕안녕하세요".rfind("안녕")
print(b)

# 문자열과 in 연산자 : a in b, a가 b에 존재하면 True, 없으면 False
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")

# 문자열 자르기: split(), 결과는 list
a = "10 20 30".split(" ") #  공백(" ")으로 문자열을 자르기
print(a)

# f-문자열: format string

# 문자열 연결 연산자 + 사용
a = "3 + 4 = " + str(3+4)
print(a)

# format() 함수 사용
a = "3 + 4 = {}".format(3+4)
print(a)

# 문자열 보간(interpolation) 사용
print('The value of pi is approximately %5.3f.' % 3.14159)
print('The value of pi is approximately %d.' % 59)

# f-문자열(f-string, Formatted string literals) 사용: f'문자열{표현식}문자열', 파이썬 3.6부터 사용
"{}".format(10) # format() 함수 사용

f'{10}' # f-문자열 사용
f"3 + 4 = {3 + 4 }"
f"""1 + 2 = {1 + 2}
2 + 3 = { 2 + 3}
3 + 4 = { 3 + 4}"""

print(f'{10}')
print(f"3 + 4 = {3 + 4}")
print(f"""1 + 2 = {1 + 2}
2 + 3 = { 2 + 3}
3 + 4 = { 3 + 4}""")

# f-문자열보다 format() 함수를 사용하는 것이 더 좋은 경우
# 첫째, 문자열 내용이 너무 많을 때
name = "구름"
age = 7
print("""문자열이 너무 긴 경우
데이터 {}을 출력해야 하는 경우가 있다.

이때 f-문자열을 사용하면
어떤 위치에 어떤 데이터 {}가 출력되는지 확인 하기 위해서
문자열 전체를 읽어야 하는 문제가 있다.
이러한 경우 format() 함수를 사용하는 것이 편리하다.
문자열이 아무리 길어도 format() 내의 인자만 보면
어떤 데이터를 출력하는지 쉽게 알 수 있다.
""".format(name, age))

# 둘째, 데이터를 리스트에 담아서 사용할 때
data = ['별', 2, 'M', '서울특별시 강서구', 'Y']

print(f"""이름: {data[0]}
나이: {data[1]}
성별: {data[2]}
지역: {data[3]}
중성화 여부: {data[4]}
""") # f-문자열일 경우 일일이 리스트 요소에 접근해야 한다.

## 위치인자를 unpacking 하는 경우는 *를, 키워드인자를 unpacking하는 경우 **를 사용한다.
## 위치인자로는 list, tuple, set등 Container 객체가 올 수 있고,
## 키워드인자로는 key와 value로 되어 있는 매핑패턴의 dictionary가 있다.
print("""이름: {}
나이: {}
성별: {}
지역: {}
중성화 여부: {}
""".format(*data)) # 인자에 있는 *는 위치인자를 unpacking하며, list, tuple, set등 Container 객체에 사용

dict = {"name": "별", "age": 2, "sex": "M", "addr": "서울특별시 강서구", "neutered": "Y"}

print("""이름: {name}
나이: {age:3d}
성별: {sex}
지역: {addr}
중성화 여부: {neutered}
""".format(**dict)) # 인자에 있는 **는 키워드인자를 unpacking하며, key와 value로 되어 있는 매핑패턴의 dictionary에 사용

print("""이름: {}
나이: {}
성별: {}
지역: {}
중성화 여부: {}
""".format(*dict)) # 인자에 있는 *는 위치인자를 unpacking하며, dictionary에 사용할 경우 key를 대입한다.