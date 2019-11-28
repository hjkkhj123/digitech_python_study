# 빈 튜플 생성
e_t1 = ()
print(e_t1)

# 하나의 원소로 튜플 생성
e_t2 = 'dog',
print(e_t2)

# 여러개의 원소로 튜플 생성
e_t3 = 'dog', 'cat', 'bird'
print(e_t3)

# 튜플 언팩
a, b, c = e_t3
print(a)
print(b)
print(c)

# 튜플 언팩할 때 아래와 같이 _(UnderScore)를 사용한다면 그 원소를 무시하는 목적
d, e, _ = e_t3

# 리스트를 튜플로 변환하는 방법
e_l = [1, 2, 3]
e_t4 = tuple(e_l)
print(e_t4)

# 빈 딕셔너리 생성
dict_1 = {}
print(dict_1)

# 3개의 원소를 가지는 딕셔너리 생성
dict_2 = {"key": e_t4, "key2": e_t3, "key3": 777}
print(dict_2)

# 딕셔너리의 특정 키의 값을 변경
dict_2["key"] = 123
print(dict_2)

# 딕셔너리의 새로운 키와 값을 추가
dict_2["key4"] = 456
print(dict_2)

# 딕셔너리의 키 목록을 출력
dict_keys = dict_2.keys()
print(dict_keys)

# 딕셔너리의 여러개의 값을 한번에 수정
tmp = {"name": 888, "key2": 999}
dict.update(tmp)
print(dict_2)

# 딕셔너리의 특정 아이템 삭제
del dict_2["key2"]
print(dict_2)

# 딕셔너리에 특정 키가 존재하는지 확인
print("name" in dict_2)

# 딕셔너리의 값의 목록을 출력
print(dict_2.values())

# 딕셔너리의 아이템 목록을 출력
print(dict_2.items())

# if elif else 문 예시
if False:
    print(1)
elif True:
    print(2)
else:
    print(3)

# while 문과 continue break 예시
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
while index < 10:
    if number[index] % 2 == 0:
        index += 1
        continue
    if index > 10:
        break
    print(number[index])
    index += 1
else:
    print("else")

# for 문의 사용 예시
for data in range(0, 10, 2):
    print(data)

# 컴프리핸션을 사용한 List 생성
comp_1 = [i + 1 for i in a]
comp_2 = list(i + 1 for i in a if i % 2 == 0)
print(comp_1)
print(comp_2)

# 컴프리핸션을 사용한 딕셔너리 생성
comp_dict = {i + 1: i for i in a}
print(comp_dict)


# 함수 정의
def sum_two_number(var1, var2):
    print(var1, var2)
    return var1 + var2


# 함수 호출과 반환값
result = sum_two_number(1, 5)
print(result)

# None 타입
none_type = None
number_type = 1
print(none_type == False)
print(number_type == False)

# a는 False가 아니라고 하지만
# if 문에서는 False로 동작한다
if none_type:
    print("Hello")
if number_type:
    print("World")

# 번외
# 파이썬에 메모리 사용
# https://planbs.tistory.com/entry/Python-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EB%A9%94%EB%AA%A8%EB%A6%AC-%ED%95%A0%EB%8B%B9-%EB%B0%A9%EC%8B%9D
a = 1
b = 1
print(a == b)
print(a is b)

c = list()
d = list()
print(c == d)
print(c is d)
