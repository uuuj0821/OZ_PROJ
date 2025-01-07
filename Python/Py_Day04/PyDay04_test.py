################################################################################### 1. if문

# amount = int((input("붕어빵 몇개 사실건가요?")))

# if amount > 3:
#     print("개당 500원 입니다.")
# else:
#     print("개당 1000원 입니다.")


# taste = input("붕어빵 맛을 선택해 주세요! (팥, 슈크림, 잡채)")

# if taste == "팥":
#     print(f'{taste}를 선택하셨습니다.')
# elif taste == "슈크림":
#     print(f'{taste}를 선택하셨습니다.')
# elif taste == "잡채":
#     print(f'{taste}를 선택하셨습니다.')


###################################################################################

# 문제 : 단어 a의 가운데 글자를 반환하는 코드
# 조건 : 단어의 길이가 짝수라면 가운데 두글자를 출력하면 됩니다.

## 입력값1 : "abcde"
## 입력값2 : "qwer"

#a = "abcde"
# a = input("문자열을 입력하세요.")

# count_a = len(a)
# center_char_a = len(a) // 2

# if count_a % 2 == 0:
#     print(a[(center_char_a)-1] + a[center_char_a])
# else:
#     print(a[center_char_a])


################################################################################### 2. for문

# for i in range(5):
#     print("for문 반복하기")

# for i in range(3, 10):
#     print("for문 출력하기", i)

# for i in range(2, 10, 3):
#     print("for문 출력하기", i) 


# 과일 = ["두리안", "사과", "바나나"]

# for i in 과일:
#     print(i)

# for i in "닥스훈트":
#     print(i, end=' ')


###################################################################################

# 문제 : 절대값 정수가 담긴 정수 변수와 그 정수와 부호를 차례로 담은 부호 변수가 있다.
# 두 변수를 이용해 실제 정수의 합을 구해주세요 (True : 양수, False : 음수)

# 정수 = map(int, (input("절대값 정수 2개를 입력해주세요 (쉼표로 구분))").split(",")))
# 부호 = input("부호 2개를 입력해주세요 (True, False) (쉼표로 구분해주세요)").split(",")

# 합 = 0

# for i, j in zip(부호, 정수):
#     if i == "True":
#         합 += j
#     else:
#         합 -= j
#     print(합)

# print(f'총 합은 {합} 입니다.')


################################################################################### 3. while문

# i = 0

# while i < 10:
#     print("점점 성장하는 여러분")
#     i += 1

# i = 1

# while i < 10:
#     print("이정도로 성장할줄이야", i)
#     i += 1


# i = 10

# while i > 0:
#     print("이정도로 성장할줄이야", i)
#     i -= 1
  

###################################################################################

# 문제 : 콜라츠하는 사람은 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다고 추측했다.
# 작업
# 1-1. 입력된 수가 짝수라면 2로 나눈다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
# 2. 위 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
# 예를 들어, 입력된 수가 6이라면 6->3->10->5->16->8->4->2->1
# num 변수에 있는 수를 1로 만드는데 몇번이나 작업을 반복해야한느지 출력한다.

# inputNum = int(input("숫자를 입력해주세요."))
# num = 0 

# while inputNum:
#     if inputNum == 1:
#         break

#     if inputNum % 2 == 0:
#         inputNum = int(inputNum / 2)
#     else:
#         inputNum = (inputNum * 3) + 1

#     num += 1
#     print(f'현재값 : {inputNum}, 작업횟수 : {num}')

    

class business():
    def __init__(self):
        self.bungeoppang_type = ["팥붕어빵", "슈크림붕어빵", "초코붕어빵"]
        self.bungeoppang_price = [1000, 1200, 1500]
        self.stock_count = [10, 8, 5]
        self.order_count = [0, 0, 0]
        self.stock = dict(zip(self.bungeoppang_type, self.stock_count))
        self.price = dict(zip(self.bungeoppang_type, self.bungeoppang_price))
        self.order = dict(zip(self.bungeoppang_type, self.order_count))
        # print(order)

    def admin_stock(self, add_type, add_amount):  # 재고 추가         
        self.stock.update({add_type : self.stock.get(add_type) + int(add_amount)})  # 재고 업데이트
        print(f'현재재고 : {self.stock}')

    def order_bungeoppang(self, order_type, order_amount):
        if (self.stock.get(order_type) - int(order_amount)) < 0: # 재고가 부족할 경우, 손님에게 재고 부족을 알리고 재고를 감소시키지 않습니다.
            print(f'{order_type}의 수량이 부족합니다. 주문할 수 있는 최고 수량은 {self.stock.get(order_type)} 개 입니다. 다시 주문 해 주세요.')
        else: # 재고가 충분할 경우, 주문한 만큼 재고를 감소시키고 판매를 완료합니다.
            self.stock.update({order_type : self.stock.get(order_type) - int(order_amount)})  # 손님의 주문 내용을 기반으로 재고를 업데이트합니다.
            self.order.update({order_type : self.order.get(order_type) + int(order_amount)})
            print(f'주문하신 붕어빵은 {order_type} 이고 주문수량은 {order_amount} 입니다. 감사합니다.') # 판매가 완료된 경우 판매된 붕어빵 맛과 개수를 출력하세요.
        print(f'현재재고 : {self.stock}')
        print(f'오늘의 주문 : {self.order}')


###### 붕어빵 장사
bungeoppang = business()

while True:
    ### 작업선택
    work = input("작업을 선택 해주세요. (재고(1), 주문(2), 종료(3))")

    if work == "종료" or work == "3":
        sales = bungeoppang.order["팥붕어빵"] * 1000 + bungeoppang.order["슈크림붕어빵"] * 1200 + bungeoppang.order["초코붕어빵"] * 1500
        print(f'오늘 장사 끝! 오늘의 판매수량은 {bungeoppang.order} 총 매출은 : {sales}원 입니다.')
        break

    if work == "재고" or work == "1":
        print("관리자모드 - 재고관리입니다.")
        add_type = input("[재고] 붕어빵의 종류를 입력해주세요. (종류(팥붕어빵, 슈크림붕어빵, 초코붕어빵)")
        add_amount = input("붕어빵의 수량을 입력해주세요.")
        bungeoppang.admin_stock(add_type, add_amount)
    elif work == "주문" or work == "2":
        print("주문이 들어왔습니다!")
        order_type = input("[주문] 붕어빵의 종류를 입력해주세요. (종류 - 팥붕어빵, 슈크림붕어빵, 초코붕어빵)")
        order_amount = input("붕어빵의 수량을 입력해주세요.")
        bungeoppang.order_bungeoppang(order_type, order_amount)
    else:
        print("다시 입력해주세요!")
        continue

    