from flask import Flask, render_template, request  # type: ignore
from utils import analyze_url  # นำเข้าฟังก์ชันจาก utils.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    risk = None
    if request.method == 'POST':
        url = request.form['url']  # ดึง URL จากฟอร์ม
        risk = analyze_url(url)  # วิเคราะห์ URL
    return render_template('index.html', risk=risk)

if __name__ == '__main__':
    app.run(debug=True)

