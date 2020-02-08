# a = int(input("만두 개수를 입력하세요: "))
# b = a*1000
# c = b-(b*0.25)
# d = b-(b*0.15)
#
# if a>=100:
#     print("가격:",int(c),"원", "현금결제가:",int(c-(c*0.10)),"원" )
# elif a>=10:
#     print("가격:",int(d),"원", "현금결제가:",int(d-(d*0.10)),"원" )
# else:
#     print("가격:",int(b),"원", "현금결제가:",int(b-(b*0.10)),"원" )

dumpling = int(input("만두 개수 입력 : "))
#알고리즘문제는 저랑 답이같을 필요없어요
price = 1000 #기본가격
if dumpling > 0 and dumpling < 10 :
    price *= dumpling #복합대입연산자 price = price * dumpling
elif dumpling >= 10 and dumpling < 100:
    price *= dumpling * 0.85
elif dumpling >=100:
    price *= dumpling * 0.75
else: #0보다 작은경우
    print("잘못된 개수입니다.")
print("가격 : %d원, 현금결제가 : %d원"%(price, price * 0.9))
