class Person:
    def __init__(self):
        self.name = None
        self.gender = None
        self.age = None

    def input_name(self):
        while True:
            name = input('당신의 이름을 입력하세요. : ')
            if name.isalpha():
                self.name = name
                break
            else:
                print('잘못입력하셨습니다. ')
                
    def input_gender(self):
        while True:
            gender = input('당신의 성별을 입력하세요. : ')
            if gender in ['남','여']:
               self.gender = gender
               break
            else:
                print('잘못 입력하셨습니다. 남,여 로만 입력해주세요.')

    def input_age(self):
        while True:
            try : 
                age = int(input('당신의 나이를 입력하세요. : '))
                self.age = age
                break
            except ValueError :
                print('숫자만 입력하세요 : ')
                
person_instance = Person()
person_instance.input_name()
person_instance.input_gender()
person_instance.input_age()

print('당신은')
print(f"이름은 {person_instance.name}, 성별은 {person_instance.gender}자이며")
print(f"나이는 {person_instance.age}살 입니다.")



    if int(person_instance.input_age()) > 33 :
        print('저보다 형이시군요')
    elif person_instance.input_age() == 33 :
        print('반갑다 친구야')
    elif person_instance.input_age() < 33 :
        print('저보다 동생이시군요')
