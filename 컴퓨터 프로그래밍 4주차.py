#1번 문제
data = input("인사")

if data == "안녕하세요" :
        print("반갑습니다")
elif data != "안녕하세요" :
        print("인사를 먼저하세요")

#2번 문제
a = int(input("값을 입력하세요"))
b = a + 100
print(b)
if b >= 150 :
        print(b)
elif b <= 150 :
        print("값이 부족합니다")

#3번문제
numbers = [100, 200, 300]
for i in numbers :
        print(i)
numbers.append(330)
numbers.append(220)
numbers.append(110)
result = numbers[3:6]
print(result)

#4번문제
number = [3, 100, 23, 33, 72, 94]
result = []
for k in number:
    if k % 3 == 0:
        result.append(k)
print(result)

#5번문제
a = 1
while a < 1000 :
    a = a + 1
    print(a)
    if a == 1000 :
        break

#6번 문제
a = 1
if a % 2 != 0:
        print("홀수")
elif a % 2 == 0:
        print("짝수")

a = 1
y = 0
while a <= 100:
    if a % 2 != 0:
        y += a
    a += 1
print(y)

