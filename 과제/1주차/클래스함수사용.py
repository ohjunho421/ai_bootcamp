class Person: #클래스 Person 지정
    def __init__(self):
        self.name = None
        self.gender = None
        self.age = None

    def input_name(self): #이름을 글자만 입력하게끔 하는 조건문 코드를 정의함.
        while True:
            name = input('당신의 이름을 입력하세요. : ')
            if name.isalpha():
                self.name = name
                break
            else:
                print('잘못입력하셨습니다. ')
                
    def input_gender(self): #성별 입력을 남,여로만 제한하는 조건문 코드를 정의함
        while True:
            gender = input('당신의 성별을 입력하세요. : ')
            if gender in ['남','여']:
               self.gender = gender
               break
            else:
                print('잘못 입력하셨습니다. 남,여 로만 입력해주세요.')

    def input_age(self): #나이 입력을 숫자만 입력하게끔 하는 조건문 코드를 정의함
        while True:
            try : 
                age = int(input('당신의 나이를 입력하세요. : '))
                self.age = age
                break
            except ValueError :
                print('숫자만 입력하세요.')

#class에서 정의한 매서드를 불러와 정보를 입력하게함                
person_instance = Person()
person_instance.input_name()
person_instance.input_gender()
person_instance.input_age()

#입력한 내용들이 print되게 함
print('당신은')
print(f"이름은 {person_instance.name}, 성별은 {person_instance.gender}자이며")
print(f"나이는 {person_instance.age}살 입니다.")

#입력된 age을 기준으로 조건문에 맞는 맨트가 나오게함
age= person_instance.age

if age > 33 :
    print('저보다 형이시군요')
elif age == 33 :
    print('반갑다 친구야')
elif age < 33 :
    print('저보다 동생이시군요')
