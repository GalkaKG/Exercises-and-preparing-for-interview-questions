class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    return prev  # New head of the reversed list

# Example Usage
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Create linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original List:")
print_list(head)

reversed_head = reverse_linked_list(head)

print("Reversed List:")
print_list(reversed_head)
