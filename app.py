import requests
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64
import time
from flask import Flask, render_template, request
import binascii

app = Flask(__name__)

def encrypt_values(plate_number, tin_number):
    start_time = time.time()
    timestamp = str(int(time.time()))
    key = SHA256.new(timestamp.encode()).digest()[:16]
    data = (plate_number + tin_number + timestamp).encode()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    encrypted_values = base64.b64encode(cipher.nonce + ciphertext + tag).decode()
    encryption_time = time.time() - start_time
    return encrypted_values, timestamp, encryption_time

def decrypt_values(encrypted_values, timestamp):
    start_time = time.time()
    key = SHA256.new(timestamp.encode()).digest()[:16]
    encrypted_values = base64.b64decode(encrypted_values.encode())
    nonce, ciphertext, tag = encrypted_values[:16], encrypted_values[16:-16], encrypted_values[-16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    decryption_time = time.time() - start_time
    return data.decode(), decryption_time

@app.route('/', methods=['GET', 'POST'])
def tp4917():
    if request.method == 'POST':
        plate_number = request.form.get('plate_number')
        tin_number = request.form.get('tin_number')
        url = "https://irembo.gov.rw/irembo/rest/public/police/request/retrieve/traffic-fines-by-plate-number-and-tin"
        headers = {
            'plateNumber': plate_number,
            'tin': tin_number
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        if data['status'] == False:
            response_message = data['message']
        else:
            if data['data']['numberOfTickets'] == 0:
                response_message = 'No traffic fines'
            else:
                response_message = 'You have a ticket'
        encrypted_values, timestamp, encryption_time = encrypt_values(plate_number, tin_number)
        decrypted_values, decryption_time = decrypt_values(encrypted_values, timestamp)
        delay = decryption_time - encryption_time
        key = SHA256.new(timestamp.encode()).digest()[:16]
        return render_template('index.html', response_message=response_message, encrypted_values=encrypted_values, decrypted_values=decrypted_values, encryption_time=encryption_time, decryption_time=decryption_time, delay=delay, key=binascii.hexlify(key), plate_number=plate_number, tin_number=tin_number)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)