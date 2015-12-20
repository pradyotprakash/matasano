s1 = '1c0111001f010100061a024b53535009181c'.decode('hex')
s2 = '686974207468652062756c6c277320657965'.decode('hex')

p = ''.join([hex(ord(a) ^ ord(b))[2:] for a,b in zip(s1, s2)])
print p