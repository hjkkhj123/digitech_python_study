class Person:
    age = ""
    address = ""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + Person.age + Person.address + "eat")

    def sleep(self):
        print(self.name + "sleep")

    def work(self):
        print(self.name + "work")


"""
    if __name__ == "__main__": 는
    굳이 중간중간에 하단과 같이 Class 이름을 호출하지 않고도
    
    모든 Class 가 끝나는 맨 마지막 줄에
    if __name__ == "__main__": 을 작성하여
    좀 더 편리하게 Class 들을 관리할 수 있습니다.
"""


# if __name__ == "__main__":
"""
    일일이 생성할 경우
    human = Person()
    human.name = "My name is" 
"""
human = Person("My name is ")
print(human.name)
human.work()
"""
    Getter 와 Setter 는 각 객체의 보안 문제를 해결하고자
    Get 과 Set 으로 보안적인 문제들을 해결합니다.
"""


class Programmer(Person):
    """
        참고로 이것도 주석입니다.
        이 주석은 C언어나 Java 에서는
        /*
        *
        */

        같은 것입니다.
    """
    # 자식 Class 가 다시 생성할 수 없지만,
    # super Class 를 사용한다면 가능합니다.
    def __init__(self, name, position):
        """
             Instance 화,
             현재 Programmer Class 는
             Person Class 로부터 상속을 받았고,
             미리 만들어 놓은 Class 를
             불러들여온 것이므로,

             Person.__init__(name) 이런식으로
             작성을 해야합니다.


             그리고 super 는 사용자가 만든 Class 들 중,
             가장 최상위 부모 객체 (Instance) 를 불러옵니다.
        """
        """
            --> ClassName.__init__() 는 이미 존재한 Class 를 불러들임 (Instance 가 아님)
            --> super.__init__() 는 이미 만든 Class 들 중, 가장 최상위 부모 객체에 놓여져 있는
                Class 를 불려들입니다. (Instance 화)
        """
        Person.__init__(name)
        super.__init__(name)
        self.position = position

    """
        Programmer Sleep 를 작성하면
        계속 불편하게 작성해야 하므로
        제거하겠습니다.
    """
    def ProgrammerSleep(self):
        pass

    def sleep(self):
        print(self.name + " over work.. He Said 'Shit!! I wanna go home!!'")


pp = Programmer("John")
"""
    일일이 생성할 경우
    pp = Programmer()
    pp.name = "John" 
"""

A = [pp, human]
pp.sleep()
