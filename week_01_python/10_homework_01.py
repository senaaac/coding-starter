import random
# 리스트를 tuple()로 만듦. 데이터 변경 못하도록함
KOREAN_FOOD = ("김치찌개", "비빔밥", "국수")
CHINESE_FOOD = ("짜장면", "탕수육", "짬뽕")
JAPANESE_FOOD = ("라면", "돈까스", "돈부리")

#사용자로부터 입력
user_choice = input("한식, 중식, 일식 중에서 골라주세요:")

#임의로 추천
if user_choice == "한식":
    choice_result = random.choice(KOREAN_FOOD)
elif user_choice == "중식":
    choice_result = random.choice(CHINESE_FOOD)
elif user_choice == "일식":
    choice_result = random.choice(JAPANESE_FOOD)
else :
    print ("한식, 중식, 일식 중에서 선택하셔야합니다.")

if choice_result:
    print ("{}중에서 {}가 선택되었습니다" .format(user_choice, choice_result)

# import random
#
# menu = input("한식, 양식, 중식 중 하나를 선택하세요?")
# menu_korean = ["김가네", "로봇김밥", "한옥집"]
# menu_western = ["tgif", "outback", "Mcdonald"]
# menu_chinese = ["양자강", "황강반점","백짜장전문점"]
#
# if menu == "한식":
#     print(random.choice(menu_korean))
#
# elif menu =="양식":
#     print(random.choice(menu_western))
#
# elif menu == "중식":
#     print(random.choice(menu_chinese))
#
# else :
#     print("한식, 양식, 중식 외 다른 것을 선택하시면 안됩니다")
