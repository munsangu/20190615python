import pickle

data = {1: 'python', 2: 'you need'}
#type dict
print(type(data))

# 파일로 저장
with open("./python_basic/test.pickle","wb") as f:
    pickle.dump(data,f)

# 파이썬 내에서 사용 바이트 형태
datab=pickle.dumps(data)
print(type(datab))

# 파일을 읽어옴
with open("./python_basic/test.pickle","rb") as f:
    data=pickle.load(f)
    print(data)

# 바이트 타입을 파이썬 형태의 데이터 타입으로
data1 = pickle.loads(datab)
print(data1)
print(type(data1))

