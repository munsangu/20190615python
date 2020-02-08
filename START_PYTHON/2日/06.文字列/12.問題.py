money = "부산 112 2014 9018 01입금 = 10억원"
bank = money[:3]
Gejoua = money[3:19]
Won = money[24:]
print("은행:", bank)
print("계좌번호:", Gejoua)
print("금액:", Won)
