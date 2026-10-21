# Builds index.html from the artifact source (which has no document shell).
import sys
src = sys.argv[1] if len(sys.argv) > 1 else 'game.html'
s = open(src).read()
head_end = s.index('</style>') + len('</style>')
doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="description" content="Worm World: turn-based third-person worm warfare for up to four laptops.">\n'
       + s[:head_end] + '\n</head>\n<body>\n' + s[head_end:] + '\n</body>\n</html>\n')
open('index.html', 'w').write(doc)
