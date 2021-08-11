## Damn Boi

`The DJ will play your Flag! <br>`

`Connection` : `nc 104.199.9.13 1338` <br>
:arrow_down: [chall](dist/chall.zip) 

## Solution

This is [Damgård–Jurik cryptosystem](https://en.wikipedia.org/wiki/Damg%C3%A5rd%E2%80%93Jurik_cryptosystem) ( the generalization of the 
[Paillier Cryptosystem](https://en.wikipedia.org/wiki/Paillier_cryptosystem) )

If we look closely, we can observe that the Prime Generation Algorithm is vulnerable to [ROCA vulnerability](https://en.wikipedia.org/wiki/ROCA_vulnerability) where the primes
are in this form:

<p align="center">
    k * M + (65537<sup>a</sup> mod M)
</p>

where **M** is a [Primorial](https://en.wikipedia.org/wiki/Primorial) and **k, a** are constants

Here, our primes are in the form:

<p align="center">
    (65537<sup>a</sup> mod M)  , k = 0
</p>

Therefore, we can factor **N** using ***ROCA Attack*** which is based on ***Coppersmith method***. After this, we just have to decrypt the Ciphertexts and get flag!

#### Solve Script: [solve.py](soln/solve.py)

## Ref
- [The Return of Coppersmith's Attack](https://crocs.fi.muni.cz/_media/public/papers/nemec_roca_ccs17_preprint.pdf)
- [A Generalisation, a Simplification and some Applications of Paillier's Probabilistic Public-Key System](https://www.brics.dk/RS/00/45/BRICS-RS-00-45.pdf)
