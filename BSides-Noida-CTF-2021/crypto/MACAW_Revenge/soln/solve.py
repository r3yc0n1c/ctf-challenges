#!/usr/bin/env python3
from pwn import *

# p = remote("localhost", 1234)
p = remote("34.121.95.29", 1338)

target = bytes.fromhex(p.recvline().split()[-1].decode())

slice1 = target[:32].hex()

p.sendlineafter("Choice: ", "M")
p.sendlineafter("plaintext(hex): ", slice1)

tag1 = p.recvline().decode().split()[-1]
tag1 = bytes.fromhex(tag1)
iv = p.recvline().decode().split()[-1]
iv = bytes.fromhex(iv)

slice2 = xor(xor(tag1, target[32:]), iv).hex()

p.sendlineafter("Choice: ", "M")
p.sendlineafter("plaintext(hex): ", slice2)

tag2 = p.recvline().decode().split()[-1]

print("[+] Found secret_tag = ", tag2)

p.sendlineafter("Choice: ", "A")
p.sendlineafter("verify: ", tag2)

p.interactive()

# BSNoida{M4c4w5_4r3_pr3tty_l0ud}
