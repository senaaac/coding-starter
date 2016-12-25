# 사람클래스: 이름, 나이, 성별
# 직장 동료 클래스를 사람클래스를 이용해 만들기, 사람 기본 요소 외 별도 추가 사항은 직급

class Person :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class CoworkerA(Person):
    def __init__(self, name, age, gender, position):
        Person.__init__(self, name, age, gender)
        self.position = position

# coworker_1 = CoworkerA(input("이름:"), input("나이:"), input("성별:"), "대리")


class CoworkerB(CoworkerA):
    def __init__(self, name, age, gender, position):
        CoworkerA.__init__(self, name, age, gender, position)

coworker_2 = CoworkerB(input("이름:"), input("나이:"), input("성별:"), input("직함:"))

# print ("이름 :" + coworker_2.name)
# print ("나이 :" + coworker_2.age)
# print ("성별 :" + coworker_2.gender)
# print ("직함 :" + coworker_2.position)
