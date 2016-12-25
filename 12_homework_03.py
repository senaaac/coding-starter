import random

winning_number = 0
losing_number = 0
drawing_number = 0

while winning_number < 3 and losing_number < 3 :
     game_user = input("가위,바위,보 중 하나를 고르세요?")
     game_list = ["가위", "바위", "보"]
     game_computer = random.choice(game_list)
     print("컴퓨터는 " + game_computer + "를 냈습니다")
     if (game_user == game_computer) :
         drawing_number = drawing_number + 1
         print("비겼다")
     elif (game_user == "가위" and game_computer == "보") or (game_user == "보" and game_computer == "바위") or (game_user == "바위" and game_computer == "가위") :
         winning_number = winning_number + 1
         print("이겼다")
     else :
         losing_number = losing_number + 1
         print("졌다")


print("이긴 횟수:" + str(winning_number))
print("진 횟수:" + str(losing_number))
print("비긴 횟수:" + str(drawing_number))
