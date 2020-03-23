x = 1
print("Hello world")

# Variable Declarations
x, y = 1, 2
z = a = 3

integer = 100
float = 4.23
string = "hello there"
boolean = True

multiple_string = """
this is a multiline string
"""
# Ints
print(type(integer))
print(id(integer))
integer = 300
print(id(integer))

# Binary and Hex
b = 10
b = 0b10
b = 0x12c

print(bin(b))
print(hex(b))

b = 1 + 2j
print(b)

# Int Operators
3 + 2
3 - 2
3 * 2
3 / 2
3 // 2
3 % 2
3 ** 2

# Lists
py_list = [1, 2, 3]
py_list.append(4)

# Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:-2])
print(course[:-2])
print(course[1:])

first = "Ben"
last = "Basuni"
full = f"{first} {last}"
print(full)

# String Methods
abc = "helloworld"
abc.upper()
abc.lower()
abc.title()
abc.strip()  # lstrip, rstrip
abc.find("he")
abc.replace("h", "H")
print("world" in abc)
print("world" not in abc)
