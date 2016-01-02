class MT19937:
	
	def lowest32(self, x):
		return int(0xFFFFFFFF & x)

	def __init__(self, seed):
		self.index = 624
		self.MT = [0]*624
				
		self.MT[0] = seed
		
		for i in range(1, 624):
			self.MT[i] = self.lowest32(1812433253 * (self.MT[i-1] ^ (self.MT[i-1] >> 30)) + i)

	def twist(self):

		for i in range(624):
			x = self.lowest32((self.MT[i] & 0x80000000) + (self.MT[(i+1) % 624] & 0x7fffffff))
			xA = x >> 1
			if x % 2 != 0:
				xA = xA ^ 0x9908B0DF

			self.MT[i] = self.MT[(i + 397) % 624] ^ xA
		
		self.index = 0

	def extract_number(self):
		
		if self.index >= 624:
			self.twist()

		y = self.MT[self.index]
		y = y ^ ((y >> 11) & 0xFFFFFFFF)
		y = y ^ ((y << 7) & 0x9D2C5680)
		y = y ^ ((y << 15) & 0xEFC60000)
		y = y ^ (y >> 18)

		self.index = self.index + 1
		return self.lowest32(y)

if __name__ == '__main__':
	x = MT19937(5489)
	print x.extract_number()