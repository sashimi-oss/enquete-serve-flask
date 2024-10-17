# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# @app.route('/')
# def index():
#   return 'Hello World'

# @app.route('/enquete')
# def enquete():
#   return render_template('enquete.html')

# @app.route('/process', methods=['POST'])
# def process():
#   return 'abc'

# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port='5001', debug=True)

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    # POSTリクエストからstart_numberとend_numberの値を取得
    start_number = int(request.form['start_number'])
    end_number = int(request.form['end_number'])
    
    results = []
    # start_numberとend_numberの範囲で処理を繰り返す
    for i in range(start_number, end_number + 1):
        # ここでstart_numberとend_numberを使って何らかの処理を行う
        result = f"実行結果{i}"
        # 結果をリストに追加
        results.append([i, result])
    
    # 処理結果をJSON形式で返す
    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
