#!/usr/bin/env python3
from pwn import *

# p = remote('localhost', 1234)
p = remote('104.199.9.13', 1338)

pt = '00'*32

p.sendlineafter('(hex)]>  ', pt)
ct = bytes.fromhex(p.recvline().decode().split()[-1])
key = ct[:32]
flag = xor(ct[32:], key)

print(flag)

p.interactive()

# BSNoida{how_can_you_break_THE_XOR_?!?!}
