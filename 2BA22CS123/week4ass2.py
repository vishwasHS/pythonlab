# Create an empty stack
stack = []

# Read number of integers
n = int(input("Enter the number of integers to push onto the stack: "))

# Push integers onto the stack
for i in range(n):
    value = int(input("Enter an integer: "))
    stack.append(value)
    print(f"Pushed {value} onto the stack")

# Display the stack
print("Stack elements are:")
for i in reversed(stack):
    print(i)
print(f"Stack length: {len(stack)}")

# Pop elements from the stack
while stack:
    value = stack.pop()
    print(f"Popped {value} from the stack")

# Display the stack after popping all elements
if not stack:
    print("Stack is now empty.")
else:
    print("Stack elements are:")
    for element in reversed(stack):
        print(element)
    print(f"Stack length: {len(stack)}")
