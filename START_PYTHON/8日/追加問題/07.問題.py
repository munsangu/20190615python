print(ord("A"))#65
print(ord("Z"))#90
print(ord("a"))#97
print(ord("z"))#122
print(chr(90))
string = input("문자 입력 : ")
convert_string = []
for i in string:
    if ord(i) >= 65 and ord(i) <= 90:
        convert_string.append(chr(ord(i) + 32))
    elif ord(i) >= 97 and ord(i) <= 122:
        convert_string.append(chr(ord(i) - 32))
    else:
        convert_string.append(i)
convert_string = str(convert_string)
print(convert_string)
convert_string = convert_string.replace("[","")
convert_string = convert_string.replace("]","")
convert_string = convert_string.replace("\'","")
convert_string = convert_string.replace(",","")
convert_string = convert_string.replace(" ","")
print(convert_string)
