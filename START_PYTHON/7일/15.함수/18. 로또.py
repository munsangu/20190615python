import random

def lotto_answer(): #정답 로또함수
    lotto = []
    while len(lotto) < 6: # 로또 리스트의 길이가 6전까지 반복
        num = random.randint(1,45)
        if num not in lotto: # 리스트에 없으면 추가
            lotto.append(num)
    return lotto

def lotto_num(): #내가 입력하는 리스트
    my_lotto = []
    count = 1
    while len(my_lotto) < 6:
        num = int(input("%d번째 숫자 입력: "%count))
        if num >= 1 and num <= 45 and num not in my_lotto:
            my_lotto.append(num)
            count += 1
    return my_lotto

lotto = lotto_answer() #정답 로또 리스트
my_lotto = lotto_num() #내가 입력할 로또 리스트
print(lotto)
print(my_lotto)
#내가 몇개를 맞췄는지?

count = 0
for i in my_lotto:
    if i in lotto:
        count += 1
print("%d개 맞췄습니다."%count)
