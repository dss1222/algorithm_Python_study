class Person:
    def __init__(self, param_name): #생성자 인자에 자기자신을 넘겨주는데 그것이 self
        print("i am created! ", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다")

person1 = Person("유재석")
print(person1.name)
print(person1)
person1.talk()
person2 = Person("박명수")
print(person2.name)
print(person2)
person2.talk()
