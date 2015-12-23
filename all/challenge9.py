def pad(block, blockLength):
	rem = blockLength - (len(block) % blockLength)
	ret = block + chr(rem)*rem
	assert len(ret) % blockLength == 0
	return ret
	
if __name__ == '__main__':
	print pad('1234567890123456', 16)