class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}살, 키는 {self.height}cm 입니다.")

    def yell(self):
        print("아?")

class Developer(Person):
    keyboard = '기계식'
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def yell(self):
        print("어?")

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def yell(self):
        print("개발자님 여기 오류있어요")

    def aging(self):
        self.age += 2
        self.height -= 5
        print("개발자를 새로 뽑아야 하나...")
        Developer.keyboard = '멤브레인'

d1 = Developer('유땡땡', 23, 170)
d2 = Designer('김왕왕', 25, 160, '불면증')
p1 = ProductManager('오양양', 24, 162)

d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()

p1.aging()
p1.introduce()
