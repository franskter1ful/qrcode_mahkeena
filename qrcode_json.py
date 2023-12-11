#The following script asks the user for key/value pairs to be saved to qrcode, then creates qrcode custom_qrcode.png in the directory

import segno
import json

def generate_custom_qrcode():
    num_pairs = int(input("Enter the number of key-value pairs you want to save:"))
    
    data = {}
    for i in range(num_pairs):
        key = input(f"Enter key name {i+i}: ")
        value = input(f"Enter value for '{key}': ")
        data[key] = value
    
    json_data = json.dumps(data)

    qr = segno.make(json_data)
    qr.save('custom_qrcode.png', scale=10)
    print("Customized QR code generated as 'custom_qrcode.png'")

if __name__ == "__main__":
    generate_custom_qrcode()

