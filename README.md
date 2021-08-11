# ctf-challs
This repository contains all the source files and solutions related to the CTF Challenges I've created.

## Structure
```bash
├── ctf-name
│   └── challenge-name
│       ├── README.md
|       ├── src
│       |   ├── src.py
│       |   └── other source files
│       │
|       ├── dist
│       |   ├── src.py
│       |   ├── out.txt
│       |   └── other files for players
|       |
|       ├── deploy
│       |   ├── files
│       |   ├── Dockerfile
│       |   └── Other files for remote deployment
|       |
|       └── soln
|           ├── solve.*
|           └── other dependencies
|
└── README.md
```

For all the challenges, 
- `src` has the source code of the challenge.
- `dist` has the files to be distributed to the players during the CTF.
- `deploy` has files needed for remote deployment files.
- `soln` has the files needed to solve the challenge.

`* -> py, c, cpp, rs, etc.`

Feel free to point out the mistakes / optimizations that could have been done while writing these challenges!

