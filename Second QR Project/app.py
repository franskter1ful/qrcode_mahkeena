from flask import Flask, render_template, request
import qrcode 
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num_pairs = int(request.form['num_pairs'])
        return render_template('form.html', num_pairs=num_pairs)
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = {request.form[f'key{i}']: request.form[f'value{i}'] for i in range(int(request.form['num_pairs']))}
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(str(data))
    qr.make(fit=True)

    img = qr.make_image(fill='black', black_color='white')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return render_template('qr.html', img_data=img_str)

if __name__ == '__main__':
    app.run(debug=True)