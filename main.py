class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_element(head):
    n = 0
    node = head
    while node:
        n += 1
        node = node.next

    if n <= 1:
        return None

    position = 2 * n // 3 - 1
    node = head
    for _ in range(position):
        node = node.next
    return node.value


head = Node(0, Node(1, Node(2, Node(3, Node(4)))))
print(find_element(head))  # 2
