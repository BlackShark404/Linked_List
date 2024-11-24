from node import Node

class Doubly_Linked_List:
    def __init__(self):
        # Initialize empty list with head pointing to None
        self._head = None

    def len(self):
        # Return the length of the list
        if not self._head:
            return 0
        else:
            count = 0
            current = self._head

            while current:
                count += 1
                current = current.next

            return count

    def insert_beginning(self, data):
        # Create new node and insert at the beginning of the list
        new_node = Node(data)

        if self._head:
            # If list not empty, update previous pointer of current head
            self._head.prev = new_node

        # Update new node's next pointer and set it as head
        new_node.next = self._head
        self._head = new_node

    def insert_end(self, data):
        # Create new node and insert at the end of the list
        new_node = Node(data)

        if not self._head:
            # If list is empty, set new node as head
            self._head = new_node
        else:
            # Traverse to the end of the list
            current = self._head

            while current.next:
                current = current.next

            # Update pointers to insert new node
            current.next = new_node
            new_node.prev = current

    def insert_before_given_node(self, key, data):
        # Find the node with the given key
        current = self._head

        while current and current.data != key:
            current = current.next

        if not current:
            raise ValueError("Node with the given key not found")

        # Create new node and update pointers
        new_node = Node(data)

        new_node.next = current
        new_node.prev = current.prev

        if current.prev:
            # Update previous node's next pointer if it exists
            current.prev.next = new_node
        else:
            # If inserting before head, update head
            self._head = new_node
        current.prev = new_node

    def insert_after_given_node(self, key, data):
        # Find the node with the given key
        current = self._head

        while current and current.data != key:
            current = current.next

        if not current:
            raise ValueError("Node with the given key not found")

        # Create new node and update pointers
        new_node = Node(data)

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            # Update next node's previous pointer if it exists
            current.next.prev = new_node
        current.next = new_node

    def insert_position(self, index, data):
        # Check for valid index
        if index < 0:
            raise IndexError("Index out of bounds")

        new_node = Node(data)

        if index == 0:
            # If inserting at beginning, use existing method
            self.insert_beginning(data)
            return

        # Traverse to the position
        current = self._head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of bounds")

        # Update pointers to insert new node
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def delete_beginning(self):
        # Check if list is empty
        if not self._head:
            raise ValueError("List is empty")

        if self._head.next:
            # Update previous pointer of second node if it exists
            self._head.next.prev = None

        # Move head to second node
        self._head = self._head.next

    def delete_end(self):
        # Check if list is empty
        if not self._head:
            raise ValueError("List is empty")

        if not self._head.next:
            # If only one node exists, set head to None
            self._head = None
            return

        # Traverse to the last node
        current = self._head

        while current.next:
            current = current.next

        # Update next pointer of second-to-last node
        current.prev.next = None

    def delete_given_node(self, key):
        # Find the node with the given key
        current = self._head

        while current and current.data != key:
            current = current.next

        if not current:
            raise ValueError("Node with the given key not found")

        if current.prev:
            # Update next pointer of previous node if it exists
            current.prev.next = current.next
        else:
            # If deleting head, update head pointer
            self._head = current.next

        if current.next:
            # Update previous pointer of next node if it exists
            current.next.prev = current.prev

    def split(self):
        # Return if list is empty or has only one node
        if not self._head or not self._head.next:
            return self, None

        # Find the middle node using slow and fast pointers
        slow = self._head
        fast = self._head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Create new list for second half
        second_half = Doubly_Linked_List()
        second_half._head = slow.next

        if slow.next:
            # Update previous pointer of second half
            slow.next.prev = None
        
        # Separate first half
        slow.next = None

        # Create new list for first half to maintain original list integrity
        first_half = Doubly_Linked_List()
        first_half._head = self._head

        # Clear the original list
        self._head = None

        return first_half, second_half

    def merge(self, new_list):
        # Merge the current list with the provided list
        if not new_list._head:
            return

        if not self._head:
            self._head = new_list._head
            return

        # Traverse to the end of current list
        current = self._head
        while current.next:
            current = current.next

        # Connect the two lists
        current.next = new_list._head
        new_list._head.prev = current

    def display(self):
        print("List:", end=" ")

        if not self._head:
            print("empty")
            return

        current = self._head

        while current:
            print(f"{current.data}", end=" -> ")
            current = current.next

        print("None")
    
    def display_reverse(self):
        # Display the list in reverse order using prev pointers
        print("Reverse List:", end=" ")

        if not self._head:
            print("empty")
            return

        # Traverse to the end of the list
        current = self._head
        while current.next:
            current = current.next

        # Print nodes from last to first
        while current:
            print(f"{current.data}", end=" -> ")
            current = current.prev

        print("None")

def main():
    # Create a new doubly linked list
    print("\n=== Testing Doubly Linked List Implementation ===")
    dll = Doubly_Linked_List()
    
    # Test empty list
    print("\n1. Testing empty list:")
    dll.display()
    print(f"Length of empty list: {dll.len()}")
    
    # Test insertions
    print("\n2. Testing insertions:")
    print("\nInserting at beginning: 10, 20, 30")
    dll.insert_beginning(30)
    dll.insert_beginning(20)
    dll.insert_beginning(10)
    dll.display()
    
    print("\nInserting at end: 40, 50")
    dll.insert_end(40)
    dll.insert_end(50)
    dll.display()
    
    print("\nInserting 25 before node with value 30")
    dll.insert_before_given_node(30, 25)
    dll.display()
    
    print("\nInserting 35 after node with value 30")
    dll.insert_after_given_node(30, 35)
    dll.display()
    
    print("\nInserting 45 at position 6")
    dll.insert_position(6, 45)
    dll.display()
    
    print("\nDisplaying list in reverse")
    dll.display_reverse()
    
    print(f"\nLength of list: {dll.len()}")
    
    # Test deletions
    print("\n3. Testing deletions:")
    print("\nDeleting from beginning")
    dll.delete_beginning()
    dll.display()
    
    print("\nDeleting from end")
    dll.delete_end()
    dll.display()
    
    print("\nDeleting node with value 30")
    dll.delete_given_node(30)
    dll.display()
    
    # Test split
    print("\n4. Testing split operation:")
    first_half, second_half = dll.split()
    print("\nFirst half:")
    first_half.display()
    print("Second half:")
    second_half.display()
    
    # Test merge
    print("\n5. Testing merge operation:")
    print("\nMerging the split lists back:")
    first_half.merge(second_half)
    print("Merged list:")
    first_half.display()
    
    # Test error handling
    print("\n6. Testing error handling:")
    try:
        print("\nTrying to delete from empty list:")
        empty_list = Doubly_Linked_List()
        empty_list.delete_beginning()
    except ValueError as e:
        print(f"Caught error: {e}")
    
    try:
        print("\nTrying to insert before non-existent node:")
        dll.insert_before_given_node(100, 500)
    except ValueError as e:
        print(f"Caught error: {e}")
    
    try:
        print("\nTrying to insert at invalid position:")
        dll.insert_position(-1, 100)
    except IndexError as e:
        print(f"Caught error: {e}")

if __name__ == "__main__":
    main()
