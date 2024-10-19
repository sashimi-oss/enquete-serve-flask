from flask import Flask, render_template, request, jsonify
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)

@app.route('/')
def index():
  return 'Hello World'

@app.route('/enquete')
def enquete():
  return render_template('enquete.html')

@app.route('/process', methods=['POST'])
def process():
  return 'abc'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5001', debug=True)
#   app.run()