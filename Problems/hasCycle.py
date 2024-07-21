'''
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. 
Given a pointer to the head of a linked list, determine if it contains a cycle. 
If it does, return 1. Otherwise, return 0.
'''

#!/bin/python3

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def has_cycle(head):
    visited = set()
    
    temp = head
    while (temp is not None):
        if temp in visited:
            return 1
        else:
            visited.add(temp)
        temp = temp.next

    return 0
if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1)
        temp = llist.head

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

    if result == 0:
        print("\nCycle")
    else:
        print("\nNo cycle")