# 1) 사용자입력
#2) 컴퓨터 임의 선택
#3) 3번 지거나, 이기면 승패 확정


import random

ROCK = "바위"
SCISSORS = "가위"
PAPER = "보"
RSP_LIST = (
    ROCK,
    SCISSORS,
    PAPER
)

win_count = 0
lose_count = 0

while win_count < 3 and lose_count < 3 :
    user_choice = input("{},{},{}:" .format(SCISSORS, ROCK, PAPER))
    computer_choice = random.choice(RSP_LIST))
    if user_choice == computer_choice :
        print("비겼습니다")
    elif  user_choice  not in RSP_LIST:
        print("가위,바위,보 중에서 하나를 입력해주세요.")

    elif ((user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS
            and computer_choice == PAPER)
        or (user_choice == PAPER
            and computer_choice == ROCK)
        win_count = win_count + 1
        print ("이겼습니다")
    else:
        lose_count = lose_count + 1

if win_count ==3:
    print("사용자가 최종 승리하였습니다.")

else:
    print("컴퓨터가 최종 승리하였습니다.")

# import random
#
# winning_number = 0
# losing_number = 0
# drawing_number = 0
#
# while winning_number < 3 and losing_number < 3 :
#      game_user = input("가위,바위,보 중 하나를 고르세요?")
#      game_list = ["가위", "바위", "보"]
#      game_computer = random.choice(game_list)
#      print("컴퓨터는 " + game_computer + "를 냈습니다")
#      if (game_user == game_computer) :
#          drawing_number = drawing_number + 1
#          print("비겼다")
#      elif (game_user == "가위" and game_computer == "보") or (game_user == "보" and game_computer == "바위") or (game_user == "바위" and game_computer == "가위") :
#          winning_number = winning_number + 1
#          print("이겼다")
#      else :
#          losing_number = losing_number + 1
#          print("졌다")
#
#
# print("이긴 횟수:" + str(winning_number))
# print("진 횟수:" + str(losing_number))
# print("비긴 횟수:" + str(drawing_number))
