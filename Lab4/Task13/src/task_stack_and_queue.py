class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def display(self):
        if self.isEmpty():
            return "Stack is empty"
        result = []
        current = self.top
        while current:
            result.append(current.data)
            current = current.next
        return result


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue is empty")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
        return result
