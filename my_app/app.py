from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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