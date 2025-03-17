n = int(input("Введите число:"))


def check_divisibility(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")

        else:
            print(i)


check_divisibility(n)
