# exceptions

# zerodivisionerror
# 1/0

def divide_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다"

# 4 / 2 = 2
print(divide_by(4,2))
print(divide_by(4,0))


# 예외 만들기
class EvenNumberDevisionError(Exception):
    pass

def devide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDevisionError #에러를일으키는상황임
    else:
        return  first / second

print(devide_by_odd_number(6, 3))
print(devide_by_odd_number(6, 2))
