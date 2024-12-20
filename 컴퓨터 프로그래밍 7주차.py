#1번 문제
import random

def numbers():
    result = []
    while len(result) < 6:
        num = random.randint(1,45)
        if num not in result:
            result.append(num)
    return result

print(numbers())

#2번 문제
class math :
    def __init__(self, math_num):
        self.num = math_num
    def output(self):
        print(f"{self.num}단")
        for i in range(1, 10) :
            result = self.num * i
            print(f"{self.num} * {i} = {result}")
a = int(input("몇 단을 해드릴까요?"))
gugudan = math(a)
gugudan.output()

#3번 문제 #축구선수 소개 프로그래밍
class Player:
    def __init__(self, player_name, player_position, player_team, player_goals, player_assists):
        # 선수의 이름, 포지션, 소속팀, 골 수, 어시스트 수 초기화
        self.name = player_name
        self.position = player_position
        self.team = player_team
        self.goals = player_goals
        self.assists = player_assists

    # 선수 정보 출력
    def information(self):
        return (f"선수 이름: {self.name}, 포지션: {self.position}, 소속팀: {self.team}")

    # 소속팀 출력
    def inteam(self):
        return f"{self.name}은(는) 현재 {self.team} 소속입니다."

    # 선수 공격스탯 출력
    def stats(self):
        return f"{self.name}의 기록은 골: {self.goals}골, 어시스트: {self.assists}개 입니다."

#선수 정보 입력. 정수형 int를 사용하고 input 함수를 사용 하여 값을 주입 받는다.
def main():
    name = input("선수의 이름을 입력하세요: ")
    position = input("선수의 포지션을 입력하세요: ")
    team = input("선수의 소속팀을 입력하세요: ")
    goals = int(input("골 수를 입력하세요: "))
    assists = int(input("어시스트 수를 입력하세요: "))

# palyer 클래스의 인스턴스 생성
    soccerplayer = Player(name, position, team, goals, assists)

#최종 선수 소개 출력
    print("선수 소개:")
    print(soccerplayer.information())
    print(soccerplayer.inteam())
    print(soccerplayer.stats())

#프로그램 시작점
main()


