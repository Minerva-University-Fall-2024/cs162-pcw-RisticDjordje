# class BlankClass(object):
#     '''This is a Blank class for CS162.'''
#     pass

# t = BlankClass()

# class ClassWithAttr(object):
#     x1 = 1
#     x2 = 2

my_attr = ClassWithAttr()
my_attr.x3 = 3


print("Output of help(t):")
# help(t)  # Displays the docstring and information about the class

print("\nOutput of type(t):")
print(type(t))  # <class '__main__.BlankClass'>

print("\nOutput of dir(t):")
print(dir(t))  # Lists all the methods and attributes of the object

print("\nOutput of hash(t):")
print(hash(t))  # Returns the hash value of the object

print("\nOutput of id(t):")
print(id(t))  # Returns the id of the object

print("\nOutput of hasattr(my_attr, 'x3'):")
print(hasattr(my_attr, 'x3'))  # True

print("\nOutput of getattr(my_attr, 'x3'):")
print(getattr(my_attr, 'x3'))  # 3

print("\nOutput of delattr(my_attr, 'x3'):")
delattr(my_attr, 'x3')  # Deletes attribute x3 from my_attr
print(hasattr(my_attr, 'x3'))  # False

print("\nOutput of vars(my_attr):")
print(vars(my_attr))  # {}

print("\nOutput of bool(t):")
 print(bool(t))  # True
