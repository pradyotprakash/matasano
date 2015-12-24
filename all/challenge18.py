import challenge10

s = 'L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ=='.decode('base64')
key = 'YELLOW SUBMARINE'

def encryptCTR(blockSize, text, key, nonce):
	ct = ''
	counter = 0
	for i in range(0, len(text), blockSize):
		keystream = challenge10.encryptECB(16, nonce + parseCounter(counter), key)

		block = text[i:i+blockSize]

		if len(block) == blockSize:
			ct += challenge10.xor(keystream, block)
		else:
			ct += challenge10.xor(keystream[:len(block)], block)

		counter += 1

	return ct

def decryptCTR(blockSize, text, key, nonce):
	pt = ''
	counter = 0
	for i in range(0, len(text), blockSize):
		keystream = challenge10.encryptECB(16, nonce + parseCounter(counter), key)

		block = text[i:i+blockSize]

		if len(block) == blockSize:
			pt += challenge10.xor(keystream, block)
		else:
			pt += challenge10.xor(keystream[:len(block)], block)

		counter += 1

	return pt	

def parseCounter(counter):
	temp = str(counter)
	l = 8 - len(temp)

	ret = '0'*l + temp
	return ''.join([chr(ord(i)-48) for i in ret])[::-1]

if __name__ == '__main__':
	t = 'Mera joota jai japani!'
	en = encryptCTR(16, t, key, '\x00'*8)
	print decryptCTR(16, s, key, '\x00'*8)