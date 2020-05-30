'''
Module for implementing functions for:
checking if number is prime;
finding greates common divisor;
finding the inverse by mod m;
implementing degree elevation by mod m;
'''



def is_prime(num: int) -> bool:
    '''
    Checks if the num is prime using
    eratosthenes sieve
    '''

    assert num > 1, "Prime numbers should be > 1"

    arr = [True]*(num + 1)
    for ind in range(2, int(num**(1/2)) + 1):
        if arr[ind]:
            temp = ind**2
            while temp <= num:
                arr[temp] = False
                temp += ind
    return arr[-1]


def gcd(x: int, y: int) -> int:
    '''
    Function for finding greatest common divisor
    of x and y integers
    '''
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def find_inverse(x: int, y: int) -> int:
    '''
    Function, which implements
    extended euclidean algorithm for finding inverse to xmody num
    '''

    assert gcd(x, y) == 1, "Exists only if x and y are mutually prime"

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


def find_degree_mod(base: int, degree: int, divisor) -> int:
    '''
    Binary method for degree elevation
    '''
    x = 1
    binary = bin(degree)[2:][:: -1]
    power = base % divisor
    for i in map(int, binary):
        if i == 1:
            x = (x*power) % divisor
        power = (power ** 2) % divisor
    return x
