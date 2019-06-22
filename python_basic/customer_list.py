import re
p = re.compile('[a-z]+')
custlist=[]
page=-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 : 
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')

    if choice=="I":
        customer={'name':'','sex':'','email':'','birthyear':''}
        customer['name']=input("이름을 입력하세요 : ")
        while True:
            customer['sex']=input("성별(M/m 또는 F/f)을 입력하세요 : ")
            customer['sex']=customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
        while True: # 중복되지 않게 입력

            regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
            while True:
                customer['email']=input("email을 입력하세요: ")
                golbang = regex.search(customer['email'])
                if golbang != None:
                    break
                else:
                    print('"@"를 포함한 정확한 이메일을 써주세요')  
                    
            check=0
            for i in custlist:
                if i['email'] == customer['email']:
                    check=1
                    
            if check==0:
                break
            print("중복되는 이메일이 있습니다. ")

            
        while True:
            customer['birthyear']=input("출생년도 4자리를 입력해주세요. : ")

            if len(customer['birthyear'])==4 and customer['birthyear'].isdigit():
                break
        print(customer)
        custlist.append(customer)
        print(custlist)
        page += 1

        print("고객 정보 입력")
        
    elif choice =="C":
        print("현재 고객 정보 조회")
    elif choice =="P":
        print("이전 고객 정보 조회")
    elif choice =="N":
        print("다음 고객 정보 조회")
    elif choice =="U":
        print("고객 정보 수정")
    elif choice =="D":
        print("고객 정보 삭제")
    elif choice =="Q":
        print("프로그램 종료")
        break
    else:
        print("잘못 입력하셨습니다.")
