#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import random


def splitn(text, size):
	return [text[i:i+size] for i in range(0,len(text),size)]


enc_flag = open('flag.png.enc', 'rb').read()
enc_ff = open('ff_error.png.enc', 'rb').read()
ff = open('ff_error.png', 'rb').read()

ff = splitn(ff, 8)
enc_ff = splitn(enc_ff, 8)
enc_flag = splitn(enc_flag, 8)

fp = [b'']*len(enc_flag)

for ct_block in enc_flag:
	i = enc_ff.index(ct_block)
	fp[i] = ff[i]

# print(fp[0].hex())

# unshuffle
sample = fp.copy()
ff0 = '89504e470d0a1a0a'
seed = bytes.fromhex(ff0)
random.seed(seed)
random.shuffle(sample)

rev_map = {}
for i,s in enumerate(sample):
	rev_map[i] = fp.index(s)
# print(rev_map)

flag = [b'']*len(enc_flag)
for i in rev_map:
	flag[rev_map[i]] = fp[i]

assert flag[0].hex() == ff0

flag = b''.join(flag)
open('recovered_flag.png', 'wb').write(flag)
