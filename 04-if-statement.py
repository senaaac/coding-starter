#참과 거짓 boolean
# if
# True or False
# 거짓: none, false, 0
# and or not
# a = True
# b = False
#
# # a가 참이고, 그리고 b가 참이라면 (a와 b가 둘다 참이어야 된다)
# print(a and b)
# # a가 참이거나 혹은 b가 참이라면 (a나 b 둘 중 하나라도 참이면 된다)
# print(a or b)

d = 7
if d > 10:
    print("숫자는 10보다 큽니다")
elif d > 5 and d <= 10:
    print("숫자는 10보다 작거나 같고, 10보다는 큽니다")
else:
    print("숫자는 5보다 작거나 같습니다")
