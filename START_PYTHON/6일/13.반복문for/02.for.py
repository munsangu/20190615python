a = [(1,2),(3,4),(5,6)]
i,j =(1,2)
i,j =(3,4)
i,j =(5,6)
for i,j in a:
    print(i + j)

filmFestival ={
"최우수 감독상" : "택시운전사",
"감독상": "아이 캔 스피크",
"남우주연상": "송강호",
"여우주연상": "나문희"
}
for prize in filmFestival.keys():
    print(prize)
for winner in filmFestival.values():
    print(winner)
for prize_winner in filmFestival.items():
    print(prize_winner)
for prize, winner in filmFestival.items():
    print("%s : %s"%(prize, winner))
