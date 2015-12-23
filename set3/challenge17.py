from Crypto.Random import random

strings = []
f = open('17.txt')
for row in f:
	strings.append(row.decode('base64'))

def f1():
	s = strings[random.randint(0, 9)]
	key = 