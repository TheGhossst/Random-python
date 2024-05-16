class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode(value={self.value})"

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next  
            current.next = prev  
            prev = current       
            current = next      
        self.head = prev
        print("The reversed linked list is : ", end = "") 
        self.print_list()

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Original Linked List:")
linked_list.print_list()

elements = linked_list.to_list()
print("Linked List to Python List:", elements)

linked_list.reverse()



