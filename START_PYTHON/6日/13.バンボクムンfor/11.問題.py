apart = [[101,102,103,104],[201,202,203,204],[301,302,303,304]]
floor = 1
# 이중 for를 써서 출력
# range를 써도 되고 안써도 됨 (단, 안 쓰는 게 조금 더 쉬움)
for i in apart:
   for j in i:
     print("%d호에 부착완료"%j)
   print("%d층에 모두 부착완료"%floor)
   floor += 1

floor = 1
for i in range(3):
    for j in range(4):
        print("%d 호에 부착완료"%apart[i][j])
    print("%d 층에 모두 부착완료"%floor)
    floor += 1
