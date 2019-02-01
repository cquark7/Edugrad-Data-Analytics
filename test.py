class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list with both head and tail
    """
    def __init__(self):
        self.head = self.tail = None

    def is_empty(self):
        if self.head == self.tail is None:
            return True
        return False

    def insert_at_end(self, data):
        """
        Adds a new node at the end of the Linked List
        Insertion complexity is O(1) of this implementation
        :param data: value you want to add at the end
        :return: None
        """
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            last_node = self.tail
            last_node.next = Node(data)
            self.tail = last_node.next

    def remove_from_beg(self):
        if self.is_empty():
            raise Exception("{} is empty".format(__class__.__name__))
        else:
            head_node = self.head
            self.head = head_node.next
            del head_node
            # when the only node is removed
            if self.head is None:
                self.tail = None

    def traverse(self):
        """
        Traverses the Nodes and prints Node data on STDOUT
        :return: None
        """
        if self.is_empty():
            raise Exception("{} is empty".format(__class__.__name__))
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()


class Queue(LinkedList):
    """
    FIFO Queue implementation using LinkedList data structure
    """
    def enqueue(self, data):
        return self.insert_at_end(data)

    def dequeue(self):
        if self.is_empty():
            raise Exception("{} is empty".format(__class__.__name__))
        return self.remove_from_beg()

    def traverse(self):
        if self.is_empty():
            raise Exception("{} is empty".format(__class__.__name__))
        super().traverse()


Q = Queue()
print(dir(Q))
