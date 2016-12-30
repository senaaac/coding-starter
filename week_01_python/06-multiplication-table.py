# 구구단 만들기
# 1) 사용자로부터 몇 단을 출력할 지 받을 것
# 2) 해당 단을 곱하기 1에서 곱ㅎ기 9까지 실행할 것

group = int(input("몇 단을 출력하시겠습니까?")) # input은 모든 것을 문자로 받으므로 숫자로 바꿔야함
for num in range (1, 10):
    print ("{} * {} = {}".format(group, num, group * num))
