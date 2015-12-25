# mtt.py
Command line utility for searching and playing movies or TV shows from http://movietv.to. Daily restrictions are avoided, and video is piped directly into VLC.  

Dependencies:  
nix `sudo pip install beautifulsoup4 click requests`  
win `python -m pip install beautifulsoup4 click requests`  

Usage:
```
> ./mtt.py --help
Usage: mtt.py [OPTIONS]

Options:
  --movie TEXT  Name of movie to find.
  --tv TEXT     Name of tv show to find.
  --help        Show this message and exit.

> ./mtt.py --movie "Lord of the Rings"
1. The Lord of the Rings: The Two Towers
2. The Lord of the Rings: The Fellowship of the Ring
3. The Lord of the Rings: The Return of the King
4. The Lord of the Rings
Movie #?: 2
```
