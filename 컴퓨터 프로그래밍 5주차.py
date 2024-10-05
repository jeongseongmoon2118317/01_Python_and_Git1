#1번 문제
def add(num1, num2, num3, num4) :
        result = num1 + num2 + num3 + num4
        return result
a = add(100, 200, 300, 400)
print(a)

def multiply(num5, num6, num7, num8) :
        result = num5 * num6 * num7 * num8
        return result
b = multiply(5, 6, 7, 8)
print(b)

#2번 문제
def name(num) :
        if num % 2 == 0 :
            return ("짝수")
        elif num % 2 != 0 :
            return ("홀수")
print(name(2))
print(name(1))

#3번 문제
def num(list) :
    total = 0
    for number in list :
        total += number
    return total / len(list)

print(num([1,2,3,4,5]))

#4번 문제
class id :
        def __init__(self, id_name, id_sex, id_information):
            self.name = id_name
            self.sex = id_sex
            self.information = id_information

        def bark(self):
            print(self.name, "공격!")

a = id("정성문", "남성", "대통령")
print(a.name, a.sex, a.information)
a.bark()

#5번 문제
class king :
        def __init__(self, king_place, king_size, king_kind, king_price, king_year):
            self.place = king_place
            self.size = king_size
            self.kind = king_kind
            self.price = king_price
            self.year = king_year
a = king("하남", "38평", "아파트", "5만원", "2024년")
print(a.place, a.size, a.kind, a.price, a.year)



