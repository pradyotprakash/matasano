def paddingValidation(string, blockSize):
	lastChar = string[-1]
	lastCharNum = ord(lastChar)

	if lastCharNum > blockSize:
		return string

	i = lastCharNum-1
	while i >= 0:
		if string[-(lastCharNum-i)] != lastChar:
			raise Exception("Not PKCS#7 padding!")
		i -= 1
		
	return string[:len(string)-lastCharNum]

if __name__ == '__main__':
	print paddingValidation('ICE ICE BABY', 16)