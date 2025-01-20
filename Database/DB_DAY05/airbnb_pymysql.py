import pymysql
import pymysql.cursors

## db connection
connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '0701',
    db = 'airbnb',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

with connection.cursor() as cursor: # connection.cursor()를 cursor로 부르겠다 아래 안에서는
    # 문제1: 새로운 제품 추가 (Python 스크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요. 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.)
    # sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ('Python Book', 10000, 10))
    # connection.commit() # select는 안해줘도 되지만, cud는 꼭 해줘야한다. 그래야 적용이 된다.


    # # 문제2: 고객 목록 조회 ('Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.)
    # cursor.execute("SELECT * FROM Products")
    # for book in cursor.fetchall(): # fetchall : 데이터를 전부 가져옴
    #     print(book)


    # 문제3: 제품 재고 업데이트 (제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.)
    # sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # cursor.execute(sql, (1, 1))
    # connection.commit()


    # 문제4: 고객별 총 주문 금액 ('Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.)
    # sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID"
    # cursor.execute(sql)
    # datas = cursor.fetchall()  # fetchall : 데이터를 전부 가져옴
    # print(datas)


    # 문제5 : 고객 이메일 업데이트 (고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.)
    # sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
    # cursor.execute(sql, ("update@update.com", 1))  # 항상 튜플로 남기!! 그래야 위의 %s에 하나씩 들어감!!
    # connection.commit()


    # 문제6 : 주문 취소 (주문을 취소하는 Python 스크립트를 작성하세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.)
    # sql = "DELETE FROM Orders WHERE orderID = %s"
    # cursor.execute(sql, (15))
    # connection.commit()


    # 문제7 : 특정 제품 검색 (제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.)
    # sql = "SELECT * FROM Products WHERE productName LIKE %s" # LIKE : 내가 입력한 단어가 포함되어있는 단어를 찾아줘 // = 을 쓰면 동일한 이름만 찾아주니까?
    # cursor.execute(sql, ("%Book%"))  # Book 이 들어간 모든 단어를 찾아주세요
    # datas = cursor.fetchall()

    # for data in datas:        
    #     print(data['productName'])


    # 문제8 : 특정 고객의 모든 주문 조회 (고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.)
    # sql = "SELECT * FROM Orders WHERE customerID = %s"
    # cursor.execute(sql, (1))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data)


    # 문제9 : 가장 많이 주문한 고객 찾기 ('Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.)
    sql1 = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID ORDER BY totalAmount DESC LIMIT 1"  # 주문 금액 제일 많은 사람
    sql2 = "SELECT customerID, COUNT(customerID) AS countOrders FROM Orders GROUP BY customerID ORDER BY countOrders DESC LIMIT 1" # 주문 횟수 제일 많은 사람
    sql3 = "SELECT customerID, COUNT(customerID) AS countOrders, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID ORDER BY customerID" # 고객별 총 주문금액, 주문수량 조회

    ### 따옴표
    sql3 = """
        SELECT customerID, COUNT(customerID) AS countOrders, SUM(totalAmount) AS totalAmount
        FROM Orders GROUP BY customerID
        ORDER BY customerID
        """


    cursor.execute(sql2)
    data = cursor.fetchone()  # 데이터가 1개니까 fetchone으로 불러옴 // 굳이 fecthall로 불러올 필요 없는듯?
    print(data)

cursor.close()
