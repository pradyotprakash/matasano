from Crypto.Cipher import AES

key = 'YELLOW SUBMARINE'
iv = '0'*16
data = open('7.txt').read().decode('base64')

aes = AES.new(key, AES.MODE_ECB)
print aes.decrypt(data)