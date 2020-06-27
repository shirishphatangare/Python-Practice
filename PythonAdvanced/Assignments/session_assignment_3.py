"""
3.Write a password generator in Python. Be creative with how you generate passwords - strong
passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The
passwords should be random, generating a new password every time the user asks for a new
password. Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word
or two from a list.

Strong password Rules:

1) Minimum 8 characters
2) Maximum 16 characters
2) At least one Uppercase
3) At least one number
4) At least one symbol

"""
from itertools import permutations, combinations
import random

menu = """ ----- Menu -------
    1) Strong Password (S)
    2) Weak Password (W)
    3) Quit (Q)
"""

lowercase = list(map(chr, range(97, 123)))
uppercase = list(map(chr, range(65, 90)))
symbols =  list(map(chr, range(33, 47)))

def generate_strong_password():
    common_list = []

    while True:
        common_list.append("".join(random.choices(lowercase,k=random.randrange(5,14))))
        common_list.append(str(random.randrange(10)))
        common_list.append(random.choice(uppercase))
        common_list.append((random.choice(symbols)))

        all_results = list(permutations(common_list,4))
        result = all_results[random.randrange(len(all_results))]

        strong_password = "".join(result)
        yield strong_password


def generate_weak_password():
    common_list = ['passw0rd','iloveyou','qwerty','secret','nothing','letmein','welcome','monkey','dragon','whatever','liberty']
    yield random.choice(common_list)

print(f"{menu}")
choice = input("Please Enter a choice (S/W/Q): ").casefold()


while choice != 'q':
    if choice == 's':
        print("Generated Strong Password is: ", end = " ")
        print(generate_strong_password().__next__())
    elif choice == 'w':
        print("Generated Weak Password is: ", end = " ")
        print(generate_weak_password().__next__())
    else:
        print("Wrong choice! Please select correct option (S/W)")

    #print('-' * 100)
    print(f"{menu}")
    choice = input("Please Enter a choice (S/W/Q): ").casefold()

