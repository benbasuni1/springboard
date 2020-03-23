def increment(number, by: int = 1) -> tuple:
    return (number + by)

# Tuple is a read only list


def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))


def save_user(**user):
    print(user["key"])


save_user(key=1, value="hello")


def fizzbuzz(input: int):
    if input % 5 == 0 and input % 3 == 0:
        return "Fizzbuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 == 0:
        return "Fizz"
    else:
        return input


print(fizzbuzz(2))
