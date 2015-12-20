def pad(block, blockLength):
	rem = blockLength - (len(block) % blockLength)
	if rem == blockLength:
		return block
	else:
		return block + chr(rem)*rem