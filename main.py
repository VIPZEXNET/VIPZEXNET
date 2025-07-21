from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📥 پیام دریافت شد:", data)
    return "✅ دریافت شد", 200

if __name__ == '__main__':
    app.run()