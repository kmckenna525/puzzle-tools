_letterdiff = 96
_literals = ["=", " "]

def tonumber(val: chr) -> int:
    return ord(val.lower()) - _letterdiff

def wrap(val: int) -> int:
    return (val - 1) % 26 + 1

def toletter(val: int) -> str:
    return chr(wrap(val) + _letterdiff).upper()

def add(a: chr, b: chr) -> chr:
    return toletter(tonumber(a) + tonumber(b))

def addlines(a: str, b: str) -> str:
    tot = ""
    for i in range(min(len(a), len(b))):
        if a[i] in _literals:
            tot += a[i]
            continue
        if b[i] in _literals:
            tot += b[i]
            continue
        tot += add(a[i], b[i])
    return tot

def addfilecontents(a:str, b:str) -> str:
    tot = ""
    for i in range(min(len(a), len(b))):
        tot += addlines(a[i].strip(), b[i].strip()) + "\n"
    return tot

def sub(a: chr, b: chr) -> chr:
    return toletter(abs(tonumber(a) - tonumber(b)))

def sublines(a: str, b: str) -> str:
    tot = ""
    for i in range(min(len(a), len(b))):
        if a[i] in _literals:
            tot += a[i]
            continue
        if b[i] in _literals:
            tot += b[i]
            continue
        tot += sub(a[i], b[i])
    return tot

def subfilecontents(a:str, b:str) -> str:
    tot = ""
    for i in range(min(len(a), len(b))):
        tot += sublines(a[i].strip(), b[i].strip()) + "\n"
    return tot
