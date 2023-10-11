class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def remove_head_node(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next
        self.print()

    def remove_last(self):
        if not self.head:
            return
        current = self.head
        while current.next.next:
            current = current.next

        current.next = None
        self.print()

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next

        current = self.head
        while current and current.next.data != data:
            current = current.next

        current.next = current.next.next

        self.print()

    def add_head_node(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node

        self.print()

    def add_at_index(self, index, data):
        if not self.head:
            return

        pos = 0
        if index == pos:
            self.add_head_node(data)
        else:
            current = self.head
            while current and pos + 1 != index:
                pos = pos + 1
                current = current.next

            if current:
                node = Node(data)
                node.next = current.next
                current.next = node
            else:
                print("Index not found")

    def remove_at_index(self, index):
        if not self.head:
            return

        pos = 0
        if pos == index:
            self.remove_head_node()
        else:
            curr = self.head
            while curr and pos + 1 != index:
                curr = curr.next
                pos = pos + 1

            if curr:
                curr.next = curr.next.next
            else:
                print("Index not found")

        self.print()

    def print(self):
        temp = self.head
        while temp:
            print(f"{temp.data}->", end="")
            temp = temp.next
        print("null\n")


def bubble_sort():
    a = [6, 2, 8, 9, 1, 2]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)


if __name__ == "__main__":
    llist = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        llist.add(i)

    llist.print()
    # llist.remove_at_index(2)
    # llist.remove(5)
    # llist.remove_first()
    # llist.remove_last()
    bubble_sort()
