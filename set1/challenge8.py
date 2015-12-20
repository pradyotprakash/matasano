import itertools

count = 0
with open('8.txt') as f:
	for row in f:
		count += 1
		string = row.strip().decode('hex')
		
		t = [string[i:i+16] for i in range(0, len(string), 16)]
		combis = itertools.combinations(t, 2)
		if not sum([1 if pair[0] == pair[1] else 0 for pair in combis]) == 0:
			print count