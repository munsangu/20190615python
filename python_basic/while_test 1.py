# treehit = 0
# while treehit < 10:
#     treehit = treehit +1
#     print("나무를 %d번 찍었습니다."%treehit)
#     if treehit == 10:
#         print("나무 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: 4
"""

number = 0
while number != 4:
    print(prompt)
    number = int(input("숫자를 입력하세요."))

