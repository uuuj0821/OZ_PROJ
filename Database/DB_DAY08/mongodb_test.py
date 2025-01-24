# from pymongo import MongoClient
# from datetime import datetime

# def insert_data():
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client.local  # 'local' 데이터베이스 사용

#     # 책 데이터 삽입
#     books = [
#         {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002},
#         {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987},
#         {"title": "1Q84", "author": "Haruki Murakami", "year": 2009}
#     ]
#     db.books.insert_many(books)

#     # 영화 데이터 삽입
#     movies = [
#         {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
#         {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
#         {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0}
#     ]
#     db.movies.insert_many(movies)

#     # 사용자 행동 데이터 삽입
#     user_actions = [
#         {"user_id": 1, "action": "click", "timestamp": datetime(2023, 4, 12, 8, 0)},
#         {"user_id": 1, "action": "view", "timestamp": datetime(2023, 4, 12, 9, 0)},
#         {"user_id": 2, "action": "purchase", "timestamp": datetime(2023, 4, 12, 10, 0)},
#     ]
#     db.user_actions.insert_many(user_actions)

#     print("Data inserted successfully")
#     client.close()

# # if __name__ == "__main__":
# #     insert_data()


# ####### 문제 1. 특정 장르의 책 찾기
# client = MongoClient('mongodb://localhost:27017/')
# db = client.local  # 'local' 데이터베이스 사용

# # def find_genre(db, genre):
# #     collection = db.books
# #     query = {"genre":genre}
# #     row = {"_id": 0, "title": 1, "author": 1}

# #     books = collection.find(row, query)
    
# #     for book in books:
# #         print(book)


# # print(find_genre(db, "fantasy"))

# # for data in db.books.find():
# #     print(data)

"""

Python Escape 11번 문제

문자열 enctypted를 2칸씩 건너뛰며 모든 문자를 처리했을 때의 출력값을 입력하세요.

"""


encrypted = "h3e2l4l6o1w5o7r9l8d0"
def decrypt_message(s):
    result = ""
    for i in range(0, len(s), 2):
        result += s[i]
    return result

output = decrypt_message(encrypted)
print("정답:", output)