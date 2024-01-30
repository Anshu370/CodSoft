import random

user_input = int(input("Enter Length of Your Password"))

caps = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'M', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

lower =['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', '|', ':', ';', '<', '>', '.', ' ?', '/']



pass_unverified = random.sample(caps, 26) + random.sample(lower, 10) + random.sample(num, 8) + random.sample(special, 9)
pass_verified = random.sample(pass_unverified, user_input)
print(''.join(pass_verified))
