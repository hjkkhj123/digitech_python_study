# 인자 Keyword 식 사용하기
def func1(a, b=0, c=1):
    print(a)
    print(b)
    print(c)


# Tuple 형태로 Default 인자(a, b)와 Keyword 인자(*args) 를 Tuple 형태로 입력 및 출력합니다.
# *args 는 Default 인자(a, b)이외에도 입력되는 값들을 (*args) 형태로 입력 및 출력합니다.
def func2(a, b, *args):
    print(*args)


# **kwargs 는 *args 와 비슷하지만, Dictionary 형태로 값을 입력 및 출력합니다.
def func3(a, b, **kwargs):
    print(kwargs)


func1(123, c=123)
func1(1233, b=123)
func2(123, 1234, 56, 78)
func3(123, 456, c=7, d=8, e=9)


def a(first, second, func):
    print(func(first, second))


def plus(first, second):
    return first+second


a(1, 2, plus)


# Python Closer
def hello(user):
    def deco(msg):
        return "receive msg: " + msg

    return deco


a = hello('hi')
print(a)
b = hello("hello")
print(b)


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(11))

# global 은 전역변수를 함수 내에서 값을 바꾸려고 할 때
# 하단에 나온 형태처럼 코딩합니다.
hi = "hi"


def test():
    global hi
    print(hi)


def plus(a, b):
    try:
        c = a+b
        print(c)
    except Exception as e:
        print(e)
    finally:
        print("Finally, the program has finished")


plus(1, '3')
plus(1, 2)
