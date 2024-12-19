class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, value):
        
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        # 2. Insert at the end (O(n))
    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node
            
    # 5. Traverse and display the list (O(n))
    def traverse(self):
        current = self.head
        elements = []
        while current:
            print(current.data)
            elements.append(current.data)
            current = current.next
        return elements
    
    
# Example Usage
linked_list = LinkedList()

# Insert at head
linked_list.insert_at_head(10)
linked_list.insert_at_head(20)
# Traverse
print("Linked List:", linked_list.traverse())  # Output: [20, 10, 30, 40]