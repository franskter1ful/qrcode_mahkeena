from flask import Flask, render_template, request
import segno
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    num_pairs = int(request.form['num_pairs'])
    data = {}

    for i in range(num_pairs):
        key = request.form[f'key_{i+1}']
        value = request.form[f'value_{i+1}']
        data[key] = value

    json_data = json.dumps(data)
    qr = segno.make(json_data)
    qr.save('static/custom_qrcode.png', scale=10)
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
