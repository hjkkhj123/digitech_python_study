# import sys
#
# # first_num = sys.argv[1]
# second_num = sys.argv[2]
# # sum = int(first_num) + int(second_num)
# print(second_num)
import numpy as np
from numpy import sum as npsum
import sys
list_test = [1, 2, 3, 4]
result = np.sum(list_test)
result_2 = npsum(list_test)
"""
    list_test 안에 있는 list 목록들의 합입니다.
    list_test 안에 총 4개의 목록(요소)가 있으며,
    각 목록에 들어 있는 1 + 2 + 3 + 4 들을 모두 합하면
    10 이 됩니다.
"""
print(result)
print(result_2)
print("\n\n\n\n")


class A:
    # 클래스 전역 변수 numbers
    numbers = 0
    
    # a 와 b 라는 변수를 name 과 age 라는 멤버 변수로 각각 초기화 시켜줍니다.
    def __init__(self, name, age):
        print("The Number is : {0} {1}".format(name, age))
        # print("The Number is : {0}".format(age))
        # 요기서 a 와 b 를 각각 name 과 age 라는 변수로 초기화 합니다.
        self.a = name
        self.b = age
        # numbers 라는 변수는 A 클래스 안에 포함되어 있으므로,
        # 객체를 생성하는 곳인 __init__ 에서 클래스 전역 변수인
        # numbers 의 값을 1씩 증가시켜줍니다.
        A.numbers += 1
        print("The Amount is : {0}".format(A.numbers))

    def __del__(self):
        """
            numbers 라는 변수는 A 클래스 안에 포함되어 있으므로,
            객체를 없애주는 __del__ 에서 클래스 전역 변수인
            numbers 의 값을 1씩 감소시켜줍니다.
        """
        A.numbers -= 1
        print("The Amount is : {0}".format(A.numbers))

    def func(self):
        # a 와 b 라는 변수에 현재 할당된 값을 출력합니다.
        print(self.a, self.b)


# 현재 순서는
# 1. def __init__(self, name, age):
# 2. def __del__ (self):
# 3. def func(self):

"""
    self.a 와 self.b 는 각각 name 과 age 라는 
    멤버 변수로 초기화 시켜준 것입니다.
"""
a = A("Kunwoo", 18)
# a.func()
