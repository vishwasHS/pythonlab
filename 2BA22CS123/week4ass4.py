
input_string = input("Enter the list elements separated by space: ")
lst = list(map(int, input_string.split()))
k = int(input("Enter the value of k to find the kth largest element: "))
if k <= 0 or k > len(lst):
    print("Invalid value of k. Please enter a valid value.")
else:
    sorted_lst = sorted(lst, reverse=True) 
    kth_largest = sorted_lst[k - 1]
    print(f"The {k}th largest element in the list is: {kth_largest}")
