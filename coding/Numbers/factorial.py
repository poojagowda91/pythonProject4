def fact(num):
    if num < 0:
        print("Not a factorial")
    elif num == 0:
        return 1  # Factorial of zero is 1
    else:
        return num * fact(num - 1)


result = fact(5)
if result:
    print(f"The factorial is: {result}")
