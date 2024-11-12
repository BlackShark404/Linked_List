from node import Node

class Linked_List:
    def __init__(self):
        # Initialize empty linked list with head as None and size as 0
        self._head = None
        self._size = 0

    @property
    def head(self):
        # Getter for head node
        return self._head

    @head.setter
    def head(self, head):
        # Setter for head node
        self._head = head

    def insert_beginning(self, data):
        # Check for invalid input
        if data is None:
            raise ValueError("Cannot insert None value")

        # Create new node and set it as head
        node = Node(data)
        node.next = self._head
        self._head = node
        self._size += 1

    def insert_end(self, data):
        # Check for invalid input
        if data is None:
            raise ValueError("Cannot insert None value")

        # Create new node
        node = Node(data)
        
        # If list is empty, set new node as head
        if not self._head:
            self._head = node
        else:
            # Traverse to end and add new node
            current = self._head
            while current.next:
                current = current.next
            current.next = node

        # Increment size
        self._size += 1

    def insert_before(self, key, data):
        # Check for invalid inputs
        if data is None or key is None:
            raise ValueError("Cannot use None as data or key")
        if not self._head:
            raise ValueError("Cannot insert before key in empty list")

        # Create new node
        node = Node(data)

        # Handle insertion before head if key matches
        if self._head.data == key:
            node.next = self._head
            self._head = node
            self._size += 1
            return
        
        # Find node before the key node
        current = self._head
        pre_current = None

        while current and current.data != key:
            pre_current = current
            current = current.next

        # Check if key was found
        if not current:
            raise ValueError(f"Key {key} not found in list")

        # Insert new node before key node
        pre_current.next = node
        node.next = current

        self._size += 1

    def insert_after(self, key, data):
        # Check for invalid inputs
        if data is None or key is None:
            raise ValueError("Cannot use None as data or key")
        if not self._head:
            raise ValueError("Cannot insert after key in empty list")

        # Create new node
        node = Node(data)

        # Find the key node
        current = self._head
        while current and current.data != key:
            current = current.next

        # Check if key was found
        if not current:
            raise ValueError(f"Key {key} not found in list")

        # Insert new node after key node
        node.next = current.next
        current.next = node
        self._size += 1

    def delete_beginning(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot delete from empty list")
        
        # Move head to next node
        self._head = self._head.next
        self._size -= 1

    def delete_end(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot delete from empty list")

        # If only one node, remove it
        if not self._head.next:
            self._head = None
        else:
            # Traverse to second-to-last node
            current = self._head
            while current.next.next:
                current = current.next
            # Remove last node
            current.next = None

        # Decrement size
        self._size -= 1

    def delete_node(self, data):
        # Check for invalid inputs
        if data is None:
            raise ValueError("Cannot delete None value")
        if not self._head:
            raise ValueError("Cannot delete from empty list")

        # Handle deletion of head node
        if self._head.data == data:
            self._head = self._head.next
            self._size -= 1
            return

        # Find node to delete
        current = self._head
        pre_current = None
        while current and current.data != data:
            pre_current = current
            current = current.next

        # Check if node was found
        if not current:
            raise ValueError(f"Data {data} not found in list")

        # Remove node
        pre_current.next = current.next
        self._size -= 1

    def display(self):
        # Display list in format: head->data1->data2->...->x
        current = self._head
        print("head->", end="")
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print("x")
    
    def len(self):
        # Return number of nodes in list
        return self._size

    def sum(self):
        # Handle empty list
        if not self._head:
            return 0

        # Calculate sum of all nodes
        try:
            total = 0
            current = self._head
            while current:
                total += current.data
                current = current.next
            return total
        except TypeError:
            raise TypeError("Cannot calculate sum of non-numeric data")

    def mean(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot calculate mean of empty list")

        # Calculate average of all nodes
        try:
            return self.sum() / self._size
        except TypeError:
            raise TypeError("Cannot calculate mean of non-numeric data")

    def min(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find minimum of empty list")
        
        # Find minimum value
        try:
            min_val = self._head.data
            current = self._head.next
            while current:
                if current.data < min_val:
                    min_val = current.data
                current = current.next
            return min_val
        except TypeError:
            raise TypeError("Cannot compare elements of different types")

    def max(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find maximum of empty list")

        # Find maximum value
        try:
            max_val = self._head.data
            current = self._head.next
            while current:
                if current.data > max_val:
                    max_val = current.data
                current = current.next
            return max_val
        except TypeError:
            raise TypeError("Cannot compare elements of different types")
   
    def has_duplicates(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot check duplicates in empty list")

        # Compare each node with subsequent nodes
        current = self._head
        while current:
            next_current = current.next
            while next_current:
                if current.data == next_current.data:
                    return True
                next_current = next_current.next
            current = current.next
        return False

    def remove_duplicates(self):
        if not self._head or not self._head.next:
            return  # Empty list or single node list, no duplicates to remove

        current = self._head
        while current.next:
            if current.data == current.next.data:
                # Skip over nodes with duplicate data
                current.next = current.next.next
            else:
                current = current.next

    def search(self, key):
        # Check for invalid inputs
        if not self._head:
            raise ValueError("Cannot search in empty list")
        if key is None:
            raise ValueError("Cannot search for None value")

        # Search for key in list
        current = self._head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def find_first_element(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find first element of empty list")
        return self._head.data

    def find_middle_element(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find middle element of empty list")

        # Handle single node case
        if not self._head.next:
            return self._head.data

        # Use fast/slow pointer technique to find middle
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def find_last_element(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find last element of empty list")

        # Traverse to last node
        current = self._head
        while current.next:
            current = current.next
        return current.data
            
    def detect_cycle(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot detect cycle in empty list")

        # Use Floyd's cycle-finding algorithm
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def copy(self, new_list):
        # Check if source list is None
        if new_list is None:
            raise ValueError("Source list cannot be None")
            
        # Check if source list is empty
        if new_list.head is None:
            raise ValueError("Cannot copy empty list")
            
        # Clear the destination list
        self.head = None
        
        # Start copying from the head
        current = new_list.head
        
        # Copy all nodes including the last one
        while current is not None:
            self.insert_end(current.data)
            current = current.next
    
    def display_reverse(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot display reverse of empty list")

        # Create a copy of the list
        copied_list = Linked_List()
        copied_list.copy(self)

        # Reverse the copied list
        prev = None
        current = copied_list._head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Display the reversed list
        current = prev
        print("head->", end="")
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print("x")

    def sort(self, reverse=False):
        # Handle empty or single node list
        if not self._head or not self._head.next:
            return

        # Implement bubble sort
        try:
            was_swapped = True
            while was_swapped:
                was_swapped = False
                current = self._head
                while current.next:
                    # Compare adjacent nodes based on sort direction
                    if (not reverse and current.data > current.next.data) or \
                       (reverse and current.data < current.next.data):
                        # Swap node data
                        current.data, current.next.data = current.next.data, current.data
                        was_swapped = True
                    current = current.next
        except TypeError:
            raise TypeError("Cannot sort list with incomparable data types")

    def find_first_node(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find first node of empty list")
        return self._head
    
    def find_middle_node(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find middle node of empty list")

        # Handle single node case
        if not self._head.next:
            return self._head

        # Use fast/slow pointer technique to find middle
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def find_last_node(self):
        # Check for empty list
        if not self._head:
            raise ValueError("Cannot find last node of empty list")

        # Traverse to last node
        current = self._head
        while current.next:
            current = current.next
        return current

    def merge(self, new_list):
        # Check for invalid input
        if new_list is None:
            raise ValueError("Cannot merge with None list")

        # Handle empty lists cases
        if not self._head and not new_list._head:
            return
        if not self._head:
            self._head = new_list._head
            self._size = new_list._size
            return
        if not new_list._head:
            return

        # Find last node of current list
        last_node = self.find_last_node()
        
        # Merge lists by connecting last node to head of second list
        last_node.next = new_list._head
        self._size += new_list._size

    def is_empty(self):
        # Check if list has no nodes
        return self._head is None

    def clear(self):
        # Remove all nodes from list
        self._head = None
        self._size = 0
