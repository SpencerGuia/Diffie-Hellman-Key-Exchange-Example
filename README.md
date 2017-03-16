# Diffie-Hellman-Key-Exchange-Example
Example of Key Exchange generator in python

Programming Language
Python 3

About
We will be making a program in python that will take 4 inputs and produce a secret key crypto through the Diffie-Hellman key exchange. In addition, we will be making a GUI to accompany the program. 

Example / Explanation
Two prime numbers are produced, we’ll call them P1 and P2 (We will only be using smaller primes for our project).
P1 =  2
P2 = 3

Then a secret number is picked, we’ll call this A1, this number is not told to the other user, instead this user computes P1A1 mod P2 and sends the other user that answer which we will call A2
A1 = 5
25 mod 3 = 32 mod 3 = 2
A2 = 2

The other user does the same thing but with their own secret number which we’ll call B1 and B2. P1B1 mod P2
B1 = 7
27 mod 3 = 128 mod 3 = 2
B2 = 2

Now the both users use the number they were sent and compute the exact same operation. B2A1 mod P2 and A2B1 mod P2
25 mod 3 = 2
27 mod 3 = 2

That result, that number we both stumbled upon in the final steps, is our shared secret key. We can use that as our password for AES or Blowfish, or any other algorithm that uses shared secrets. And we can be certain that nobody else, nobody but us, knows that key that we created together.

(P1A1 mod P2)B1 mod P2 = P1A1B1 mod P2
(P1B1 mod P2)A1 mod P2 = P1B1A1 mod P2
