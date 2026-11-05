# Assessment 3.2 - Stack (LIFO: Last In, First Out)
# Algorithm: append each letter on top of the stack, then pop the top
# letter until the stack is empty.

last_name = input("Enter your last name: ").strip().upper()

if last_name == "":
    print("No last name entered.")
    raise SystemExit

stack = []


def show(items):
    return ", ".join(items) if items else "empty"


print("\nADDING (bottom -> top)")
for letter in last_name:
    stack.append(letter)
    print(f"append({letter}) -> {show(stack)}")

print("\nREMOVING")
removal_order = []
while len(stack) > 0:
    removed = stack.pop()
    removal_order.append(removed)
    print(f"pop -> removes {removed} -> {show(stack)}")

print("\nRemoval order:", ", ".join(removal_order))