########################################
# Diffie-Hellman Key Exchange Project  #
# MAT 243                              #
# Group 10                             #
# Nick Greenlees & Spencer Guia        #
########################################

# Modules
from tkinter import *
import tkinter.messagebox

# Create the window
root = Tk()

# Title of project
root.title('Math 243 Project')

# Set window size
root.geometry('275x210')

# Make entrys and get information
label1 = Label( root, text="What is your first prime number? ")
E1 = Entry(root, bd =1)

label2 = Label( root, text="What is your second prime number? ")
E2 = Entry(root, bd =1)

label3 = Label( root, text="What is your first secret number? ")
S1 = Entry(root, bd =1)

label4 = Label( root, text="What is your second secret number? ")
S2 = Entry(root, bd =1)

# Math
def nickPart():
    # Check Input
    try:
        int(E1.get())
        int(E2.get())
        int(S1.get())
        int(S2.get())
    except ValueError:
        tkinter.messagebox.showinfo('Error', 'Please enter an integer')

    # Assign Variables
    p1 = int(E1.get())
    p2 = int(E2.get())
    a1 = int(S1.get())
    b1 = int(S2.get())

    # Prime Checker Function
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    # Check that P1 & P2 are prime
    if not is_prime(p1):
        tkinter.messagebox.showinfo('Error', 'First input is not prime')

    if not is_prime(p2):
        tkinter.messagebox.showinfo('Error', 'Second input is not prime')

    # Calculations
    # A2
    a2 = (p1 ** a1) % p2

    # B2
    b2 = (p1 ** b1) % p2

    # Secret Key
    secret_key = (b2 ** a1) % p2

    # Secret Key Check
    secret_key_check = (a2 ** b1) % p2

    # Output
    if secret_key != secret_key_check:
        tkinter.messagebox.showinfo('Error', 'Unknown Error')
    if is_prime(p1) & is_prime(p2):
        tkinter.messagebox.showinfo('Key', 'Your Secret Key is: ' + str(secret_key))

    # End Function nickPart()

# Define Submit button and tell it to run nicks command to get key
submit = Button(root, text ="Submit", command = nickPart)

# Pack everything and put it where you want it to be
label1.pack()
E1.pack()

label2.pack()
E2.pack()

label3.pack()
S1.pack()

label4.pack()
S2.pack()

submit.pack(side =BOTTOM)

# Start the program, Have at end
root.mainloop()
