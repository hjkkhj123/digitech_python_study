class Parent:
    def name(self):
        pass


class Child(Parent):
    def age(self):
        pass


# Class 들을 호출할 때
# 굳이 if __name__ == "__main__":
# 적을 필요가 없습니다.

if __name__ == "__main__":
    p = Parent()
    p.name()
    c = Child()
    c.age()
    c.name()

# 위에 p = Parent() 와 c = Child() 는
# 각각의 Class 들의 내용들을 초기화시켜줍니다.

# 그러나 p 는 Parent() Class 의 내용이고,
# c 는 Child() Class 이며, Child() Class 는
# Parent() Class 로부터 상속을 받기 때문에
# C언어 또는 Java 구조처럼

# Parent p = new Child()
# 이런식으로 작성할 수 있게 되는 것입니다.
