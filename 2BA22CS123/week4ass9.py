num_tuples = int(input("Enter the number of inner tuples: "))
tuple_of_tuples = []
for i in range(num_tuples):
    inner_tuple = tuple(input(f"Enter tuple {i+1} elements (comma-separated): ").split(','))
    tuple_of_tuples.append(inner_tuple)
element_to_check = input("Enter the element to check: ")
element_found = False
for tup in tuple_of_tuples:
    if element_to_check in tup:
        element_found = True
        break  
if element_found:
    print(f"The element '{element_to_check}' is found in the tuple of tuples.")
else:
    print(f"The element '{element_to_check}' is not found in the tuple of tuples.")
