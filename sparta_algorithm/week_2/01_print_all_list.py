class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def print_all(self):
        print("hihihi")
        cur = self.head
        while  cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        for i in index:
            cur = cur.next
        return "index 번째 노드를 반환해보세요!"

linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()
