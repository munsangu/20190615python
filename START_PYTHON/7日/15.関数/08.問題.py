def reverse_number(num):
    reverse = 0
    while num != 0:
        reverse = reverse * 10 + num % 10
        num //= 10
    print("거꾸로 수: %d"%reverse)


    # while num ! = 0:
    #     print(num%10,end="")
    #     num // = 10

reverse_number(int(input("정수 입력 : ")))
