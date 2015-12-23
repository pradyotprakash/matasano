def paddingValidation(string, blockSize):
	if len(string) % blockSize != 0:
		raise Exception("Not PKCS#7 padding!")

	lastBlock = string[-16:]
	lastChar = lastBlock[-1]
	lastCharNum = ord(lastChar)

	if lastCharNum == 0:
		raise Exception("Not PKCS#7 padding!")

	i = lastCharNum - 1
	while i >= 0:
		if lastBlock[-(lastCharNum-i)] != lastChar:
			raise Exception("Not PKCS#7 padding!")
		i -= 1

	return string[:len(string)-lastCharNum]

if __name__ == '__main__':
	print paddingValidation('ICE ICE BABY1234\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 16)