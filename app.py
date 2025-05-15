from flask import Flask, request, jsonify, render_template

import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').strip().lower()

    if '숭실대학교' in user_input:
        response = "숭실대학교는 1897년에 설립된 대한민국 최초의 근대대학 중 하나입니다."
    elif '교수님' in user_input and ('몇 명' in user_input or '얼마나' in user_input):
        response = "2024년 기준으로 약 400명 정도의 교수님이 재직 중입니다."
    elif '최고의 교수님' in user_input:
        response = "나는 정문선 교수님이라고 생각해!"
    else:
        response = "그건 네가 검색해봐."

    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ← 이 부분이 핵심!
    app.run(host='0.0.0.0', port=port)

