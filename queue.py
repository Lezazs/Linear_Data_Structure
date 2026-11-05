# Assessment 3.2 - Queue (FIFO: First In, First Out)
# Algorithm: append each letter at the back of the queue, then popleft
# the letter at the front until the queue is empty.

from collections import deque

last_name = input("Enter your last name: ").strip().upper()

if last_name == "":
    print("No last name entered.")
    raise SystemExit

queue = deque()


def show(items):
    return ", ".join(items) if items else "empty"


print("\nADDING (front -> back)")
for letter in last_name:
    queue.append(letter)
    print(f"append({letter}) -> {show(queue)}")

print("\nREMOVING")
removal_order = []
while len(queue) > 0:
    removed = queue.popleft()
    removal_order.append(removed)
    print(f"popleft -> removes {removed} -> {show(queue)}")

print("\nRemoval order:", ", ".join(removal_order))