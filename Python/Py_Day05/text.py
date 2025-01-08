# __BungeoppangShop 클래스__

# - __init__(): 초기 재고, 가격, 판매량을 설정합니다.
# - check_stock(): 현재 재고를 출력합니다.
# - process_order(): 주문을 처리하고 재고를 업데이트합니다.
# - admin_mode(): 관리자 모드에서 재고를 추가합니다.
# - calculate_total_sales(): 총 매출을 계산하고 출력합니다.

class BungeoppangShop:
    def __init__(self): # 현재재고
        self.stock = {"팥붕어빵":10, "슈크림붕어빵":8, "초코붕어빵":5}
        self.prices = {"팥붕어빵":1000, "슈크림붕어빵":1200, "초코붕어빵":1500}
        self.sales = {"팥붕어빵":0, "슈크림붕어빵":0, "초코붕어빵":0}

    def check_stock(self):  # 현재재고 확인용
        print(f'[재고/확인] 현재 재고는 {self.stock}')

    def process_order(self, bread_type, bread_count): # 주문처리
        print(f'[주문/접수] 고객님의 주문은 {bread_type} {bread_count}개 입니다.') # 주문을 확인한다.

        try: # 입력값 예외처리
            if self.stock.get(bread_type) >= bread_count: # 현재재고와 비교한다. (주문수량보다 재고가 많을 경우 // 주문 진행)                
                self.stock.update({bread_type : self.stock.get(bread_type) - bread_count}) # 현재재고업데이트 (현재재고 - 주문수량)
                self.sales.update({bread_type : self.sales.get(bread_type) + bread_count}) # 총주문수량업데이트 (총주문수량 + 현재주문수량)  
                print(f'[주문/완료] 주문해주셔서 감사합니다!')
                print(f'[재고/확인] 현재 주문 가능 수량은 {self.stock} 입니다!')
            else: # 현재재고와 비교한다. (주문수량보다 재고가 적을 경우 // 주문 미이행)
                print("[주문/재고부족] 재고수량이 부족합니다ㅠㅠ 다시 주문 해 주세요.")
                print(f'[재고/확인] 현재 주문 가능 수량은 {self.stock} 입니다!')
        except TypeError: # 붕어빵이름 및 수량 잘못입력 시 예외처리 발생
            print("[주문/오류] 주문을 다시 확인해주세요!")      
        except NameError: # 붕어빵이름 및 수량 잘못입력 시 예외처리 발생            
            print("[주문/오류] 주문을 다시 확인해주세요!")  

    def admin_mode(self, bread_type, additional_stock):
        print(f'[재고/추가] 추가된 재고는 {bread_type} {additional_stock}개 입니다.') # 추가된 재고를 확인한다.

        try: # 입력값 예외처리
            self.stock.update({bread_type : self.stock.get(bread_type) + additional_stock}) # 현재재고업데이트 (현재재고 + 추가된재고)
            print(f'[재고/확인] 현재 주문 가능 수량은 {self.stock} 입니다!')
        except TypeError: # 붕어빵이름 및 수량 잘못입력 시 예외처리 발생
            print("[재고/오류] 주문을 다시 확인해주세요!")      
        except NameError: # 붕어빵이름 및 수량 잘못입력 시 예외처리 발생            
            print("[재고/오류] 주문을 다시 확인해주세요!")  

work = BungeoppangShop()
work.check_stock()
work.process_order("팥붕어빵", 3)
work.admin_mode("초코붕어빵", 10)
