'''
1. Create a Python Generator to generate the vowels. This should be a cyclic generator and will generate infinite list of vowels.
'''

from itertools import cycle
print("---------------Generate infinite sequence of vowles---------------------")

def generate_vowels():
    vowels_list = "aeiou"

    while True:
        for each in cycle(vowels_list):
            yield each

vowel_generator = generate_vowels()
print(vowel_generator.__next__())
print(vowel_generator.__next__())
print(vowel_generator.__next__())
print(vowel_generator.__next__())
print(vowel_generator.__next__())
print(vowel_generator.__next__())
print(vowel_generator.__next__())