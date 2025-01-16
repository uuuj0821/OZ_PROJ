import mysql.connector
from faker import Faker
import random  # 파이썬 기본 모듈

# (1) MYSQL 연결 설정
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0701',
    database='testdatabase'
)

# (2) MYSQL 연결
cursor = db_connection.cursor()
faker = Faker()


# 100명의 users 더미 데이터 생성
for _ in range(100):  # 변수생성 없이 100번의 반복을 할거야 -> _(언더바) 사용
    username = faker.user_name()  # user 이름을 랜덤으로 만듦
    # print(username)
    email = faker.email()

    sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
    values = (username, email)
    # print(sql)
    cursor.execute(sql, values)

# user_id 불러오기
# 잘못된 값이 들어오는걸 막기 위함
cursor.execute("SELECT user_id FROM users")
valid_user_id = [row[0] for row in cursor.fetchall()]  # 데이터를 전부 가져옴

# 100개의 주문 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)

        cursor.execute(sql, values)
    except:
        pass


db_connection.commit() # 이렇게해야 반영이 됨
cursor.close()
db_connection.close()