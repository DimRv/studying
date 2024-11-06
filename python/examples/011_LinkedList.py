"""Linked List - структуда данных в которой элементы (Nodes) имеют связи с соседними эдементами"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, data=None):
        self.head = None
        if data:
            node = Node(data[0])
            self.head = node
            for elem in data[1:]:
                node.next = Node(elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_first(self, value):
        node = self.head
        self.head = Node(value)
        self.head.next = node

    def add_last(self, value):
        node = self.head
        if node is None:
            self.head = Node(value)
            return
        while node.next:
            node = node.next
        node.next = Node(value)

    def add_between(self, value, val1, val2):
        node = self.head
        while node:
            if node.value == val1 and node.next.value == val2:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
        raise Exception(f"No Match Value Found while executing add_between method")

    def delete(self, value):
        node = self.head
        if node.value == value:
            self.head = node.next
            return
        else:
            while node.next:
                if node.next.value == value:
                    node.next = node.next.next
                    return
                node = node.next
        raise Exception(f"No Match Value Found while executing delete method")


if __name__ == '__main__':

    llist = LinkedList('abcd')
    print(llist)
    for elem in llist:
        print(elem)
    llist.add_first('_')
    print(llist)
    llist.add_last('e')
    print(llist)
    llist.add_between('bb', 'b', 'c')
    print(llist)
    llist.delete('bb')
    print(llist)
    llist.delete('_')
    print(llist)
    llist.delete('e')
    print(llist)
    try:
        llist.add_between('bb', 'b', 'e')
    except Exception as err:
        print(f'Error: {err}')
    try:
        llist.delete('bb')
    except Exception as err:
        print(f'Error: {err}')
