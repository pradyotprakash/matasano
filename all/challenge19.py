import challenge10, challenge11, challenge18
from challenge3 import charFrequencies

cts = []
key = challenge11.getRandomBytes(16)

for row in open('19.txt'):
	# cts.append(row.decode('base64'))
	cts.append(challenge18.encryptCTR(16, row.decode('base64'), key, '\x00'*8))
# print cts
def decryptBlock(blockNum, blockSize):

	blocks = [ct[blockNum*blockSize:(1+blockNum)*blockSize] for ct in cts]
	
	# all these blocks encrypted using the same key
	u = challenge10.xor(blocks[0], blocks[1])
	sentinel = 'the'
	for i in range(0, len(u)-len(sentinel)+1):
		print challenge10.xor(sentinel, u[i:i+len(sentinel)])

if __name__ == '__main__':
	decryptBlock(0, 16)