import challenge10, challenge11

key = None
iv = None

def f1(string):
	global key, iv
	prefix = 'comment1=cooking%20MCs;userdata='
	suffix = ';comment2=%20like%20a%20pound%20of%20bacon'
	
	string = string.replace('=', '%3D').replace(';', '%3B')

	if key is None:
		key = challenge11.getRandomBytes(16)
	if iv is None:
		iv = challenge11.getRandomBytes(16)	

	return challenge10.encryptCBC(16, prefix + string + suffix, key, iv)

def f2(ct):
	string = challenge10.decryptCBC(16, ct, key, iv) # unpad the string later
	print string
	temp = string.split(';')
	for t in temp:
		u = t.split('=')
		if len(u) == 2 and u[0] == 'admin' and u[1] == 'true':
			return True
	return False

def f():
	prevlen = len(f1(''))
	for i in range(1, 16):
		l = len(f1('A'*i))
		if prevlen != l:
			break
		prevlen = l	
	totLen = prevlen - i

	# figure out the length of prefix, and focus on the block after that
	# ignore the above code for now
	a = list(f1(':admin<true:AAAA'))
	a[16] = chr(ord(a[16]) ^ 1)
	a[22] = chr(ord(a[22]) ^ 1)
	a[27] = chr(ord(a[27]) ^ 1)
	print f2(''.join(a))


if __name__ == '__main__':
	f()