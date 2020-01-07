# PYTHON-BASE64-FUNCTION


import base64

def encryptBase64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def decryptBase64(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

message = "!@#$%^&*()"
print('Message is: ', message)

encrypted_message = encryptBase64(message)
print('Encrypted is: ', encrypted_message)

decrypted_message = decryptBase64(encrypted_message)
print('Decrypted is: ', decrypted_message)
