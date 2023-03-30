# 04-1 리스트와 반복문
# 리스트, 요소, 인텍스, 리스트 슬라이싱,  for 반복문

# 리스트 선언하고 요소에 접근하기
# [1, 2, 3, 4]
# [273, "문자열", True, False]

list_a = [273, 32, 103, "문자열", True, False]
# 0번 인덱스의 요소
print(list_a[0])
# 1번 인덱스의 요소
print(list_a[1])

print(list_a[2])

# 리스트 슬라이싱
print(list_a[1:3])

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[0:5:2])  # 인덱스 0~ 4(=5-1)까지 2만큼의 인덱스를 건너뛴다.
print(numbers[::-1])  # 반대로 출력

# 요소 변경
list_a[0] = "변경"
print(list_a)

# 뒤에서 부터 요소를 선택
print(list[-1])
print(list[-2])

# 리스트 접근 연산자를 이중으로 사용하여 접근
print(list_a[3])
print(list_a[3][0])  # "문"

# 리스트 안에 리스트 사용
list_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_b[1])
print(list_b[1][1])

# 리스트에서 IndexError 예외
list_a = [1, 2, 3]
# list_a[3]  # IndexError 예외 발생

# 리스트 연산하기: 연결(+), 반복(*), len()
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)

print("# 리스트 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

print("# 리스트 길이 구하기")
print("len(list_a) =", len(list_a))

# 리스트에 요소 추가하기: append(), insert()
list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

print("# 한번에 여러 요소 추가하기")
list_a = [1, 2, 3]
list_a.extend([4, 5, 6])
print(list_a)


# 리스트 연결 연산자(비파괴적)와 요소 추가(파괴적)의 차이
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# 리스트 연결 연산자는 원본에 영향을 주지 않는다")
print("list_a + list_b =", list_a + list_b)
print("list_a =", list_a)
print("list_b =", list_b)

print("# 요소 추가의 경우 원본이 변경된다.")
list_a.extend(list_b)
print(list_a)
print(list_b)

# 리스트 연결 연산자와 같이 원본에 영향을 주지 않는 것을 "비파괴적"이라고 표현하고
# append(), insert(), extend() 함수와 같이 리스트에 직접적인 영향을 주는 함수 또는 연산을 "파괴적"이라고 표현한다.

# 원래 자료는 비파괴적으로 사용하는 것이 편리하다.
# 비파괴적으로 사용하면 원본도 활용하고, 새로운 결과도 활용할 수 있으므로 선택지가 더 넓기 때문이다. 
# 그래서 기본 자료형(숫자, 문자열, 불)과 관련된 모든 것들은 비파괴적으로 작동한다.
# 하지만 리스트는 용량이 매우 커질 수도 있다. 
# 용량이 얼마나 큰지도 모르는 "원본과 결과"라는 두 가지로 생성하는 것은 위험할 수도 있기 때문에 이러한 위험을 피하는 것이다.

# 리스트에 요소 제거하기(인덱스 또는 값으로 제거하기)
## 인덱스로 제거하기: del 키워드, pop()
list_a = [0, 1, 2, 3, 4, 5]

del list_a[1]
print("del list_a[1]:", list_a)

list_a.pop(2)
print("pop(2):", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print("del list_b[3:6]:", list_b)

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print("del list_c[:3]", list_c)

## 값으로 제거하기: remove()
list_c = [1, 2, 1, 2] 
list_c.remove(2)  # 먼저 발견되는 값 하나만 제거된다.
print("list_c.remove(2):", list_c)

## 모두 제거하기: clear()
list_c.clear()
print("list_c.clear()", list_c)

# 리스트 정렬하기: Sort()
list_e = [22, 23, 21, 67, 66, 2, 1]
list_e.sort()
print(list_e)

list_e.sort(reverse=True)
print(list_e)

# 리스트 내부에 있는지 확인하기: in/not in 연산자
list_a = [23, 44, 65, 32]
print(44 in list_a)
print(12 in list_a)

print(65 not in list_a)
print(12 not in list_a)

# for 반복문
for i in range(100):
    print(i, "번")

array = [22, 32, 42, 55, 102, 60]
for element in array:
    print(element)

for char in "안녕하세요":
    print(char)

# 중첩 리스트와 중첩 반복문
# 1차원 리스트: [1, 2, 3]
# 2차원 리스트: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## 2차원 리스트에 반복문 사용하기
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

print("# 2차원 리스트에서 반복문 사용하기")
for items in list_of_list:
    print(items)

for items in list_of_list:
    for item in items:
        print(item)


# 전개 연산자: *
# *리스트 = 리스트[0], 리스트[1], ...
# 전개 연산자는 
# 1. 리스트 내부, 
# 2. 함수의 매개변수 위치에 사용한다.

print("# 전개 연산자 *")
## 첫째, 리스트 내부에서 사용하는 경우
a = [1, 2, 3, 4]
b = [*a, *a]
print(b)

### 전개 연산자를 사용하면 리스트에 요소를 추가할 때 비파괴적으로 구현할 수 있다.
b = [1, 2, 3, 4] 
c = [*b, 5]
print(b)
print(c)

## 둘째, 함수 매개변수 위치에 사용하는 경우
a = [1, 2, 3, 4]
print(*a)
