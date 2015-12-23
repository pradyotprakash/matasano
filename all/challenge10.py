from Crypto.Cipher import AES
import challenge9

def xor(s1, s2):
	t = [hex(ord(a) ^ ord(b))[2:] for a,b in zip(s1, s2)]
	t = ['0' + a if len(a) == 1 else a for a in t]
	return ''.join(t).decode('hex')

def encryptCBC(blockSize, text, key, iv):
	previousC = iv
	aes = AES.new(key, AES.MODE_ECB)

	text = challenge9.pad(text, blockSize)
	cipherText = ''

	for i in range(0, len(text), blockSize):
		p_i = text[i:i+blockSize]
		t_i = xor(p_i, previousC)
		c_i = aes.encrypt(t_i)
		previousC = c_i
		cipherText += c_i

	return cipherText

def decryptCBC(blockSize, text, key, iv):
	previousC = iv
	aes = AES.new(key, AES.MODE_ECB)

	plainText = ''

	for i in range(0, len(text), blockSize):
		c_i = text[i:i+blockSize]
		t_i = aes.decrypt(c_i)
		p_i = xor(t_i, previousC)
		previousC = c_i
		plainText += p_i

	return plainText

def encryptECB(blocksize, text, key):
	aes = AES.new(key, AES.MODE_ECB)
	text = challenge9.pad(text, blocksize)

	ct = ''
	for i in range(0, len(text), blocksize):
		pt = text[i:i+blocksize]
		ct += aes.encrypt(pt)

	return ct
	

def decryptECB(blocksize, text, key):
	aes = AES.new(key, AES.MODE_ECB)
	
	pt = ''
	for i in range(0, len(text), blocksize):
		ct = text[i:i+blocksize]
		pt += aes.decrypt(ct)
	
	return pt

if __name__ == '__main__':
	blockSize = 16
	text = 'Lay down and boogie and play that funky music till you die.'
	key = 'YELLOW SUBMARINE'
	iv = 'a'*blockSize
	
	ct = encryptCBC(blockSize, text, key, iv)
	pt = decryptCBC(blockSize, ct, key, iv)
	print pt