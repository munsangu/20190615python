
import re
custlist=[]
page = -1

def exe(choice):
        if choice=='I':
            insertData()
        
        elif choice=='C':
            curSearch()
        
        elif choice=='P':
            preSearch()

        elif choice=='N':
            nextSearch()

        elif choice=='U':
            updateData()
        
        elif choice=='D':
            deleteData()
        
        elif choice=='Q':
            quit()

def insertData():        
    customer={'name':'','sex':'',"email":'',"birthyear":''}
    customer['name']=str(input("이름을 입력하세요 : "))
        
    while True:
            customer['sex']=str(input("성별(M/m 또는 F/f)을 입력하세요 : "))
            customer['sex']=customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
            else:
                print('M/m 또는 F/f 중 입력해주세요')

    while True: # 중복되지 않게 입력
        regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
        while True:
            customer['email']=input("이메일을 입력하세요 : ") 
            golbang = regex.search(customer['email'])
            if golbang:
                break
            else:
                print('"@"를 포함한 정확한 이메일을 써주세요')

        check=0
        for i in custlist:
            if i['email']==customer['email']:
                check=1
        
        if check==0:
            break
        print('중복되는 이메일이 있습니다.')    
            

    while True:
            customer['birthyear']=input("출생년도 4자리를 입력해주세요 : ")    

            try:
                int(customer['birthyear'])
            except:
                print('숫자를 입력해주세요')
            else:
                if len(customer['birthyear'])==4:
                    break
                else:
                    print('4자리로 입력해주세요')

    print(customer)
    custlist.append(customer)
    print(custlist)
    global page
    page += 1

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
    exe(choice)