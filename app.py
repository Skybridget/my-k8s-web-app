from flask import Flask
app = Flask(__name__)

# ❌ 錯誤：@font_index_route('/')
#  正確：
@app.route('/')
def hello_world():
    return '<h1>Hello K8s and Argo CD! 這是我的第一個自製 GitOps 網頁！</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
