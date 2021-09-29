import random

def isPrime(x):
    for i in range(2, (x//2)+1):
        if x%i==0:
            return False
    return True

# Generates an n-digit prime number
def primeGenerator(n):
    string = ""
    for i in range(n):
        x=random.randint(1,9)
        string += str(x)
    number = int(string)

    if number%2==0:
        number+=1

    while True:
        if isPrime(number):
            return number
        number+=2

# Finds the GCD of x and y using Euclid's Algorithm
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

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
    numberOfDigits = 3
    p = primeGenerator(numberOfDigits)        # First random prime number
    q = primeGenerator(numberOfDigits)        # Second random prime number

    n = p*q
    r = (p-1)*(q-1)              # Euler's Totient
    e = primeGenerator(numberOfDigits)**2     # A number that is highly likely to be relatively prime with r

    publicKey = (e,n)

    g, d, y = pulverizer(e,r)
    if d<0:
        d %= r

    secretKey = (d,n)

    return secretKey, publicKey

def encrypt(message, publicKey):
    e,n = publicKey
    encryptedMessage = []
    for letter in message:
        letter = ord(letter)
        if gcd(letter,n) != 1:
            raise Exception('UNEXPECTED ERROR, TRY AGAIN')  # For security, but highly unlikely to happen

        encryptedLetter = (letter**e)%n
        encryptedMessage.append(encryptedLetter)

    return encryptedMessage

def decrypt(encryptedMessage, secretKey):
    d,n = secretKey
    originalMessage = ""

    for number in encryptedMessage:
        number = int(number)
        originalNumber = (number**d)%n

        originalMessage += chr(originalNumber)

    return originalMessage

def main():
    secretKey, publicKey = keyGen()

    message = input("Input the message to encrypt: ")
    encryptedMessage = encrypt(message,publicKey)
    print('*'*100)
    print("Encrypted text:", encryptedMessage)
    print("The secret key is:", secretKey)

    originalMessage = decrypt(encryptedMessage,secretKey)
    print("Original Text:", originalMessage)

main()
