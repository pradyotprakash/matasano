import challenge6, challenge11, challenge18

if __name__ == '__main__':
	cts = []
	key = challenge11.getRandomBytes(16)
	smallestCtLength = 100000

	for row in open('19.txt'):
		cts.append(challenge18.encryptCTR(16, row.decode('base64'), key, '\x00'*8))
		smallestCtLength = min(smallestCtLength, len(cts[-1]))

	truncatedCts = [ct[:smallestCtLength] for ct in cts]

	ret = challenge6.decryptVigenereCipher(''.join(truncatedCts), smallestCtLength+1)

	for i in range(0, len(ret), smallestCtLength):
		print ret[i:i+smallestCtLength]