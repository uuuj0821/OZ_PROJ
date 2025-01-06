######################################## 1. input()

# hello = input()
# print(hello + "나도 안녕")

# hello2 = input("인사해줘!")
# print(hello + " 나도 안녕")

# num = input("숫자입력해줘 : ")
# print(num)
# print(type(num))

# num2 = int(num)
# print(type(num2))
# print(num2) 

# num3 = int(input("숫자를 입력해줘 : "))
# print(num3, type(num3))

# str1, str2 = input(), input()
# str3, str4 = input().split() # () 안의 설정에 따라 구분되어 변수할당 됨 예) input().split(","), ...


######################################## 2. print()

# print(str1, " ", str2)

# num1, num2, num3, num4 = map(int, input().split(","))
# print(num1, num2, num3, num4)

# print("초코칩", "민트", "샷추가", "휘핑크림")
# print("초코칩", "민트", "샷추가", "휘핑크림", sep = '/')
# print("초코칩", "민트", "샷추가", "휘핑크림", sep = ' : ')
# print("초코칩", "민트", "샷추가", "휘핑크림", sep = '\n')

# print("초코칩", "민트", "샷추가", "휘핑크림", end = '\n')
# print("초코칩", "민트", "샷추가", "휘핑크림", end = '///////')


######################################## 3. list()

# 리스트 = []
# print(리스트)
# print(type(리스트))

# 리스트1 = [23, "이게 리스트다", 3.43, True, False]
# print(리스트1)
# print(type(리스트1))

# 리스트 = list(range(10))
# print(리스트)
# print(type(리스트))

# 리스트1 = range(10)
# print(type(리스트1))

# 리스트2 = list(range(0, 20, 2))
# print(리스트2)

# 리스트3 = list(range(20, 0, -1))
# print(리스트3)

# 리스트4 = list(range(20, 0))
# print(리스트4)

# a, b, c = ["들", "어", "가"]
# print(a, b, c, sep='\n')

# 지갑 = [1000, 2000, 3000]
# print(f'지갑은 : {지갑}')
# print(type(지갑))

# 천원, 이천원, 삼천원 = 지갑
# print(f'각 변수는 {천원}, {이천원}, {삼천원}')
# print(type(천원))

## 리스트문제 - 로또
# 로또 = [3, 5, 15, 33, 41, 44]
# 로또2 = [2, 12, 15, 24, 33, 39]

# # 1. 로또 변수에 있는 리스트의 인덱스 1번부터 2번까지의 값을 출력
# print(f'1. {로또[1:3]}')

# # 2. 로또 변수의 마지막 위치 출력
# print(f'2. {로또[len(로또)-1]}')
# print(f'2. {로또[-1]}')

# # 3. 반대로 출력해보세요
# print(f'3. {로또[::-1]}')

# # 4. 로또 리스트 안에 33이 있는지 확인해보세요
# print(f'4. {로또.count(33) >= 1}')
# print(f'4. {33 in 로또}')

# # 5. 로또 리스트와 로또2 리스트를 합쳐보세요
# print(f'5. {로또 + 로또2}')

# # 6. range를 이용해서 1부터 10 사이의 짝수만 들어있는 짝수(변수명) 리스트를 만들어주세요
# 짝수 = list(range(2, 11, 2))
# print(f'6. {짝수}')

# # 7. 짝수 리스트에 들어있는 값을 2배 늘리고 다시 짝수 변수에 담아줘 (길이를 2배로...)
# 짝수 = 짝수 * 2
# print(f'7. {짝수}')

# # 8. 짝수 리스트에 들어있는 요소의 개수를 구해줘
# print(f'8. {len(짝수)}')

# # 9. 짝수 리스트의 3번째 인덱스를 출력해줘
# print(f'9. {짝수[3]}')

# # 10. len() 함수를 이용해 인덱스 마지막 값을 출력해주세요.
# print(f'10. {짝수[len(짝수)-1]}')


######################################## 3-1. list() 메서드들

# ## list 값 넣고, 바꾸고, 지우고
# mzfood = ["숙주", "분모자", "마라", "소세지", "소고기", "옥수수면"]

# ## 값을 추가하는 방법 2가지
# # append()) : 마지막 요소에 값을 넣음
# # insert() : 원하는 곳에 값을 넣음

# print(mzfood)

# mzfood.append("고수")
# print(mzfood)

# mzfood.insert(0, "탕후루")
# print(mzfood)

# # print(type(mzfood.insert(0, "탕후루")))
# # print(type(mzfood))

# ## 값 지우기
# del mzfood[-1]
# print(mzfood)

# ## 값 바꾸기
# mzfood[-2] = "양고기"
# print(mzfood)

# ################ 문자열도 시퀀스자료형이긴하나 위 방식으로 할당 안 됨
# str = "반가워"
# print(str)
# print(str.replace("워", "웡"))

# # print(dir(str))

# mzfood.reverse()
# print(mzfood)

# mzfood.sort() # 기본오름차순
# print(mzfood)

######################################## 3-2. 2차원 리스트
# 양파같은 = [[2, 0], [3, 1]]
# print(양파같은)
# print(양파같은[0])
# print(양파같은[0][0])

# # 3을 출력하기
# print(양파같은[1][0])

# # 추가
# 양파같은.append([4, 1])
# print(양파같은)

# 양파같은.append(2)
# print(양파같은)

# 양파같은.append([3, 1])
# print(양파같은)

# print(양파같은[3])




# x, y = map(float, input('실수를 입력하세요: ').split())
# print(x, type(x))
# print(y, type(y))



######################################## 4. tuple

# 튜플 = (1, 2, 3, "4")
# print(튜플)

# 튜플_리스트화 = list(튜플)
# print(type(튜플_리스트화))

# 리스트 = [1, 2, 3]
# print(type(리스트))

# 리스트_튜플화 = tuple(리스트)
# print(type(리스트_튜플화))

#번외

# 수강생 = "중꺾그마"

# 수강생_list = list(수강생)
# 수강생_tuple = tuple(수강생)

# print(수강생_list)
# print(수강생_tuple)

# 수강생_list[1] = "뿌"
# print(수강생_list)

# #join함수 공부 알고 있으면 코테에 좋아요
# 취뽀_수강생 = "".join(수강생_list)
# print(취뽀_수강생)

# 취뽀_수강생 = "_".join(수강생_list)
# print(취뽀_수강생)

# 취뽀_수강생 = "&".join(수강생_tuple)
# print(취뽀_수강생)



######################################## 5. tuple

# people = {"힘":50, "지능":40}

# print(people["지능"])


# ### 딕셔너리 형변환
# student = ["유리", "철수", "맹구"]
# print(type(student))

# student_dict = dict(student)
# print(student_dict)
# print(type(student_dict))

딕셔너리3 = dict(힘=30, 지능=20, 체력=40, 민첩=90)
print(딕셔너리3)

딕셔너리4 = dict("힘"=30, "지능"=20, "체력"=40, "민첩"=90)