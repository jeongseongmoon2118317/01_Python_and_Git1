#1번 문제
class join:
    def __init__(self, join_name, join_age, join_phone):
        self.name = join_name
        self.age = join_age
        self.phone = join_phone

    def info(self):
        print(f"가입하신 계정의 이름은 {self.name}이며, 나이는 {self.age}. 그리고 연락처는 {self.phone}입니다.")


a = join("정성문", "23", "01050154903")
print(a.name, a.age, a.phone)
a.info()

#2번 문제
def length(message):
    if len(message) <= 20:
        return "50원"
    else:
        return "100원"


mail = input("문자 메시지를 입력하세요: ")
print(length(mail))