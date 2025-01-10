import mymath as m

# 원의 넓이 구하기
num_circle = int(input("숫자를 입력하세요 : "))
print(m.get_circle(num_circle))

# 속도 구하기
num_speed = input("거리와 시간 값을 숫자로 입력하세요 (공백으로 구분)").split(" ")
print(m.speed(int(num_speed[0]), int(num_speed[1])))