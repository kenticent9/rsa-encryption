def is_prime(n):
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


def get_input():
    message = input("Enter a message: ")
    p = int(input("Please enter a prime number p: "))
    while not is_prime(p):
        p = int(input("Please enter a prime number p: "))
    q = int(input("Please enter a prime number q: "))
    while not is_prime(q):
        q = int(input("Please enter a prime number q: "))
    return message, p, q


def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def find_inverse(x, y):
    oldolds = 1
    olds = 0
    while y != 0:
        q = x // y
        r = x % y
        x = y
        y = r
        s = oldolds - q*olds
        oldolds = olds
        olds = s
    return oldolds


def generate_keys(p, q):
    n = p * q
    number = (p-1) * (q-1)
    i = 1
    while True:
        if gcd(i, number) == 1:
            e = i
            break
        i += 2
    d = find_inverse(e, number)
    return n, e, d


def replace(message, e, n):
    message = message.upper()
    replaced = ''.join(str(ord(letter) - ord("A")).rjust(2, "0")
                       for letter in message)
    a = ''.join(str(int(replaced[i:i+4].lstrip("0"))**e % n).rjust(4, "0")
                for i in range(0, len(replaced), 4))
    return a


def main():
    message, p, q = get_input()
    n, e, d = generate_keys(p, q)
    print(replace(message, e, n))


if __name__ == '__main__':
    main()
