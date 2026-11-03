from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="background:#101820;color:white;text-align:center;padding:20px">
    <h1>☀️ Welcome</h1>
    <img src="/static/sun.png" width="90%">
    <h3>مشاركة عنوان IP</h3>
    <p>عند الموافقة سيتم حفض الصورة.</p>
    <form action="/agree" method="post">
    <button>أوافق</button>
    </form>
    </body>
    </html>
    """

@app.route("/agree", methods=["POST"])
def agree():
    ip = request.remote_addr
    return f"<h2>عنوان IP الخاص باتصالك هو:</h2><h1>{ip}</h1>"

app.run(host="127.0.0.1", port=8080)
