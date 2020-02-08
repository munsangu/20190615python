user_input = input("저장할 내용 입력 : ")
with open("test.txt","a") as f:
    f.write(user_input)
    f.write("\n")
