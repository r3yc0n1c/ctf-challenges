#!/usr/bin/env python3
from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from pwn import *

# context.log_level = 'debug'
r = remote('localhost', 1234)
# r = remote('34.83.246.93', 8000)

"""
| [1] DH Parameters       |
| [2] View PublicKeys     |
| [3] Encrypt Flag        |
| [4] Generate PublicKey  |
"""

r.sendlineafter('? ', '1')
data = r.recvuntil('Choice').split()
g = int(data[4])
p = int(data[-2])

r.sendlineafter('? ', '2')
data = r.recvuntil('Choice').split()
R = int(data[4])
K = int(data[-2])

r.sendlineafter('? ', '3')
data = r.recvuntil('Choice').split()
enc_flag = data[4].decode()[1:-1]
iv = data[-2].decode()[1:-1]

l = p.bit_length() - 2
bits = ''

prog = log.progress('Found')

try:
	for n in range(l):
		mask = 2**n

		r.sendlineafter('? ', '4')
		r.sendlineafter('> ', str(mask))
		data = r.recvuntil('Choice').split()
		npk = int(data[-2])

		ge = pow(g, mask, p)
		if npk * ge % p == K:
			bits = '1' + bits
			# print(t.index(e), '-> 1')
		else:
			bits = '0' + bits
			# print(t.index(e), '-> 0')
		prog.status(f'({n}/{l}) : {bits}')

	# print(f"LEAK: {bits}")
	priveky = int(bits, 2)
	print(f"PRIV: {priveky}")

	s = pow(R,priveky,p)
	bs = AES.block_size
	key = SHA256.new(str(s).encode()).digest()[:bs]
	iv = bytes.fromhex(iv)
	cipher = AES.new(key, AES.MODE_CBC, iv)
	enc_flag = bytes.fromhex(enc_flag)
	flag = cipher.decrypt(enc_flag)
	print(flag)

except:
	r.interactive()

# wormcon{00p5!_n0_m45k_n0_FL4G}
