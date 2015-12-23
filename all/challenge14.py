import challenge10, challenge11, challenge12
from Crypto.Random import random

def encryptionOracle(text):
	global prefix, key, suffix
	return challenge10.encryptECB(16, prefix + text + suffix, key)

def getBlocks(ct, bs):
	return [ct[i:i+bs] for i in range(0, len(ct), bs)]

def findBlockSize(encryptionOracle):
	return challenge12.guessBlockSize(encryptionOracle)

def getDifferingBlock(blocks1, blocks2):
	for i in range(len(blocks1)):
		if not blocks1[i] == blocks2[i]:
			return i

def findPrefixLength(encryptionOracle):
	bs = findBlockSize(encryptionOracle)

	e1 = encryptionOracle('')
	e2 = encryptionOracle('A')

	blocks1 = getBlocks(e1, bs)
	blocks2 = getBlocks(e2, bs)

	i = getDifferingBlock(blocks1, blocks2)
	
	for j in range(1, 17):
		e2 = encryptionOracle('A'*j)
		blocks2 = getBlocks(e2, bs)

		k = getDifferingBlock(blocks1, blocks2)
		
		if not k == i:
			return (i+1)*bs - j + 1
		blocks1 = blocks2

	return i*bs

def guessSaltAtIndex(encryptionOracle, concernedBlock, last15, extraPrefixLength, effectiveStartBlock):
	
	for i in range(256):
		s = 'A'*extraPrefixLength + last15 + chr(i)
		en = encryptionOracle(s)
		if en[effectiveStartBlock*16:(effectiveStartBlock + 1)*16] == concernedBlock:
			return chr(i)

def findSuffix(encryptionOracle):
	prefixLength = findPrefixLength(encryptionOracle)
	bs = findBlockSize(encryptionOracle)

	rem = prefixLength % bs
	if rem == 0:
		extraPrefixLength = 0
	else:
		extraPrefixLength = bs - rem
	effectiveStartBlock = (prefixLength + extraPrefixLength) / bs

	known = ''
	j = 0
	try:
		while j < 16:
			j = (bs-1) - len(known)%bs
			pad = 'A'*j
			
			whichBlock = (len(known) // bs) + effectiveStartBlock
			
			en = encryptionOracle(pad + 'A'*extraPrefixLength)
			concernedBlock = en[bs*whichBlock:bs*(whichBlock+1)]
			last15 = (pad + known)[-15:]
			known += guessSaltAtIndex(encryptionOracle, concernedBlock, last15, extraPrefixLength, effectiveStartBlock)
		return known	
	except Exception as e:
		return known

if __name__ == '__main__':
	suffix = """Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK""".decode('base64')

	key = challenge11.getRandomBytes(16)
	prefix = challenge11.getRandomBytes(random.randint(16, 48))
	
	print findSuffix(encryptionOracle)