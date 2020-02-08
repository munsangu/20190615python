class Player: # 슈퍼 클래스
    def __init__(self,name,age):
        self.name = name
        self.age = age
class SoccerPlayer(Player): # 서브 클래스
    def Goal(self,goal):
        self.goal = goal

player = Player("손흥민", 28)
print("%s : %d"%(player.name, player.age))

soccerplayer = SoccerPlayer("손흥민",28)
soccerplayer.Goal(3)
print("%s : %d : %d"%(soccerplayer.name,soccerplayer.age,soccerplayer.goal))
