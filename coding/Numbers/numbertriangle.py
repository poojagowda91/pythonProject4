class Triangle:
    def num_triangle(self, rows=5):
        for i in range(1, rows + 1):
            print((str(i) + ' ') * i)

    def num_triangle2(self, rows=5):
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    def num_triangle3(self, rows=5):
        for i in range(5, 0, -1):  # Outer loop for the number of rows
            for j in range(i, 6):  # Inner loop for printing the numbers
                print(j, end=" ")
            print()  # Move to the next line after printing each row

    def num_triangle4(self, rows=5):
        for i in range(5, 0, -1):  # Outer loop for the number of rows
            for j in range(i, 6):  # Inner loop for printing the numbers
                print(i, end=" ")
            print()  # Move to the next line after printing each row

    def print_equilateral_triangle_pattern(self):
        for i in range(1, 6):  # Outer loop for the number of rows
            for j in range(5, i - 1, -1):  # Inner loop for spaces before the numbers
                print(" ", end='')
            for k in range(i, 0, -1):  # Inner loop for printing the numbers
                print(k, end='')
            print()  # Move to the next line after printing each row

    # Call the function to print the equilateral triangle pattern
    def pattern(self,n):
        # Running the 1st loop for the number of rows, so n times.
        for i in range(n):
            # 2nd loop for printing spaces in front of the stars
            for j in range(n - i - 1):
                print(" ", end=" ")

            # 3rd loop for printing stars
            for star in range(i + 1):
                print("*", end=" ")

            # Printing a new line after the end of each row
            print()


# Create an instance of the Triangle class
triangle = Triangle()

# Call the num_triangle method with the default number of rows (5)
triangle.num_triangle()
triangle.num_triangle2()
triangle.num_triangle3()
triangle.num_triangle4()
triangle.print_equilateral_triangle_pattern()
triangle.pattern(6)
