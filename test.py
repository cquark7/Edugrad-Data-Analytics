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
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        """
        Checks if the LinkedList is empty or not
        :return: bool
        """
        if self.head == self.tail is None:
            return True
        return False

    def insert_at_end(self, data):
        """
        Adds a new node at the end of the LinkedList
        Time Complexity: O(1)
        :param data: value you want to add at the end
        :return: None
        """
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            last_node = self.tail
            last_node.next = Node(data)
            self.tail = last_node.next
        self.size += 1

    def remove_from_beg(self):
        """
        Removes node which is at the beginning of LinkedList
        Time Complexity: O(1)
        :return: self.head.data
        """
        if self.is_empty():
            raise Exception("Data Structure is empty")
        else:
            head_node = self.head
            self.head = head_node.next
            # when the only node is removed
            if self.head is None:
                self.tail = None
        self.size -= 1
        return head_node.data

    def traverse(self):
        """
        Traverses the Nodes and prints data on STDOUT
        Time Complexity: O(n)
        :return: None
        """
        if self.is_empty():
            raise Exception("Data Structure is empty")
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()


class Queue(LinkedList):
    """
    Queue (FIFO) data structure implementation using singly LinkedList
    """
    def enqueue(self, data):
        return self.insert_at_end(data)

    def dequeue(self):
        return self.remove_from_beg()


class Stack(Queue):
    """
    Stack (LIFO) data structure implementation using a Queue
    """
    def push(self, data):
        return self.enqueue(data)

    def pop(self):
        for _ in range(self.size-1):
            temp = self.dequeue()
            self.enqueue(temp)
        return self.dequeue()

