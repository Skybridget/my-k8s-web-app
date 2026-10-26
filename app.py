from flask import Flask
app = Flask(__name__)

# ❌ 錯誤：@font_index_route('/')
#  正確：
@app.route('/')
def hello_world():
    return '<h1>GitOps 大成功！這是我自動更新的第二版網頁！</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
