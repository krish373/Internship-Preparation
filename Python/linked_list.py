class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display(head):

    current = head
    count = 0

    while current:
        print(current.data)

        if current == head:
            print("The first node is:", current.data)

        if current.next is None:
            print("The last node is:", current.data)

        current = current.next
        count += 1

    print("Total nodes:", count)

first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

first.next = second
second.next = third
third.next = fourth
fourth.next = None

display(first)

insert_at_beg = int(input("Enter the value to insert at the beginning: "))
new_node = Node(insert_at_beg)
new_node.next = first
first = new_node

display(first)
insert_at_end = int(input("Enter the value to insert at the end: "))
last_node = Node(insert_at_end)

current = first
while current.next:
    current = current.next
current.next = last_node

display(first)

delete_value = int(input("Enter the value to delete: "))
current = first
previous = None
while current:
    if current.data == delete_value:
        if previous:
            previous.next = current.next
        else:
            first = current.next
        print("Deleted:", current.data)
        break
    

    previous = current
    current = current.next
else:
    print("Value not found: ", delete_value)

display(first)