# 문자열 변수 [인덱스번호]
# 책[책 페이지]
book = "Welcome to Python!"
print(book[0])
print(book[4])
print(book[11])
print(book[-1]) #가장 뒷에 있는 글자
print(book[-7])

#len() : 내부에 적은 변수의 길이를 반환
length = len(book)
print(length)
print(book[length -1]) #인덴스 번호는 0부터 시작
# 총 문자열의 길이 - 1 : 가장 뒤의 문자
book = "Welcome to Python!"

Wet = book[0] + book[1] + book[-5]
print(Wet)

Phone = book[-7] + book[-4] + book[-3] + book[-2] + book[1]
print(Phone)
