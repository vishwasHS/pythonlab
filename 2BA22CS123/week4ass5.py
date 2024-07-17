m = int(input("Enter the number of rows for matrix : "))
n = int(input("Enter the number of columns for matrix :"))

# Step 2: Initialize matrices A and B with user input
print("Enter elements for matrix A:")
matrix_A = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Enter element A[{i}][{j}]: "))
        row.append(element)
    matrix_A.append(row)

print("Enter elements for matrix B:")
matrix_B = []
for i in range(m):  # Rows of matrix B is equal to columns of matrix A
    row = []
    for j in range(n):
        element = int(input(f"Enter element B[{i}][{j}]: "))
        row.append(element)
    matrix_B.append(row)

a_identical=matrix_A==matrix_B
if a_identical:
    print("identical")
else:
    print("non idential")