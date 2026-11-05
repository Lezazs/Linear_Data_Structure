# Assessment 3.2 - Array
# Algorithm: add each letter at the next open index, then remove the
# element at the last index until the array is empty.

last_name = input("Enter your last name: ").strip().upper()

if last_name == "":
    print("No last name entered.")
    raise SystemExit

array = []


def show(arr):
    return "[" + ", ".join(arr) + "]" if arr else "[ ] (empty)"


print("\nADDING")
for letter in last_name:
    array.append(letter)
    print(f"Add {letter} at index {len(array) - 1} -> {show(array)}")

print("\nREMOVING")
while len(array) > 0:
    index = len(array) - 1          # last index
    removed = array[index]
    del array[index]
    print(f"Remove {removed} from index {index} -> {show(array)}")

print("\nRemoval order:", ", ".join(reversed(last_name)))