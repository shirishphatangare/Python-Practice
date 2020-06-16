import math
from functools import reduce

vector_add = lambda a,b: [x+y for x,y in zip(a, b)]
vector_subtract = lambda a,b: [x-y for x, y in zip(a, b)]
vector_multipy = lambda a,b: [x*y for x, y in zip(a, b)]
vector_sum_all = lambda vecs: reduce(vector_add, vecs)
vector_scalar_multiply = lambda a, v: [k*v for k in a]
vector_mean = lambda a: sum(a)/len(a)
vector_dot = lambda a, b: [i*j for i, j in zip(a, b)]
vector_sum_of_squares = lambda a: sum(vector_dot(a, a))
vector_magnitude = lambda a: math.sqrt(vector_sum_of_squares(a))
vector_squared_distance = lambda v, w: vector_sum_of_squares(vector_subtract(v, w))
vector_distance = lambda u, v: vector_magnitude(vector_subtract(u, v))

vec_1 = [1,2,3]
vec_2 = [4,5,6]
vec_3 = [7,8,9]
lst = [vec_1, vec_2, vec_3]

print(vector_sum_all(lst))

print(vector_add(vec_1, vec_2))
print(vector_subtract(vec_2, vec_1))
print(vector_multipy(vec_2, vec_1))

print(vector_scalar_multiply(vec_1, 3))
print(vector_dot(vec_1, vec_2))
print(vector_sum_of_squares(vec_1))
print(vector_mean(vec_1))
print(vector_magnitude(vec_1))
print(vector_squared_distance(vec_1, vec_2))
print(vector_distance(vec_1, vec_3))
