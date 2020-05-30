'''
RSA Encryption module
'''

from additional_functions import gcd, find_degree_mod, find_inverse, is_prime


def generate_keys(p: int, q: int) -> tuple:
    '''
    Function, which returns a tuple of
    n number, public and private keys
    '''
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


def encode(message: str, e: int, n: int) -> str:
    '''
    Function for encoding the message
    '''
    if len(message) % 2 == 1:
        message += "a"
    message = message.upper()
    replaced = ''.join(str(ord(letter) - ord("A")).rjust(2, "0")
                       for letter in message)
    encoded = ''.join(str(find_degree_mod(int(replaced[i:i+4].lstrip("0")), e, n)).rjust(4, "0")
                      for i in range(0, len(replaced), 4))
    return encoded


def get_input() -> tuple:
    '''Read user input'''
    message = input("Enter a message: ")
    while True:
        try:
            p = int(input("Please enter a prime number p: "))
            if is_prime(p):
                break
        except TypeError:
            continue
    while True:
        try:
            q = int(input("Please enter a prime number q: "))
            if is_prime(q):
                break
        except TypeError:
            continue

    return message, p, q


def main() -> None:
    '''
    Runs the main program
    '''
    message, p, q = get_input()
    n, e, _ = generate_keys(p, q)
    print(encode(message, e, n))


if __name__ == '__main__':
    main()
