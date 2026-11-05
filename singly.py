# Assessment 3.2 - Singly Linked List
# Algorithm: add each letter as a new node at the end (last node's next
# points to it), then remove the head and move head to its next node
# until the list is empty.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


last_name = input("Enter your last name: ").strip().upper()

if last_name == "":
    print("No last name entered.")
    raise SystemExit

head = None


def show(first):
    if first is None:
        return "empty"
    parts = []
    current = first
    while current is not None:
        parts.append(current.data)
        current = current.next
    return " -> ".join(parts) + " -> none"


print("\nADDING")
for letter in last_name:
    new_node = Node(letter)
    if head is None:
        head = new_node                  # first node becomes the head
    else:
        current = head
        while current.next is not None:  # go to the last node
            current = current.next
        current.next = new_node          # last node's next points to new node
    print(f"Add node {letter} -> {show(head)}")

print("\nREMOVING")
removal_order = []
while head is not None:
    removed = head.data
    removal_order.append(removed)
    head = head.next                     # head moves to its next node
    print(f"Remove head {removed} -> {show(head)}")

print("\nRemoval order:", ", ".join(removal_order))