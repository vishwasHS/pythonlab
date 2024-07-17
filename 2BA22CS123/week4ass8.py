tuple_input = tuple(input("Enter a tuple of positive integers (comma-separated values): ").split(','))
tuple_of_integers = tuple(map(int, tuple_input))
result_integer = int(''.join(map(str, tuple_of_integers)))
print(f"The integer converted from the tuple {tuple_of_integers} is: {result_integer}")
