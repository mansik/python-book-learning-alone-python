# 02-3 변수와 입력
# 변수 선언, 변수 할당, 변수 참조, input(), int(), float(), str()

# 변수 선언과 할당
pi = 3.14
r = 10 

# 변수 참조
print(pi)
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)

# 복합 대입 연산자 : +=, -=, *=, /=, %=, **=, //=
number = 100
number += 5
number -= 5
number *= 2
number /= 2
number %= 3
number **= 2
number = 3
number //= 2

print("number //= 2", number)

# 문자열의 복합 대입 연산자 : +=, *=
string ="안녕하세요"
string += "!"
string *= 3
print("string:", string)

# input() : 사용자 입력, 입력받은 값의 자료형은 문자열 자료형이다.
string = input("인사말을 입력하세요> ")
print(string)
print(type(string))

number = input("숫자을 입력하세요> ")
print(number)
print(type(number))

boolean = input("input True/False> ")
print(boolean)
print(type(boolean))

# 입력받고 더하기
string = input("input number> ")
# print("input + 100:", string + 100) # input()를 통해 입력받은 값은 문자열 + 숫자는 오류 발생한다.
# 그래서 int(), float()으로 숫자형으로 형 변환을 해줘야 한다.
print("input + 100:", int(string) + 100)


# int(), float() 활용
a = int("52")
b = float("52.12")
print(type(a), a)
print(type(b), b)

# ValueError 예외 발생
# 1. 숫자가 아닌 것을 숫자로 변환하려고 할 때 
# c = int("hi") # ValueError
# d = float("hi") # ValueError

# 2. 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때
# e = int("2.25") # ValueError


input_a = float(input("1st number> "))
input_b = float(input("2st number> "))
print("+:", input_a + input_b)
print("/:", input_a / input_b)

# str() 활용
a = str(52)
b = str(52.111)
print(type(a), a)
print(type(b), b)