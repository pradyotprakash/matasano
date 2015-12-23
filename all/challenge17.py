from Crypto.Random import random
import challenge10, challenge11, challenge15

key = None

strings = []
f = open('17.txt')
for row in f:
	strings.append(row.decode('base64'))

def f1():
	global key
	rand = random.randint(0, 9)
	s = strings[rand]
	if key is None:
		key = challenge11.getRandomBytes(16)

	iv = challenge11.getRandomBytes(16)
	
	return iv, challenge10.encryptCBC(16, s, key, iv)

def paddingOracle(ct, iv):
	pt = challenge10.decryptCBC(16, ct, key, iv)
	
	try:
		challenge15.paddingValidation(pt, 16)
		return True
	except Exception as e:
		return False

def decryptBlock(paddingOracle, iv, arg):
	l = len(arg)
	known = ''
	IVSuffix = ''
	IVPrefix = str(iv) if l == 16 else arg[-32:-16]

	for i in range(15, -1, -1):
		
		randBytes = 'a'*i
		k = chr(16 - i)
		
		for j in range(256):
			p = chr(j)
			
			prefix = randBytes + chr(ord(p) ^ ord(k) ^ ord(IVPrefix[-1])) + ''.join([chr(ord(k) ^ ord(x) ^ ord(y)) for x,y in zip(known, IVSuffix)])
			
			if l == 16:
				IV = prefix
				changedCt = arg
			else:
				IV = iv
				changedCt = arg[:-32] + prefix + arg[-16:]
			
			if paddingOracle(changedCt, IV):
				known = chr(j) + known
				IVSuffix = IVPrefix[-1] + IVSuffix
				IVPrefix = IVPrefix[:-1]
				break
			
	return known	


def decrypt(paddingOracle, iv, ct):
	known = ''
	for i in range(len(ct)/16):
		arg = ct if i == 0 else ct[:-i*16]

		known = decryptBlock(paddingOracle, iv, arg) + known
	
	return challenge15.paddingValidation(known, 16)

if __name__ == '__main__':
	a = f1()
	u = decrypt(paddingOracle, *a)
	print u