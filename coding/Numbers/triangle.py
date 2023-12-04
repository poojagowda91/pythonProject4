def triangleofstars(n=5):
    for i in range(1, n + 1):
        print('*' * i)


def triangleofnumbers(n=5):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


triangleofstars()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
triangleofnumbers()
