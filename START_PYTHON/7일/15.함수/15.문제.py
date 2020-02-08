account = ["msw", "123"]
def login(i,p):
    if i == account[0] and p == account[1]:
        print("[%s] 님이 로그인 하셨습니다."%i)
    else:
        print("비밀번호가 다릅니다.")

uid, upw = input("ID : "), input("PW : ")
login(uid, upw)


# def login(ac, id, pw):
#     if id in ac:
#         if pw == ac[id]:
#             print("[%s]님이 로그인했습니다."%id)
#         else:
#             print("비밀번호가 다릅니다.")
#     else:
#         print("아이디가 잘못됐습니다.")
# account = {"pomin615":"0123","thdehdduf20":"4567"}
# uid = input("ID : ")
# upw = input("PW : ")
# login(account, uid, upw)
