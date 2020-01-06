class Monster:
    Hp = 0
    level = 0

    def name(self):
        print("Oak Name")


class Oak(Monster):
    def OakAttack(self):
        print("Oak Attack")


class UglyOak(Oak):
    def UglyOakAttack(self):
        print("Ugly Oak Attack")


if __name__ == "__main__":
    oak1 = Oak()
    oak1.name()
    oak1.OakAttack()
    oak2 = UglyOak()
    oak2.name()
    oak2.OakAttack()
    oak2.UglyOakAttack()
