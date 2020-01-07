import base64

# SIMPLE STRING ENCRYPT FUNCTION
def encryptBase64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

# SIMPLE STRING DECRYPT FUNCTION
def decryptBase64(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

# THIS IS THE STRING WE NEED TO ENCRYPT
message = "!@#$%^&*()"
print('Message is: ', message)

# THIS IS THE MESSAGE WE'RE GONNA ENCRYPT
encrypted_message = encryptBase64(message) # Call encrypt function and store into variable
print('Encrypted is: ', encrypted_message)

# THIS IS THE MESSAGE WE'RE GONNA DECRYPT
decrypted_message = decryptBase64(encrypted_message) # Call decrypt function and store into variable
print('Decrypted is: ', decrypted_message)

input('')
