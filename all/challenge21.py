class MT19937:
	
	def lowest32(self, x):
		return int(0xFFFFFFFF & x)

	def __init__(self, seed):
		self.n = 624
		self.lower_mask = (1 << 31) - 1
		self.upper_mask = self.lowest32(not(self.lower_mask))
		
		self.MT = [0]*self.n
		
		self.index = self.n
		
		self.MT[0] = seed
		
		for i in range(1, self.n):
			self.MT[i] = self.lowest32(1812433253 * (self.MT[i-1] ^ (self.MT[i-1] >> 30)) + i)

	def twist(self):
		
		for i in range(self.n):
			x = (self.MT[i] & self.upper_mask) + (self.MT[(i+1) % self.n] ^ self.lower_mask)
			xA = x >> 1
			if x % 2 != 0:
				xA = xA ^ 0x9908B0DF16

			self.MT[i] = self.MT[(i + 397) % self.n] ^ xA
		
		self.index = 0


	def extract_number(self):
		
		if self.index >= self.n:
			self.twist()

		y = self.MT[self.index]					
		y = y ^ ((y >> 11) & 0xFFFFFFFF16)
		y = y ^ ((y << 7) & 0x9D2C568016)
		y = y ^ ((y << 15) & 0xEFC6000016)
		y = y ^ (y >> 18)

		self.index = self.index + 1
		return self.lowest32(y)

if __name__ == '__main__':
	print MT19937(23).extract_number()