import challenge21, time
from Crypto.Random import random

wait = int(time.time())
wait += random.randint(40, 1000)

print 'Seed: ' + str(wait)

out = challenge21.MT19937(wait).extract_number()
print out

wait += random.randint(40, 1000)

for i in range(2000):
	t = wait - i
	if challenge21.MT19937(t).extract_number() == out:
		print 'Guessed seed: ' + str(t)