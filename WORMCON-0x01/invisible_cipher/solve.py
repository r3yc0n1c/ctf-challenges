#!/usr/bin/env python3
#!/usr/bin/env python3
from Crypto.Util.number import *
from collections import Counter

def rep(text, oldch, newch):
	return text.replace(oldch, newch, text.count(oldch))

def viz_us(pt):
	for ch in pt:
		if ch not in PTALPHA:
			pt = pt.replace(ch, '_')
	return pt

def viz_idx(pt, ct):
	for i, ch in enumerate(pt):
		if ch not in PTALPHA:
			pt = pt.replace(ch, f'({i:x})', 1)
	return pt


PTALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
enc_flag = open('flag.enc').read()

ctr = Counter(enc_flag).most_common()
# print(ctr)

let = ' ETA'#OIN'#SHRDLU'#CMFWYPVBGKJQXZ'
pt = enc_flag

for elem, l in zip(ctr[:len(let)],let):
	ch, n = elem
	# print(ch,n, l)
	pt = pt.replace(ch, l)

# substitute
pt = rep(pt, enc_flag[0x1], 'H')
pt = rep(pt, enc_flag[0x3], 'R')
pt = rep(pt, enc_flag[0x6], 'W')
pt = rep(pt, enc_flag[0x8], 'S')
pt = rep(pt, enc_flag[0x24], 'O')
pt = rep(pt, enc_flag[0x7c3], 'I')
pt = rep(pt, enc_flag[0xc5], 'D')
pt = rep(pt, enc_flag[0x79a], 'L')
pt = rep(pt, enc_flag[0x5c], 'N')
pt = rep(pt, enc_flag[0xc], 'C')
pt = rep(pt, enc_flag[0x7e1], 'U')
pt = rep(pt, enc_flag[0x802], 'B')
pt = rep(pt, enc_flag[0x803], 'M')
pt = rep(pt, enc_flag[0x764], 'F')
pt = rep(pt, enc_flag[0x791], 'P')
pt = rep(pt, enc_flag[0x153], 'Y')
pt = rep(pt, enc_flag[0x727], 'G')
pt = rep(pt, enc_flag[0x76b], 'Q')
pt = rep(pt, enc_flag[0x9b], 'K')
pt = rep(pt, enc_flag[0x2bb], 'V')
pt = rep(pt, enc_flag[0x7b3], 'J')
pt = rep(pt, enc_flag[0x460], 'X')


# visualize with _
# pt = viz_us(pt)
pt = viz_idx(pt, enc_flag)

print(pt)
