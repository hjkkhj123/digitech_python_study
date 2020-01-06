a = 7
print(type(a))
a += 0.1
print(type(a))
a = str(a) + "b"  # 새로 알게 된 방법
print(type(a))

a = 10
print(bin(a))
print(0b10)
print(oct(a))
print(0o10)
print(hex(a))
print(0x10)

a = "10"
a = int(a)
a += 0.0  # float 에서 int 로 바꾸는 법
print(type(a))

a = 10
b = 7
c = 3

print(a, b, c)
a, b, c = b, a, c
print(a, b, c)

# a = "123"
# b = 3
# c = a * 3
# a = "456"
# b *= 3
# print(c)
# print(b)

a = 1
b = 3
c = (a, b)
d = c * 3
print(d)

string = "seoul digitech high school"
print(string[-11:-7])
print(string[-6:])
print(string[6:14])
print(string[0:10:1])  # 0 ~ 10까지 1칸씩 출력
print(string[a::-1])
print(len(string))
print(string.split())

a = [1, 2, 3, 4, 5]
b = (1, 3, 5)
b = list(b)
b += [2, 4]  # append 와 같다고 생각할 수 있지만 다릅니다.
# append 는 원소 하나하나가 객체로 인식하므로, "변수 += [원소 목록]" 과 다릅니다.
# b.append([2, 4])
# b.append((2, 4))
print(type(b))
print(b)
del a[2]  # 원하는 수를 지워줍니다.
print(a)
print((2, 4) in b)  # 값이 있는지 알려줍니다.
print(b.count(3))

c = ['1', '3', '2']
print(",".join(c))  # '' 뿐만 아니라 []까지 없애주는 신기한 기능!! 지금 바로 파이썬을 하세요 (광고 아님)
b.sort()
print(b)
c.sort()
print(c)

a1 = [1, 2, 3]
print(a1)
b = a1.copy()
# b = a1
print(b)
a1[0] = 4
print(b)
