import random

number_list = range(1,11) 
#범위를 일일히 적어 리스트로 만들기보다 범위를 설정하는것이더 빠르다고 생각해서 range를 사용.
def game():
    correct = random.choice(number_list)
    #랜덤으로 선택된 숫자가 코드가 진행될때마다 바뀌지 않게 correct로 지정.

    print("자 이제 숫자게임을 시작하지")
    print("너는 평소 숫자를 소중히 하지 않았어")
    print("1부터 10까지 숫자 중 하나를 맞춰봐")

    while True:
        try:
            answer = int(input("숫자를 입력해:"))
            #유저가 입력한 숫자와 랜덤으로 선탠학 숫자가 일치할수 있게 input데이터를 비교할수 있도록 answer로 할당함.
            if answer == correct: #정답을 맞췄을때 게임이 정지되도록 break를 함
                print("운이 좋군,,,,")
                break

            elif answer > 10 or answer < 0: #input데이터가 1~10사이의 숫자가 아닐때 게임을 진행을 중단함.
                print("멍청아 1에서 10사이의 수를 입력해라")
            elif answer > correct: #input데이터와 랜덤으로 정한 숫자를 비교하여 정답으로 유도 할 수 있게함.
                print("틀렸다 숫자가 너무 크군")
            elif answer < correct: #input데이터와 랜덤으로 정한 숫자를 비교하여 정답으로 유도 할 수 있게함.
                print("틀렸다 숫자가 너무 작군")
        except ValueError: #택스트나 유효하지 않은 입력이 있을 때
                print("유효하지 않은 입력입니다. 숫자만 입력하세요")

game() #게임을 실행

while True: #다시 게임을 실행하기 위한 반복문
    replay = input('하지만 이건 연습게임이었다. 다시한번 도전해볼텐가? y/n : ')
    if replay in ['y','yes']: #대답을 y와 yes로 만 입력하게 한후 계속 게임을 진행하게함
        print('좋다 이번엔 봐주지 않겠어')
        game()
    elif replay in ['n','no']:#대답을 n과 no로만 입력하게 한후 게임을 중단함
        print('겁쟁이로군....')
        break
    else: #그외의 대답을 입력했을때 게임이 종료되게함
        break
