# 02-1 자료형과 문자열
# 자료형, 문자열, 이스케이프 문자, 문자열 연산자, type(), len()
# 파이썬 기본 자료형 : 문자열(string), 숫자(int, float), boolean(True, False)

print("Hello Python!")
print('Hello Python!')
print(type("hello"))

print("Hi", "python")  # ','는 한칸 띄움
print("Hi", 'python', 10, 3.25, True, False) 

print("say 'Hi'")
print('say "Hi"')

# 이스케이스 문자(\) 사용
# \" : 큰따옴표
# \' : 작은 따옴표
# \n : 줄바꿈
# \t : 탭
# \\ : \

print("\"안녕하세요\"라고 말했습니다.")
print("안녕하세요!\n안녕하세요!")
print("안녕하세요\t안녕하세요")

print("\\ \\ \\ \\")

# 여러 줄 문자열 만들기
print("""동해물과 백두산이
마르고 닳도록
하느님이 보우하사""")

print("-" * 10)

# 위 아래 줄바꿈이 들어감
print("""
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
""")

print("-" * 10)

# """ 안에서 \는 줄바꿈을 하지 않겠다는 선언이다.
print("""\
동해물과 백두산이
마르고 닳도록
하느님이 보우하사\
""")

# 문자열 연산자 : 연결(+), 반복(*), 인덱싱([]), 슬리이싱([:])
# 문자열 연결 연산자 + 는 문자열 + 문자열이라야 한다. 
# 문자열 + 숫자 또는 boolean은 안된다.
print("안녕하세요" + "!")
# print("안녕하세요" + 1)  # TypeError : 문자열 + 문자열이라야 한다.

print("안녕하세요" * 3)

print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[-1])
print("안녕하세요"[-2])

print("안녕하세요"[1:4])
print("안녕하세요"[1:])
print("안녕하세요"[:4])
print("안녕하세요"[:])


# len()
print(len("ansaa"))
