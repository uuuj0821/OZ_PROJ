from math import sqrt


pi = 3.141592

# 반지름 구하기
def number_input(num):
    return float(num)

# 원 둘레 구하기
def get_circum(radius):
    return 2 * pi * radius

# 원 넓이 구하기
def get_circle(radius):
    return pi * radius * radius

# 정사각형 넓이 구하기
def square(num):
    return num * num

# 직사각형 넓이 구하기
def rectangle(x, y):
    return x * y

# 삼각형 넓이 구하기
def triangle(x, y):
    return x * y / 2

# 속도 구하기
def speed(s, t):
    return s / t

