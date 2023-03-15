# 03-1 불 자료형과 if 조건문
# 불, 비교 연산자, 논리 연산자, if 조건문

# Boolean, 불, 불리언: True, False
print(True)
print(False)

# 불 만들기: 비교 연산자(==, !=, <, >, <=, >=)
print("# 숫자 비교")
print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)


print("# 문자열 비교")

print("가방" == "가방")
print("가방" != "하마")
print("가방" < "하마")
print("가방" > "하마")

# 불 연산하기: 논리 연산자(not, and, or)
print("# 불 연산하기: 논리 연산자(not, and, or)")

print(not True)
print(not False)

# not 연산자 조합하기
x = 10
under_20 = x < 20
print("under_20:", under_20)
print("not under_20:", not under_20)

# and 연산자와 or 연산자
print(True and True)  # True
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)  # False

# if 조건문
print("# if 조건문")

if True:
    print("This is True.")
    print("This is Real True.")

# 조건문의 기본 사용
number = input("input decimal> ")
number = int(number)

if number < 0:
    print(f"{number} is posigive")
elif number > 0:
    print(f"{number} is negative")
else:
    print("This is 0")


# 날짜/시간 활용하기
import datetime

# 현재 날짜/시간을 구한다.
now = datetime.datetime.now()

## 날짜/시간 출력하기
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

## 오전/오후를 구분하는 프로그램
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.".format(now.hour))
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))

## 계절을 구분하는 프로그램
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))

if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

