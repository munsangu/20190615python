def data_unit(d, u):
    #k, m, g, t말고 다른걸 입력하면 에러메시지!
    ex = ["T","G","M","K"]
    if u not in ex:
        print("잘못된 단위 입력입니다.")
    elif u == 'T':
        return data * 1024 * 1024 * 1024 * 1024 #data * 1024 ** 4
    elif u == 'G':
        return data * 1024 * 1024 * 1024
    elif u == 'M':
        return data * 1024 * 1024
    elif u == 'K':
        return data * 1024
data, unit = input("용량입력(k, m, g, t) : ").split() #"5 m" => ["5", "m"]
data = int(data)
unit = unit.upper()
#고급포매팅 {:,d} : 1000단위 구분기호
print("출력 {:,d} {} => {:,d} byte입니다.".format(data,unit,data_unit(data, unit)))
