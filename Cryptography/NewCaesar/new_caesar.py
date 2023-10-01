import string

class NewCaesar:
    def __init__(self, flag: str, key: str):
        self.LOWERCASE_OFFSET = ord("a")
        self.ALPHABET = string.ascii_lowercase[:16]
        self.flag = flag
        self.key = key

    def b16_encode(self, plain):
        enc = ""
        for c in plain:
            binary = "{0:08b}".format(ord(c))
            enc += self.ALPHABET[int(binary[:4], 2)]
            enc += self.ALPHABET[int(binary[4:], 2)]
        return enc

    def shift(self, c, k):
        t1 = ord(c) - self.LOWERCASE_OFFSET
        t2 = ord(k) - self.LOWERCASE_OFFSET
        return self.ALPHABET[(t1 + t2) % len(self.ALPHABET)]

    def encrypt(self):
        b16 = self.b16_encode(self.flag)
        enc = ""
        for i, c in enumerate(b16):
            enc += self.shift(c, self.key[i % len(self.key)])
        return enc
