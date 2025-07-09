import random
p = int(input())
q = int(input()) 

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    n = p*q
 
    phi = (p-1)*(q-1)


    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
        

def wide_gcd(a, b):
    r_old = a
    r = b
    x_old = 1
    x = 0
    y_old = 0
    y = 1
    while r != 0:
        q = r_old // r
        r_old, r = r, r_old - q*r
        x_old, x = x, x_old - q * x
        y_old, y = y, y_old - q * y

    return r_old, x_old, y_old

def multiplicative_inverse(e, phi):
    r_old, x_old, y_old = wide_gcd(e, phi)
    if r_old != 1:
        print('нет таких')
        return None
    else:
        d = x_old % phi
    return d