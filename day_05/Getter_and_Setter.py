def propetry():
    pass


class Person:
    def __init__(self, name):
        self.name = name
        self.__hp = 0
        # self.__hp = 0 는
        # private 처럼 사용할 수 있지만
        # 사실상 private 는 Python 에 없습니다.

    # Console.log 를 찍습니다.
    @property
    def hp(self):
        # 저런 자료형으로 바꾸어 줘야 합니다.
        print("get_hp " + str(self.__hp))
        return self.__hp

    @hp.setter
    def hp(self, num):
        # 정말 기분이 나쁘지만,
        # 꼭 str(self._변수이름) 형태로
        # 작성해야 합니다.
        self.__hp = num
        print("set_hp " + str(self.__hp))


human = Person("Your name ")
print(human.name)
# human.set_hp(1)
# print(human.get_hp())
print(human.hp)
human.hp = 10
print(human.hp)

# private 속성 안에 있는 목록인 __hp 를 출력합니다.
print(human._Person__hp)