#Random password generator

#importing the required module
import random

#Declaring the letters/elements and length for the password
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}:?;"
pass_len = int(input("Enter the length of the password: "))

#Creating a random password
a = "".join(random.sample(password, pass_len))
print("Your password is: ", a)