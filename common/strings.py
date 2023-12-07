# https://stackoverflow.com/a/34445090
def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

def all_replacements(s : str, w : str, r : "list(str)"):
    "Produces all possible replacements of wildcard characters 'w' in string 's' from a list of replacements 'r'."
    c = s[0]
    l = len(s) == 1
    if c == w:
        for x in r:
            # Do not replace a wildcard with a wildcard.
            if x == w:
                continue
            if l:
                yield x
            else:
                for a in all_replacements(s[1:], w, r):
                    yield x + a 
    else:
        if l:
            yield c
        else:
            for a in all_replacements(s[1:], w, r):
                yield c + a
    