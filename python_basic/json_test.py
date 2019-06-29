import json

customer = {
    'id': 152352,
    'name': '강진수',
    'history':[
        {'data':'2015-03-11', 'item':'iphone'},
        {'data':'2016-02-23', 'item':'Monitor'},
    ]
}

jsonString = json.dumps(customer)

print(jsonString)
print(type(jsonString))

jsonString = json.dumps(customer, indent=4)
print(jsonString)

with open("./python_basic/data.json","wt") as f:
    f.write(jsonString)

# json.dumps 파이썬 내에서 바로 사용
jsonString = json.dumps(customer, indent=4)
print(jsonString)

# json.dump 파일로 바로 저장
with open('./python_basic/data.json','wt') as f:
    json.dump(customer,f,indent=4)

# json.loads json 문자를 읽어서 파이썬 객체로 변경
customer1 = json.loads(jsonString)
print(jsonString)

# json.load json 파일을 읽어서 파이썬 객체로 변경
with open('./python_basic/data.json','rt') as f:
    customer2 = json.load(f)
    print(type(customer2))
    print(customer2) 



    