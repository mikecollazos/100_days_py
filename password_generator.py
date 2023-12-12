import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


letter_list=[]
for i in range(0, nr_letters):
    print
    random_letter = random.randint(0,nr_letters)
    letter_list.append(letters[random_letter])

symbol_list=[]
for i in range(0, nr_symbols):
    random_symbol = random.randint(0,nr_symbols)
    symbol_list.append(symbols[random_symbol])

numbers_list=[]
for i in range(0, nr_letters):
    random_number = random.randint(0,nr_numbers)
    numbers_list.append(numbers[random_number])


password_list=letter_list + symbol_list + numbers_list
password=''.join(password_list)

#print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(password_list)
password=''.join(password_list)

print(f"your password is {password}")
