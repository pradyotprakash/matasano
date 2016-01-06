#import challenge28

class HMAC:
	self.blocksize = 64
	self.hash_ = lambda x : '1'
	
	def __init__(self, key, message):
		if len(key) > self.blocksize:
			key = self.hash_(key)
		
		if len(key) < self.blocksize:
			key += '\x00' * (self.blocksize - len(key)

		oKeyPad = ''.join([chr(0x5c ^ ord(c)) for c in key])
		iKeyPad = ''.join([chr(0x36 ^ ord(c)) for c in key])
		
		return self.hash_(oKeyPad + self.hash_(iKeyPad + message))
		

if __name__ == '__main__':
	print HMAC('', '')
