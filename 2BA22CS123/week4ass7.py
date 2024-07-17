n = int(input("Enter the number of tuples: "))
tuple_list = []
for i in range(n):
    tuple_input = tuple(input(f"Enter tuple {i+1} (comma-separated values): ").split(','))
    tuple_list.append(tuple_input)
new_value = input("Enter the new value to replace the last element with: ")
for i in range(n):
    temp_list = list(tuple_list[i])
    temp_list[-1] = new_value
    tuple_list[i] = tuple(temp_list)
print("Updated list of tuples with the last element replaced:")
for tup in tuple_list:
    print(tup)
