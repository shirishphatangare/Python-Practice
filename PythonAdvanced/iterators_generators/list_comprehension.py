#List comprehensions are a tool for transforming one list (any iterable actually)
# into another list. During this transformation, elements can be conditionally
# included in the new list and each element can be transformed as needed.

numbers=[2,3,5,4,9]
doubled_odds = list(map(lambda n: n * 2, filter(lambda n: n % 2 == 1, numbers)))
print(doubled_odds)
#Writing it in a different way
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
print(doubled_odds)

print("---------Example of List Transformation from For Loop---")
#Original For Loop
numbers = [1, 2, 3, 4, 5]
doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)
print("---For Loop:",doubled_odds)
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
print("--List Comprehension:",doubled_odds)

print("-------Unconditional Comprehensions-------------")
#original For Loop
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
for n in numbers:
    doubled_numbers.append(n * 2)
print("-----For Loop(Unconditional):",doubled_numbers)
#List Comprehension
doubled_numbers = [n * 2 for n in numbers]
print("-----List Comprehension(Unconditional):",doubled_numbers)

