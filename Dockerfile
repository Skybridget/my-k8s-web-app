# 使用輕量級的 Python 基礎鏡像
FROM python:3.11-slim

# 設定容器內的工作目錄
WORKDIR /app

# 將本機的套件清單複製進容器並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製其餘的程式碼進容器
COPY . .

# 宣告容器會使用 5000 連接埠
EXPOSE 5000

# 容器啟動時執行的指令
CMD ["python", "app.py"]
