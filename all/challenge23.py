import challenge21
from Crypto.Random import random

def get32bitBinary(x):
	ret = bin(x)[2:]
	return '0'*(32 - len(ret)) + ret

def undoLeftShiftXor(x, amount):
	ret = get32bitBinary(x & int('1'*amount, 2))
	x = get32bitBinary(x)

	for i in range(amount, 32):
		ret = ret[:-(i+1)] + str(int(x[-(i+1)]) ^ int(ret[-(i+1-amount)])) + ret[-i:]

	return int(ret, 2)

def undoRightShiftXor(x, amount):
	arg = int(get32bitBinary(x)[::-1], 2)
	ret = undoLeftShiftXor(arg, amount)
	
	return int(get32bitBinary(ret)[::-1], 2)

def undoLeftShiftXorAnd(x, amount, const):
	ret = get32bitBinary(x & int('1'*amount, 2))
	x = get32bitBinary(x)
	const = get32bitBinary(const)

	for i in range(amount, 32):
		ret = ret[:-(i+1)] + str(int(x[-(i+1)]) ^ (int(ret[-(i+1-amount)])) & int(const[-(i+1)])) + ret[-i:]

	return int(ret, 2)

def undoRightShiftXorAnd(x, amount, const):
	arg = int(get32bitBinary(x)[::-1], 2)
	const = int(get32bitBinary(const)[::-1], 2)
	ret = undoLeftShiftXorAnd(arg, amount, const)
	
	return int(get32bitBinary(ret)[::-1], 2)

def untemper(output):

	temp = undoRightShiftXor(output, 18)
	temp = undoLeftShiftXorAnd(temp, 15, 0xEFC60000)
	temp = undoLeftShiftXorAnd(temp, 7, 0x9D2C5680)
	temp = undoRightShiftXorAnd(temp, 11, 0xFFFFFFFF)

	return temp

if __name__ == '__main__':
	x = challenge21.MT19937(random.getrandbits(32))
	MT = [0]*624
	for i in range(624):
		MT[i] = untemper(x.extract_number())

	y = challenge21.MT19937(random.getrandbits(32))
	y.MT = MT

	for i in range(1000):
		if not x.extract_number() == y.extract_number():
			print 'Issue at index: ', i
			break
