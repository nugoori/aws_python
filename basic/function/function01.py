#def( define )
def add(x, y):
    result = x + y
    return result

# 매개변수의 이름을 명시하면 순서가 바뀌어도 상관없음
# r = add(y=20, x=10)

# 오버로딩 불가능 : 한 블럭씩 실행되고, 다음 블럭이 실행되면 이전 블럭은 정의X(인터프리터언어의 특징?)
# !! 매개변수, 여러개의 리턴은 튜플 자료형으로 정의된다 !!
def add(*a):
    print(type(a))
    return list(a), 10

# 튜플을 리스트로 형변환하여 사용가능
r = list(add(20, 10, 5, 30, 15))

print(r)

# **이면 딕셔너리 자료형으로 매개변수를 변환해준다
def sub(**data):
    print(type(data))
    print(data)
sub(a=1, b=2)

def sub(data):
    print(type(data))
    print(data)
sub({"a": 1, "b": 2})

def connection(servername, password, ip="127.0.0.1", port="8080", username="root"):
    # 초기값을 정하지 않은 매개변수는 초기값을 정한 매개변수의 앞으로 와야 함
    print(f"ip: {ip}")
    print(f"port: {port}")
    print(f"servername: {servername}")
    print(f"username: {username}")
    print(f"password: {password}")

connection(servername="test_server", password="1q2w3e4r", port="3306")

# < 함수 안에서 함수 밖의 변수 변경 >
a = 2

def multi(a):
    return a ** 2
a = multi(a)
print(a)

def div():
    global a    # 함수 밖의 전역 변수를 가져옴
    a = a * 10
div()
print(a)

    #람다식
def add(a, b):
    return a + b

print(add(10, 20))

# 파이썬에서 람다는 하나의 명령만 수행 할 수 있다( 여러 줄 작성 불가능 )
add = lambda a, b: print(a+b)
add(20, 30)
