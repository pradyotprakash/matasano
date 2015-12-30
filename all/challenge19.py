import challenge10, challenge11, challenge18, itertools
from challenge3 import charFrequencies

cts = []
key = challenge11.getRandomBytes(16)

for row in open('19.txt'):
	# cts.append(row.decode('base64'))
	cts.append(challenge18.encryptCTR(16, row.decode('base64'), key, '\x00'*8))

def getPrintableKeyChar(cts, i):
	for j in range(256):
		decrypted = [ord(x[i]) ^ j for x in cts]
		if all([chr(x) in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,' for x in decrypted]):
			yield j

def extendKey(k, ciphertext, guess):
	return k + ''.join([chr(guess[i] ^ ciphertext[len(k) + i]) for i in range(len(guess))])

def decryptBlock(blockNum, blockSize):

	blocks = [ct[blockNum*blockSize:(1+blockNum)*blockSize] for ct in cts]
	
	# all these blocks encrypted using the same key
	u = challenge10.xor(blocks[0], blocks[1])
	sentinel = 'the'
	for i in range(0, len(u)-len(sentinel)+1):
		print challenge10.xor(sentinel, u[i:i+len(sentinel)])

if __name__ == '__main__':
	# decryptBlock(0, 16)
	ks = [getPrintableKeyChar(cts, i) for i in range(10)]
	# print list(itertools.islice(itertools.product(*ks), 1))[0]
	k = list(itertools.islice(itertools.product(*ks), 1))[0]
	k = extendKey(k, cts[1], b'h ')
	k = extendKey(k, cts[3], b'entury ')
	k = extendKey(k, cts[5], b'ss ')
	k = extendKey(k, cts[3], b'se')
	k = extendKey(k, cts[5], b'rds')
	k = extendKey(k, cts[0], b' ')
	k = extendKey(k, cts[29], b'ght')
	k = extendKey(k, cts[4], b' ')
	k = extendKey(k, cts[27], b'd')
	k = extendKey(k, cts[4], b'ead')
	k = extendKey(k, cts[37], b'n,')
	kl = len(k)
	decrypted = [strxor(x[:kl], k[:len(x)]) + x[kl:] for x in cts]
	for i in range(len(decrypted)):
		if decrypted[i] != base64.b64decode(strings[i]):
			raise Exception('Invalid decryption')
		print decrypted[i]