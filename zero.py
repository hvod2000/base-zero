alphabet = open("alphabet.bin").read()
rev = {c: i for i, c in enumerate(alphabet)}
encode = lambda data: "".join((alphabet[b] for b in data))
decode = lambda data: (rev[c] for c in data)
