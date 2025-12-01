#Write a program to perform binary search using recursion
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, high, key)

arr = sorted(list(map(int, input("Enter sorted elements (space-separated): ").split())))
key = int(input("Enter the element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print(f"\nElement {key} found at index {result}.")
else:
    print(f"\nElement {key} not found in the list.")
