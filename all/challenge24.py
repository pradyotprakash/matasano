import challenge10, challenge11, challenge21
from Crypto.Random import random

def initRng(seed):
	rng = challenge21.MT19937(seed & 0xFFFF)
	return rng

def MT19937Encrypt(rng, plaintext):
	remainingKeyBytes = ''	
	if len(plaintext) == 0:
		return ''

	keystream = remainingKeyBytes
	while len(keystream) < len(plaintext):
		keystream += str(rng.extract_number())

	if len(keystream) > len(plaintext):
		remainingKeyBytes = keystream[len(plaintext):]
		keystream = keystream[:len(plaintext)]

	return challenge10.xor(plaintext, keystream)

key = random.getrandbits(16)

def encryptionOracle(plaintext):
	prefix = challenge11.getRandomBytes(random.randint(10, 20))
	rng = initRng(key)
	return MT19937Encrypt(rng, prefix + plaintext)

def getKey(encryptionOracle):
	pt = 'A'*14
	ct = encryptionOracle(pt)
	prefixLength = len(ct) - len(pt)
	
	for i in range(2**16):
		rng = initRng(i)
		ct_ = MT19937Encrypt(rng, 'A'*len(ct))

		if ct_[prefixLength:] == ct[prefixLength:]:
			return i

print getKey(encryptionOracle)