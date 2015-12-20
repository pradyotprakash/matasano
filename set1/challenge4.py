# read from the english dictionary
words = []
with open('/usr/share/dict/words') as f:
	for x in f:
		words.append(x.strip())

words = set(words)

def score(string):
	w = string.split()
	return len(set(w) & words)

# find the best possible string by xoring with all possible characters
def operate(s):
	mx = -1
	index = ''
	for x in range(256):
		a = [hex(ord(a) ^ x)[2:] for a in s]
		a = ['0' + b if len(b) == 1 else b for b in a]
		t = ''.join(a).decode('hex')
		sc = score(t)

		if sc > mx:
			mx = sc
			index = t

	return index

# find the most probable string which has been xored
mx = -1
index = ''
with open('4.txt') as f:
	for row in f:
		s = row.strip().decode('hex')
		# print s
		s = operate(s)
		# print s
		sc = score(s)
		if sc > mx:
			mx = sc
			index = s

print index