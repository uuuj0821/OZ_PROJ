from flask import Flask, request, Response

app = Flask(__name__) # 서버 구축

# 라우팅
@app.route("/") #메인페이지
def home():
    return "Hello, This is Main Page!"

@app.route("/about")    #주소/about 페이지
def about():
    return "This is about Page!"

@app.route("/company")    #주소/about 페이지
def company():
    return "This is company Page!"

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
# http://127.0.0.1:5000/user/uuuj0821 와 같이 넣어주면 됨
@app.route('/user/<username>')
def user_profile(username):
    return f'UserName : {username}'

@app.route('/number/<int:number>')
def number(number):
    return f'Number : {number}'

# POST 요청 날리는 법
# (1) postman
# (2) requests
import requests #pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(url=url, data=data)
    return Response("Successfully submitted", status=200)

@app.route('/submit', methods=['GET', 'POST', 'PUT', 'DELETE'])
def submit():
    print(request.method)

    if request.method == 'GET':
        print('GET method')

    if request.method == 'POST':
        print('****POST method***', request.data)

    return "success"

if __name__ == "__main__":
    #print("__name__", __name__)
    app.run()