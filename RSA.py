import random

def isPrime(x):
    i = 2
    while i*i < x:          # Only checks for factors up to the square root of x
        if x%i==0:
            return False
        i+=1
    return True

# Generates an n-digit prime number
def primeGenerator(n):
    string = ""
    for i in range(n):
        x=random.randint(1,9)
        string += str(x)
    number = int(string)

    if number%2==0:         # Eliminating even numbers
        number+=1

    while True:
        if isPrime(number):
            return number
        number+=2

# Finds the multiplicative inverse of a mod b
def pulverizer(a,b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = pulverizer(b % a, a)
        d = y - (b // a) * x
        return gcd, d, x

# Generates a secret key and a public key
def keyGen():
    numberOfDigits = 10
    p = primeGenerator(numberOfDigits)        # First random prime number
    q = primeGenerator(numberOfDigits)        # Second random prime number

    n = p*q
    r = (p-1)*(q-1)                           # Euler's Totient
    e = primeGenerator(numberOfDigits)**2     # A number that is highly likely to be relatively prime with r

    publicKey = (e,n)

    g, d, y = pulverizer(e,r)
    if d<0:
        d %= r

    secretKey = (d,n)

    return secretKey, publicKey

def encrypt(message, publicKey):
    (e,n) = publicKey
    encryptedMessage = []
    for letter in message:
        letter = ord(letter)
        encryptedLetter = pow(letter, e, n)
        encryptedMessage.append(encryptedLetter)

    return encryptedMessage

def decrypt(encryptedMessage, secretKey):
    (d,n) = secretKey
    originalMessage = ""

    for number in encryptedMessage:
        originalNumber = pow(number, d, n)
        originalMessage += chr(originalNumber)

    return originalMessage

def main():
    message = input("Input the message to encrypt: ")

    secretKey, publicKey = keyGen()

    encryptedMessage = encrypt(message,publicKey)

    print("\nEncrypted text:", encryptedMessage)
    print("\nThe secret key is:", secretKey)

    originalMessage = decrypt(encryptedMessage,secretKey)
    print("\nDecrypted Text:", originalMessage)

main()
