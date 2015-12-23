from Crypto.Cipher import AES
from Crypto.Random import random
import challenge10, challenge11

key = challenge11.getRandomBytes(16)

def encryptionOracle(text):
	global key
	suffix = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK""".decode('base64')


	return challenge10.encryptECB(16, text + suffix, key)

# guess block size
def guessBlockSize(encryptionOracle):
	l = len(encryptionOracle(''))
	bs = 1

	while True:
		en = encryptionOracle('A'*bs)
		if not len(en) == l:
			return len(en) - l
		bs += 1

def detectECB(encryptionOracle):
	bs = guessBlockSize(encryptionOracle)

	# print padBytes + bs*3
	s = 'A'*(bs*2)
	en = encryptionOracle(s)
	
	if en[0:bs] == en[bs:2*bs]:
		print 'ECB'
	else:
		print 'Something else'	

def guessSaltAtIndex(encryptionOracle, concernedBlock, last15):
	
	for i in range(256):
		s = last15 + chr(i)
		en = encryptionOracle(s)
		if en[:16] == concernedBlock:
			return chr(i)

def guessSalt(encryptionOracle):
	bs = guessBlockSize(encryptionOracle)

	known = ''
	j = 0
	try:
		while j < 16:
			j = (bs-1) - len(known)%bs
			pad = 'A'*j
			whichBlock = len(known) // bs
			en = encryptionOracle(pad)
			concernedBlock = en[bs*whichBlock:bs*(whichBlock+1)]

			last15 = (pad + known)[-15:]
			known += guessSaltAtIndex(encryptionOracle, concernedBlock, last15)
		return known	
	except Exception as e:
		return known

if __name__ == '__main__':
	print guessSalt(encryptionOracle)