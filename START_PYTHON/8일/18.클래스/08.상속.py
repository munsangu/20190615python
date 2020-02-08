#상속 : 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
#기존클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황에서 자주 사용
#개발기간을 단축할 수 있고 코드의 중복을 피할 수 있다.

#스마트티비를 만들거야 => 기존의 TV의 기능들을 새로 만들필요가 없어 => 추가시키면되겠네
class Tv: #부모클래스, 수퍼클래스
    def powerOn(self):
        print("TV를 켭니다.")
    def powerOff(self):
        print("TV를 끕니다.")
    def vlUp(self):
        print("볼륨을 올립니다.")
    def vlDown(self):
        print("볼륨을 줄입니다.")
class SmartTv(Tv): #자식클래스, 서브클래스
    def SettopOn(self):
        print("셋톱을 켭니다.")
    def SettopOff(self):
        print("셋톱을 끕니다.")
    def Search(self, search):
        print("%s를 시청합니다."%search)

LGTV = SmartTv()
#부모로부터 물려받은 모든 메소드, 필드 사용가능
LGTV.powerOn()
LGTV.SettopOn()
LGTV.vlUp()
LGTV.Search("나혼자산다")
LGTV.vlDown()
LGTV.powerOff()
LGTV.SettopOff()
