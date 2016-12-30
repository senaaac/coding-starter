def gugudan():
    try:  #예외처리와 구분되는 정상적인 조건
        dan = int(input("2에서 9사이의 숫자를 입력해주세요:"))
        if 1 < dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan*num))
        else:
            print("2에서 9사이의 숫자만 입력해주세요!")
            gugudan()
    except ValueError: #예외처리를 하이 위한 조건: 변수의 기본자료종류(정수,소수,문자 등)이 아닌경우
        print("숫자만 입력해주세요.")
        gugudan()
    except:
        print("알 수 없는 에러가 발생했습니다")
        gugudan()
gugudan()
