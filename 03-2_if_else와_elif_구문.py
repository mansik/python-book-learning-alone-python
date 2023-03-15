# 03-2 if~else와 elif 구문

# else 조건문의 활용

# 짝수와 홀구 구분하기
number = input("input decimal>")
last_number = int(number[-1])  # 마지막 자리 숫자 추출

## 방법 1.
if (last_number == 0 or
    last_number == 2 or
    last_number == 4 or
    last_number == 6 or
    last_number == 8):
    print("짝수입니다.")
else:
    print("홀수입니다.")

## 방법 2. in 문자열 연산자 활용, 방법 3의 숫자 연산보다 속도가 느림
if last_number in "02468":
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 방법 3. 나머지 연산자를 활용, 숫자 연산으로 속도가 빠름
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# elif 구문

# 계절 구하기
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("봄입니다.")
elif 6 <= month <= 8:
    print("여름입니다.")
elif 9 <= month <= 11:
    print("가을입니다.")
else:
    print("겨울입니다.")


# if 조건문을 효율적으로 사용하기
score = float(input("input score> "))

# 비효율적인 조건문
if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5: # 위에서 이미 제외된 조건을 한 번 더 검사하고 있다.
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자")
else:
    print("일반인")

# 효율적인 조건문: 앞 단계 조건문에서 비교한 것을 다음 단계에서는 제외시킨다.
if score == 4.5:
    print("신")
elif 4.2 <= score:  # 위에서 이미 제외된 조건을 한 번 더 검사할 필요가 없다.
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
else:
    print("일반인")


# False로 반환되는 값: None, 0, 0.0, 빈 컨테이너(빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)
# 이 외에는 모두 True

print("# False로 반환되는 값")
if 0:
    print("0은 True로 반환된다.")
else:
    print("0은 False로 반환된다.")

if "":
    print("빈 문자열은 True로 반환된다.")
else:
    print("빈 문자열은 False로 반환된다.")

if []:
    print("[]은 True로 반환된다.")
else:
    print("[]은 False로 반환된다.")


# pass 키워드: '아무것도 안함' 또는 '미 구현상태임'를 나타냄
number = int(input("input decimal> "))

# if number > 0:
#  여기에 아무 것도 없으면 IndentationError 발생한다.
# else:
#  여기에 아무 것도 없으면 IndentationError 발생한다.

if number > 0:
    pass
else:
    pass

# raise NotImplementedError: 미구현 에러라고 오류를 발생시킨다.
# : pass 키워드를 입력해놓고 추후 잊어버리고 구현을 하지 않은 경우 찾기가 쉽지 않다. 
# : 이런 경우 "아직 구현하지 않은 부분입니다.!!"라는 오류를 강제로 발생시켜 구현을 유도하기 위해 사용한다.

if number > 0:
    # 양수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
else:
    # 음수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError


# 배수 구하기

# 3의 배수: 각 자리 숫자의 합이 3의 배수인 경우
# 4의 배수: 십의 자리까지의 숫자가 4로 나누어 떨어지는 경우
# 5의 배수: 마지막 자리 숫자가 0 또는 5로 끝나는 경우
# 6의 배수: 짝수이면서, 각 자리의 숫자의 합이 3의 배수인 경우
# 9의 배수: 각 자리의 숫자의 합이 9의 배수인 경우
# 10의 배수: 마지막 자리 숫자가 0으로 끝나는 경우

