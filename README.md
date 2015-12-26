# mtt.py
Command line utility for searching and playing movies from http://movietv.to. Daily restrictions are avoided, and the video is piped directly into VLC to avoid flash. Tested on Windows and Linux.  

Dependencies:  
python 2.7, VLC, beautifulsoup4, click, requests  
Linux   - `sudo pip install beautifulsoup4 click requests`  
Windows - `python -m pip install beautifulsoup4 click requests`  

Usage:
```> python mtt.py --help
Usage: mtt.py [OPTIONS]

Options:
  --movie TEXT  Name of movie to find.
  --help        Show this message and exit.

> python mtt.py --movie "Lord of the Rings"
1. The Lord of the Rings: The Two Towers
2. The Lord of the Rings: The Fellowship of the Ring
3. The Lord of the Rings: The Return of the King
4. The Lord of the Rings
Movie #?: 2```
