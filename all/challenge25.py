import challenge10, challenge11, challenge18

key = nonce = None
counter = 0

def do():
	global key, nonce
	if key is None:
		key = challenge11.getRandomBytes(16)
	if nonce is None:
		nonce = challenge11.getRandomBytes(16)

	data = open('25.txt').read().decode('base64')
	pt = challenge10.decryptECB(16, data, challenge18.key)
	
	return challenge18.encryptCTR(16, pt, key, nonce)


# need a copy to maintain state
def encryptCTR(blockSize, text, key, nonce):
	global counter
	
	ct = ''
	for i in range(0, len(text), blockSize):
		keystream = challenge10.encryptECB(16, nonce + challenge18.parseCounter(counter), key)

		block = text[i:i+blockSize]

		if len(block) == blockSize:
			ct += challenge10.xor(keystream, block)
		else:
			ct += challenge10.xor(keystream[:len(block)], block)

		counter += 1

	return ct

def edit(ct, offset, pt):
	encryptCTR(16, '0'* offset, key, nonce)
	return ct[:offset] + encryptCTR(16, pt, key, nonce)

ct = do()
pt = edit(ct, 0, ct)
print pt
