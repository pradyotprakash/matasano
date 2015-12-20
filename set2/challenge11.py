from Crypto.Cipher import AES
from Crypto.Random import random
import challenge9, challenge10

def getRandomBytes(n):
	temp = bin(random.getrandbits(n*8))[2:]
	ret = ''
	
	for i in range(0, len(temp), 8):
		ret += chr(int(temp[i:i+8], 2))

	return ret

def appendRandomChars(text):
	return getRandomBytes(random.randint(5, 10)) + text + getRandomBytes(random.randint(5, 10))

def encryptionOracle(text):
	# generate a 16 byte key
	key = getRandomBytes(16)
	text = appendRandomChars(text)

	if random.getrandbits(1):
		# CBC if 1
		# print 'CBC'
		iv = getRandomBytes(16) # need to generate iv
		return challenge10.encryptCBC(16, text, key, iv)
	else:
		# ECB if 0
		# print 'ECB'
		return challenge10.encryptECB(16, text, key)

def modeDetector(encryptionOracle):
	text = 'a'*64
	ct = encryptionOracle(text)

	if ct[16:32] == ct[32:48]:
		print 'ECB mode'
	else:
		print 'CBC mode'

if __name__ == '__main__':
	modeDetector(encryptionOracle)