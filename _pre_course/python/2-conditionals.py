age = 22

# > ; >= ; < ; <= ; != ; ==
if age >= 18 and age < 65:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

print("all done!")

if age >= 18 and age < 65:
    print("this is the same")

if 18 <= age < 65:
    print("as this")

if age >= 18:
    message = "eligible"
else:
    message = "not eligible"

# message = age >= 18 ? "eligible": "not eligible"
message = "eligiblie" if age >= 18 else "not eligible"

# Logical operators (and, or, not)

name = ""
if not name:
    print("helllo")

# Loops
# for x in "python":
#     print(x)

# for a in [a, b, c]:
#     print(a)

# for x in range(5):
#     print(x)

# for x in range(0, 10, 2):
#    print(x)

names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("not found")
