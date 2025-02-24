from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # main page
def index():
    title = '사용자 목록'
    users = [
        {"username": "traveler", "name": "Alex"},
        {"username": "photographer", "name": "Sam"},
        {"username": "gourmet", "name": "Chris"}
    ]

    return render_template('index.html', title=title, users=users)

if __name__ == "__main__":
    app.run(debug=True)
