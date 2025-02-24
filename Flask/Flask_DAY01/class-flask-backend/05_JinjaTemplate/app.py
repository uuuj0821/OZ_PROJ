from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # main page
def index():
    data = {
        'title' : 'Flask Jinja Template',
        'user' : 'yujin',
        'is_admin' : True,
        'item_list' : ['Item1', 'Item2', 'Item3']
    }

    # (1번째 파라미터) rendering할 html 파일명 입력
    # (2번째 파라미터) html로 넘겨줄 데이터 입력
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
