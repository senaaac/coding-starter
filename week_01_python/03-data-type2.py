# 목록  list, tuple
# 사전 dict - dictionary
# 집합 set

# list []
# print("list")
# list_a = [1,2,3]
# print(list_a)
# # print(type([1,2,3]))
# # index [n]는 0부터 시작 해서 숫자를 찾음 결국 n-1의 자리수 출력
#
# # print(list_a[0])
# # slice [n1:n2]는 인덱스를 짜른다는 의미인데, 맨 마지막 인덱스는 출력하지 않음
# # print(list_a[0:2])
# # append
# list_a.append(4)
# print(list_a)
# list_a.remove(2)
# print(list_a)
# list_a.clear()
# print(list_a)

# tuple ()
# print("tuple")
# print((1,2,3))
# print(type((1,2,3)))
# tuple_a = (1,2,3)
# print(tuple_a)
# print(type(tuple_a))
# tuple은 한 번 생성 후 내부 값 변경 불가

#dict map 역할 {} 사용
# key & value
# dict_a =  {"apple" : "a type of fruits", "pen" : " a thing to write" }
# print(dict_a)
# print(dict_a["apple"])
# #edit value
# dict_a["pen"] = "something to write"
# print(dict_a)

# set set([])
set_a = set([1,2,3,3,3,3,2])
set_b = set([2,4,6])
print(set_a)
print(set_b)

# 집합 - 교집합, 합집함, 차집합, 여집합
# set을 쓰는 가장 중요한 기능은 중복제거

#교집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
