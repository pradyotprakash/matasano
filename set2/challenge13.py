import challenge10, challenge11, challenge15

def decode(inp = 'foo=bar&baz=qux&zap=zazzle'):
	d = []
	temp = inp.split('&')
	for t in temp:
		y = t.split('=')
		d.append((y[0], y[1]))

	return d
	
def encode(inp):
	ret = ''
	for item in inp:
		ret += str(item[0]) + '=' + str(item[1]) + '&'

	return ret[:len(ret)-1]

def profile_for(email):
	d = [('email', email), ('uid', '10'), ('role', 'user')]
	return encode(d)

def encrypt(email):
	return challenge10.encryptECB(16, profile_for(email), key)

def decrypt(encrypted):
	ret = decode(challenge15.paddingValidation(challenge10.decryptECB(16, encrypted, key)))
	return ret

key = challenge11.getRandomBytes(16)

e1 = encrypt('abcd@wxyz.com')
e2 = encrypt('abc@xy.comadmin' + '\x0b'*11)

print decrypt(e1[:32] + e2[16:32])