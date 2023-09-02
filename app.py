import sys
import requests

data = sys.argv[1]
x = requests.get(f'https://api.qrserver.com/v1/create-qr-code/?size=100x100&data={data}');

try:
    with open('QR.png', 'wb') as f:
        for byte in x.content:
            f.write(byte.to_bytes(1, byteorder='big'))
        print('QR code generated successfully!');
except Exception as e:
    print(e);