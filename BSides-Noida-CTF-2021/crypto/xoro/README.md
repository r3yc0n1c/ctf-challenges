## Xoro

"You need to accept the fact that you’re not the best and have all the will to strive to be better than anyone you face." – Roronoa Zoro <br>
`Connection` : `nc 104.199.9.13 1338` <br>
:arrow_down: [chall](dist/src.py) 

## Solution

The Vulnerability lies in line 23 of the source file which allows us to send arbitrary input and recieve the encrypted flag with it.
```py
ct = encrypt(bytes.fromhex(pt) + FLAG, key)
```
So, the attack goes like this,

Case 1:
- Send **Null bytes** (32 bytes are enough)
- Recieve E(Null bytes || FLAG)
- The first 32 bytes will be the key
- XOR it with next 32 bytes to recover the FLAG

Case 2:
- Send any input  to the server (32 bytes are enough)
- Recieve E(input || FLAG)
- XOR our known plaintext with he first 32 bytes of the encrypted data to recover the key
- XOR it with next 32 bytes to recover the FLAG

#### Solve Script: [solve.py](soln/solve.py)
