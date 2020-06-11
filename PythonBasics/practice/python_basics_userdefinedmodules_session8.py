#To use a module we need to import
from practice.util import MathModule as m

print("Multiply 23 and 32: ",m.multiply(23,32))
print("Subtract 23 and 32: ",m.sub(23,32))
print("Adding values 23,34,45,56,67: ",m.addMultiple(23,34,45,56,67))
print("Module Variable multiplicative_identity:",m.multiplicative_identity)

print("MathModule Functions:",dir(m))

#Properties of the module
print("MathModule Functions :multiply:",(m.multiply.__doc__))
print("Module File:",(m.__file__))
print("Name of the Module:",(m.__name__))
print("Caching of  Module:",(m.__cached__))
print("Package of  Module:",(m.__package__))
