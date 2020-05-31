"""Keeps the modular operations."""


def is_prime(n):
    """Return True if n is prime, False otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(5, n//2):
        if n % i == 0:
            return False
    return True


def gcd(x, y):
    """Return the greatest common divisor found using euclidean method
    of x and y."""
    while y != 0:
        x, y = y, x % y
    return x


def generate_keys(p, q):
    """Return two parts of public key: n and small odd number e that
    is mutually prime with number (p-1) * (q-1)."""
    n = p * q
    number = (p-1) * (q-1)
    i = 7  # Iteration variable for finding e
    while True:
        if gcd(i, number) == 1:
            return n, i
        i += 2


def encrypt(message, n, e):
    """Return encrypted message."""
    message = message.replace(" ", "").upper()
    digital_string = "".join(str(ord(letter) - ord("A")).rjust(2, "0")
                             for letter in message)

    digits = "23"
    while int(digits+"23") < n:
        digits += "23"
    block_len = len(digits)

    blocks = [digital_string[i:i+block_len]
              for i in range(0, len(digital_string), block_len)]
    while len(blocks[-1])+2 <= block_len:
        blocks[-1] += "23"

    encrypted = " ".join(str(int(M.rstrip("0"))**e % n).rjust(block_len, "0")
                         for M in blocks)

    return encrypted
