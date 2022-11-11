import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


alphabets = []
for letter in range(nr_letters):
  randstr = random.choice(letters)
  alphabets.append(randstr)


integers = []
for Num in range(nr_numbers):
  randnum = random.choice(numbers)
  integers.append(randnum)

symbol = []
for symb in range(nr_symbols):
  randsymb = random.choice(symbols)
  symbol.append(randsymb)

password = []

password.extend(alphabets)
password.extend(symbol)
password.extend(integers)


Strongpassword = ""

for Pass in password:
  rand = random.choice(password)
  Strongpassword = Strongpassword + rand

print(Strongpassword)
