# Assessment 3.2 - Doubly Linked List
# Algorithm: add each letter as a new node at the tail (old tail's next
# points to it, new node's prev points back), then remove the tail, move
# the tail back using prev, and set the new tail's next to none until
# the list is empty.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


last_name = input("Enter your last name: ").strip().upper()

if last_name == "":
    print("No last name entered.")
    raise SystemExit

head = None
tail = None


def show(first):
    if first is None:
        return "empty"
    parts = []
    current = first
    while current is not None:
        parts.append(current.data)
        current = current.next
    return " <-> ".join(parts)


print("\nADDING")
for letter in last_name:
    new_node = Node(letter)
    if head is None:
        head = new_node                  # head and tail are the same node
        tail = new_node
    else:
        tail.next = new_node             # old tail's next -> new node
        new_node.prev = tail             # new node's prev -> old tail
        tail = new_node                  # new node becomes the tail
    print(f"Add node {letter} -> {show(head)}")

print("\nREMOVING")
removal_order = []
while tail is not None:
    removed = tail.data
    removal_order.append(removed)
    tail = tail.prev                     # tail moves back using prev
    if tail is not None:
        tail.next = None                 # new tail's next is none
    else:
        head = None                      # list is now empty
    print(f"Remove tail {removed} -> {show(head)}")

print("\nRemoval order:", ", ".join(removal_order))