# import time
# #유닉스 시간 : 1970년 1월 1일 0시 0분
# #time.time() : 유닉스 시간부터 오늘날까지를 초 단위로 리턴
# print(time.time())
#
# #time.sleep() : 일정한 간격을 두고 코드를 실행
# time.sleep(3)
# print("이것이 슬립이다.")
#
# #localtime : 연도, 월, 일, 시, 분, 초의 형태로 바꿔주는 함수
# print(time.localtime(time.time()))

import time as t
print("\n===time함수를 이용한 스톱워치===")
input("엔터를 누르고 3초를 마음속으로 세시오")
start = t.time() #시작시간 저장

input("3초가 되면 다시 엔터를 누르세요")
end = t.time() #끝나는 시간 저장

result = end - start

print("걸린 시간 : %.2f"%result)
print("오차 : %.2f초"%abs(result-3))
