import pymysql
import pymysql.cursors

# (1) db connection
connection = pymysql.connect(
    host = 'localhost',  # '127.0.0.1' 해도 됨
    user = 'root',
    password = '0701',
    db = 'classicmodels',
    charset = 'utf8mb4',  # emoji 사용할 수 있게 해줌
    cursorclass = pymysql.cursors.DictCursor  # dictcursor : 출력값이 dict형태로 반환된다.
    # cursors의 기본은 튜플임 속도가 빠르나 한계가 있다. json으로 변환의 어려움이 있다든지...
)

# (2) CRUD
## 1. SELECT * FROM
def get_customers():
    cursor = connection.cursor()  # cursor 혹은 cur 이라고도 많이 한다.

    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    #customers = cursor.fetchall() # 데이터가 전부 필요하다.
    customers = cursor.fetchone() # 데이터 하나만 필요하다.

    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])
    cursor.close()


## 2. INSERT INTO
def add_customer():
    cursor = connection.cursor()  # cursor 혹은 cur 이라고도 많이 한다.

    name = "yujin"
    family_name = "park"
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES(1005, '{name}', '{family_name}')"
    cursor.execute(sql)
    connection.commit()   # 쿼리를 실행한 결과가 있는데 이걸 데이터베이스에 반영을 해줘!
    cursor.close()

# add_customer()

## 3. UPDATE SET
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_yujin'
    contactLastName = 'update_park'

    sql = f"UPDATE customers SET customerName='{update_name}', contactLastName='{contactLastName}' WHERE customerNumber = 1005"
    
    cursor.execute(sql)
    connection.commit()  # select는 안해줘도 되지만, cud는 꼭 해줘야한다. 그래야 적용이 된다.
    cursor.close()  # 보안과 메모리 손실 등을 막기 위해서 항상 닫아준다.

# update_customer()

## 4. DELETE FROM
def delete_customer():
    curosr = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1005"  # safe mode 때문에 권한이 필요함
    curosr.execute(sql)
    connection.commit()
    curosr.close()

delete_customer()

