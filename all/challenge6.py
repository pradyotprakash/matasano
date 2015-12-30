import itertools, challenge3

data = open('6.txt').read().decode('base64')

def hamming(s1, s2):
	# assume len(s1) == len(s2)
	a = ''.join([bin(ord(a) ^ ord(b))[2:] for a,b in zip(s1, s2)])
	return a.count('1')

def normalizedHammingDistance(data, keysize):
	blocks = [data[i:i+keysize] for i in range(0, len(data), keysize)][0:4]
	combinations = list(itertools.combinations(blocks, 2))
	distances = [hamming(entry[0], entry[1]) for entry in combinations][0:6]
	
	return float(sum(distances))/(float(len(distances)) * keysize)

def decryptVigenereCipher(data, maxKeySize):
	keysizes = range(2, maxKeySize)
	keysizes.sort(key=lambda x:normalizedHammingDistance(data, x))
	# print keysizes
	keysizes = keysizes[0:1]

	for keysize in keysizes:
		print keysize
		blocks = [data[i:i+keysize] for i in range(0, len(data), keysize)]
		transpose = list(itertools.izip_longest(*blocks, fillvalue='0'))
		# print transpose
		decrypted = [challenge3.alternateUsingCharFreq(t) for t in transpose]
		decrypted = list(itertools.izip_longest(*decrypted, fillvalue='0'))
		
		# return decrypted
		return ''.join([''.join(d) for d in decrypted])
		

if __name__ == '__main__':
	print decryptVigenereCipher(data, 41)