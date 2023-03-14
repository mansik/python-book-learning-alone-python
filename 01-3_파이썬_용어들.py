# 01-3 파이썬 용어들
## 표현식, 키워드, 식별자, 주석, print()


# 문장(statement): 실행할 수 있는 코드의 최소 단위를 문장(statement)라고 한다.
a = 10 + 20 # 문장
print("Python") # 문장


# 표현식(expression): 어떠한 값을 만들어 내는 간단한 코드를 표현식(expression)이라고 한다. 숫자, 수식, 문자열등
273
10 + 20 + 30
"python programming"


# 키워드(keyword): 특별한 의미가 부여된 단어로, 파이썬의 예약어
import keyword
print(keyword.kwlist)

# 'False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 
# 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
# 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'

## 파이썬은 대소문자를 구분한다.


# 식별자(identifier): 이름을 붙일 때 사용하는 단어, 주로 변수나 함수 이름등으로 사용한다.

## 식별자 작성 규칙 ##
### 키워드는 사용하면 안된다.
### 특수 문자는 언더 바(_)만 허용한다.
### 숫자로 시작하면 안된다.
### 공백을 포함할 수 없다.

# snake_case와 CamelCase: 파이썬에서 식별자를 만드는 방법
## snake_case: 모두 소문자로 단어와 단어사이에 _ 기호를 붙여 식별자를 만든다. item_list, login_status, 변수 또는 함수
## CamelCase(UpperCamelCase): 단어들의 첫 글자를 대문자로 만들어 식별자로 만든다. ItemList, LoginStatus, 클래스

### 원래 CamelCase는 UpperCamelCase(첫 글자를 대문자로 적는다)와 lowerCamelCase(첫 글자를 소문자로 적는다)의 2가지 유형이 있다.
### lowerCamelCase : ItemList, LoginStatus => 파이썬에서 사용
### UpperCamelCase : itemList, loginStatus => PascalCase

## 식별자 구분하기
# CamelCase(UpperCamelCase) : 클래스에 사용(class Animal:, BeautifulSoup()), 클래스 생성자는 CamelCase이고 뒤에 괄호가 있다.
# snake_case: 변수(item_list), 함수(print())에 사용, 함수는 snake_case이고 뒤에 괄호가 있다.


# 주석(comment): 주석으로 처리하고자 하는 부분 앞에 # 기호를 붙인다. #기호와 문장은 1칸 뛰운다.
print(10+20) # 이것이 주석이다.
# 이것도 주석이다. 

# 연산자와 자료
## 연산자:  +, -, *, / 등
## 자료 또는 리터럴(literal): 1, 10, "Hello"등, 숫자이든지 문자이든지 어떠한 값 자체를 의미한다. 변하지 않는 값을 의미


# 출력: print()
print() # 줄바꿈
print("100") # 1개의 값을 출력
print(10, 255) # 여러개의 값을 출력
print(10, 255, "Hello", True) # 여러개의 값을 출력
# 문자열 보간(interpolation) 사용
print('The value of pi is approximately %5.3f.' % 3.14159)
