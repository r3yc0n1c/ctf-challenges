#!/usr/bin/env python3
from Crypto.Util.Padding import pad


def splitit(n):
	return (n >> 4), (n & 0xF)

def decrypt(cipher, key1, key2):
	flag = []
	for i, b in enumerate(cipher):
		m, l = splitit(b)
		if i%2 == 0:
			d = ((m ^ key1) << 4) | (l ^ key2)
		else:
			d = ((m ^ key2) << 4) | (l ^ key1)
		flag.append(d)
	return bytes(flag)


alpha = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
cipher = open('out.txt').read().split()[-1]
cipher = bytes.fromhex(cipher)

# Method 1
for otp in range(256):
	otpm, otpl = splitit(otp)

	flag = decrypt(cipher, otpm, otpl)
	if all(x in alpha for x in flag):
		print(flag)

# Method 2
# for f0 in alpha:
# 	fm, fl = splitit(f0)
# 	cm, cl = splitit(cipher[0])
# 	otpm = cm ^ fm
# 	otpl = cl ^ fl

# 	flag = decrypt(cipher, otpm, otpl)
# 	if all(x in alpha for x in flag):
# 		print(flag)
