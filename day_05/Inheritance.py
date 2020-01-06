"""
    수업 시간엔 하지 않았지만 그래도 혹시 몰라서
    한 번 찾아본 코드입니다.

    번외편입니다. 참고용으로 사용하세요.
"""
# 다음 코드는 __new__가 사실은 생성자라는 것을 알려주게 됩니다.
# __new__ 는 동적으로 계속 생성해줄 수 있지만, __init__ 는 한 번만 생성을
# 할 수 밖에 없다는 것이 단점입니다.

# 그리고 이 Code 는 아래 Child 를 실행하기 전에
# Instance 가 만들어졌는지 확인하고, 만들어졌다면
# 하단의 오류와 같이 ValueError 를 발생시킵니다.


class Parent:
    x = None
    y = None
    MAX_Inst = 0
    Inst_Created = 0

    def __new__(cls, *args, **kwargs):
        if cls.Inst_Created >= cls.MAX_Inst:
            raise ValueError("Cannot create more objects because you already created it")
        elif cls.Inst_Created < cls.MAX_Inst:
            cls.Inst_Created += 1
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print("From Init")
        self.x = x
        self.y = y


class Child(Parent):
    def print_text(self):
        print("X 는 {0}, Y 는 {1}".format(Parent.x, Parent.y))


if __name__ == "__main__":
    c = Child()

