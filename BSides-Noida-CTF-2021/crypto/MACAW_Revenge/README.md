## MACAW Revenge

Macaw seeks revenge. <br>
`Connection` : `nc 34.121.95.29 1338` <br>
:arrow_down: [chall](dist/src.py)

## Solution
This service is vulnerable to AES CBC-MAC Length Extension Attack.

So, the attack goes like this (in general),
- Split the Forbidden Msg in AES BLOCKSIZE (16 bytes) chunks
- Generate auth tag (T) = MAC(M1) of the 1st block (M1) from the server
- Calculate M2 = next 16 bytes chunk and X = (T XOR M2 XOR IV) and send X to the server
- Get the forged tag which will be same as the Original Secret Tag, i.e. MAC(M1 || M2)
- Verify

For this challenge, you just have to send first two 16 bytes chunks ( M1 = Forbidden_Msg[:32] ) instead of one because the Forbidden Msg was of 48 bytes (three 16 bytes chunks).

#### Solve Script: [solve.py](soln/solve.py)
