import random

menu = input("한식, 양식, 중식 중 하나를 선택하세요?")
menu_korean = ["김가네", "로봇김밥", "한옥집"]
menu_western = ["tgif", "outback", "Mcdonald"]
menu_chinese = ["양자강", "황강반점","백짜장전문점"]

if menu == "한식":
    print(random.choice(menu_korean))

elif menu =="양식":
    print(random.choice(menu_western))

elif menu == "중식":
    print(random.choice(menu_chinese))

else :
    print("한식, 양식, 중식 외 다른 것을 선택하시면 안됩니다")
