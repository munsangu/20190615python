# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")

# pocket = ['paper','handphone']
# card = True
# if 'money' in pocket:
#     print("택시를 타고 가라")
# else:
#     if card:
#         print("택시를 타고 가라")
#     else:
#         print("걸어가라")

pocket = ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")