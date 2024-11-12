class Node:
    def __init__(self, data=None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter 
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

class Linked_List:
    def __init__(self) -> None:
        self._head = None

    def insert_beginning(self, data):
        # Assert that the data is not None
        assert data is not None, "Cannot use None as value"

        # Create a new node with the given data
        node = Node(data)

        # Set the new node's next pointer to the current head
        node.next = self._head
        # Set the head to the new node
        self._head = node

    def insert_end(self, data):
        # Assert that the data is not None
        assert data is not None, "Cannot use None as value"
        
        # Create a new node with the given data
        node = Node(data)

        # If the list is empty, set the head to the new node
        if not self._head:
            self._head = node
        else:
            # Traverse to the last node
            current = self._head
            while current.next:
                current = current.next

            # Set the next pointer of the last node to the new node
            current.next = node

    def insert_before_given_data(self, key, data):
        # Assert that the key and data are not None, and the list is not empty
        assert key is not None or data is not None, "Cannot use None as key or data"
        assert self._head, "Cannot insert before a given node from empty list"

        # Create a new node with the given data
        node = Node(data)

        # If the head's data matches the key, insert the new node at the beginning
        if self._head.data == key:
            node.next = self._head
            self._head = node
            return

        # Traverse the list to find the node just before the key
        current = self._head
        pre_current = None
        while current and current.data != key:
            pre_current = current
            current = current.next

        # Assert that the key was found
        assert current, f"Key {key} not found in list"

        # Insert the new node before the node with the key data
        pre_current.next = node
        node.next =  current

    def insert_after_given_node(self, key, data):
        # Assert that the key and data are not None, and the list is not empty
        assert key is not None and data is not None, "Cannot use None as key or data"
        assert self._head, "Cannot insert after a given node from empty list"

        # Create a new node with the given data
        node = Node(data)

        # Traverse the list to find the node with the key data
        current = self._head
        while current and current.data != key:
            current = current.next

        # Assert that the key was found
        assert current, f"Key {key} not found in list"

        # Insert the new node after the node with the key data
        node.next = current.next
        current.next = node

    def delete_beginning(self):
        # Assert that the list is not empty
        assert self._head, "Cannot delete from empty list"

        # Set the head to the next node
        self._head = self._head.next
   
    def delete_end(self):
        # Assert that the list is not empty
        assert self._head, "Cannot delete from empty list"

        # If there's only one node, set the head to None
        if self._head.next is None:
            self._head = None
        else:
            # Traverse to the second-to-last node and set its next pointer to None
            current = self._head
            while current.next.next:
                current = current.next
            current.next = None

    def delete_given_node(self, key):
        # Assert that the key is not None, and the list is not empty
        assert key is not None, "Cannot use None as key"
        assert self._head, "Cannot delete from empty list"

        # If the head's data matches the key, update the head to the next node
        if self._head.data == key:
            self._head = self._head.next
            return

        # Traverse the list to find the node just before the node with the key data
        current = self._head
        pre_current = None
        while current and current.data != key:
            pre_current = current
            current = current.next

        # Assert that the key was found
        assert current, f"Key {key} not found in list"

        # Update the next pointer of the previous node to skip the node with the key data
        pre_current.next = current.next

    def len(self):
        # Initialize the count to 0
        total_count = 0

        # Traverse the list and increment the count
        current = self._head
        while current:
            total_count += 1
            current = current.next

        # Return the total count
        return total_count

    def sum(self):
        # If the list is empty, return 0
        if not self._head:
            return 0
        
        # Initialize the total sum to 0
        total_sum = 0

        # Traverse the list and add the data values
        current = self._head
        while current:
            total_sum += current.data
            current = current.next

        # Return the total sum
        return total_sum

    def mean(self):
        # Assert that the list is not empty
        assert self._head, "Cannot calculate mean of empty list"

        # Calculate the mean by dividing the sum by the length
        return self.sum() / self.len()

    def min(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find minimum value of empty list"

        # Initialize the minimum value to the first node's data
        min_val = self._head.data

        # Traverse the list and update the minimum value
        current = self._head
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next

        # Return the minimum value
        return min_val

    def max(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find maximum value of empty list"

        # Initialize the maximum value to the first node's data
        max_val = self._head.data

        # Traverse the list and update the maximum value
        current = self._head
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next

        # Return the maximum value
        return max_val

    def has_duplicates(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find duplicates in empty list"

        # Traverse the list and check for duplicates
        current = self._head
        while current:
            next_current = current.next
            while next_current:
                if current.data == next_current.data:
                    return True
                next_current = next_current.next
            current = current.next

        # If no duplicates were found, return False
        return False

    def remove_duplicates(self):
        # If the list has 0 or 1 nodes, return
        if not self._head or not self._head.next:
            return

        # Traverse the list and remove any duplicate nodes
        current = self._head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def search(self, key):
        # Assert that the key is not None, and the list is not empty
        assert key is not None, "Cannot use None as key"
        assert self._head, "Cannot search in empty list"

        # Traverse the list and check if the key is found
        current = self._head
        while current:
            if current.data == key:
                return True
            current = current.next

        # If the key was not found, return False
        return False

    def find_first_element(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find first element of empty list"

        # Return the data of the first node
        return self._head.data

    def find_middle_element(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find middle element of empty list"

        # If there's only one node, return its data
        if self._head.next is None:
            return self._head.data

        # Use the "slow" and "fast" pointers to find the middle node
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Return the data of the middle node
        return slow.data

    def find_last_element(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find last element of empty list"

        # Traverse to the last node and return its data
        current = self._head
        while current.next:
            current = current.next
        return current.data

    def detect_cycle(self):
        # Assert that the list is not empty
        assert self._head, "Cannot detect cycle in empty list"

        # Use the "slow" and "fast" pointers to detect a cycle
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        # If no cycle was detected, return False
        return False

    def copy(self, list):
        # Assert that the input list is not None and not empty
        assert list is not None, "List cannot be None"
        assert list._head is not None, "Cannot copy from empty list"

        # Initialize the new list to be empty
        self._head = None

        # Traverse the input list and insert each node into the new list
        current = list._head
        while current is not None:
            self.insert_end(current.data)
            current = current.next

    def sort(self, reverse=False):
        # If the list has 0 or 1 nodes, it's already sorted
        if not self._head or not self._head.next:
            return

        # Perform a bubble sort
        was_swapped = True
        while was_swapped:
            was_swapped = False
            current = self._head
            while current.next:
                if (not reverse and current.data > current.next.data) or \
                   (reverse and current.data < current.next.data):
                    # Swap the data of the current and next nodes
                    current.data, current.next.data = current.next.data, current.data
                    was_swapped = True
                current = current.next

    def find_first_node(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find first node of empty list"

        # Return the head node
        return self._head

    def find_middle_node(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find middle node of empty list"

        # Use the "slow" and "fast" pointers to find the middle node
        slow = fast = self._head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Return the middle node
        return slow

    def find_last_node(self):
        # Assert that the list is not empty
        assert self._head, "Cannot find last node of empty list"

        # Traverse to the last node and return it
        current = self._head
        while current.next:
            current = current.next
        return current

    def merge(self, list):
        # Assert that the input list is not None
        assert list is not None, "Cannot merge with None list"

        # If the current list is empty, set its head to the head of the input list
        if not self._head and list._head:
            self._head = list._head
        # If the input list is empty, do nothing
        elif not list._head:
            return
        else:
            # Find the last node in the current list and append the head of the input list
            last_node = self.find_last_node()
            last_node.next = list._head

    def is_empty(self):
        # Return True if the list is empty, False otherwise
        return self._head is None

    def clear(self):
        # Set the head to None to clear the list
        self._head = None

    def display(self):
        # Initialize the current node to the head
        current = self._head

        # Print the list
        print("Linked List:", end=" ")
        while current:
            print(f"{current.data}", end=" ")
            current = current.next
        print()

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

    
def main():
    # Create a new linked list
    print("\n=== Creating and Basic Operations ===")
    ll = Linked_List()
    ll2 = Linked_List()
    print("Is empty?", ll.is_empty())  # Should be True
    
    # Test insertions
    print("\n=== Testing Insertions ===")
    ll.insert_beginning(1)
    ll.insert_end(3)
    ll.insert_beginning(0)
    ll.insert_end(4)
    ll.insert_after_given_node(1, 2)
    print("List after insertions:", end=" ")
    ll.display()  # Should show: head->0->1->2->3->4->x
    
    # Test length and basic stats
    print("\n=== Testing Basic Statistics ===")
    print("Length:", ll.len())  # Should be 5
    print("Sum:", ll.sum())  # Should be 10
    print("Mean:", ll.mean())  # Should be 2.0
    print("Min:", ll.min())  # Should be 0
    print("Max:", ll.max())  # Should be 4
    
    # Test element finding
    print("\n=== Testing Element Finding ===")
    print("First element:", ll.find_first_element())  # Should be 0
    print("Middle element:", ll.find_middle_element())  # Should be 2
    print("Last element:", ll.find_last_element())  # Should be 4
    
    # Test search
    print("\n=== Testing Search ===")
    print("Search for 2:", ll.search(2))  # Should be True
    print("Search for 7:", ll.search(7))  # Should be False
    
    # Test duplicates
    print("\n=== Testing Duplicates ===")
    ll.insert_end(2)
    print("List with duplicate:", end=" ")
    ll.display()
    print("Has duplicates?", ll.has_duplicates())  # Should be True
    ll.remove_duplicates()
    print("List after removing duplicates:", end=" ")
    ll.display()
    
    # Test sorting
    print("\n=== Testing Sorting ===")
    ll.insert_end(1)  # Add some out-of-order elements
    ll.insert_beginning(5)
    print("Unsorted list:", end=" ")
    ll.display()
    ll.sort()
    print("Sorted ascending:", end=" ")
    ll.display()
    ll.sort(reverse=True)
    print("Sorted descending:", end=" ")
    ll.display()
    
    # Test display reverse
    print("\n=== Testing Reverse Display ===")
    print("Normal display:", end=" ")
    ll.display()
    print("Reverse display:", end=" ")
    ll.display_reverse()
    
    # Test copying an
    print("\n=== Testing Copy and Merge ===")
    ll2.copy(ll)
    print("Copied list:", end=" ")
    ll2.display()
    
    ll3 = Linked_List()
    ll3.insert_end(10)
    ll3.insert_end(20)
    print("Second list:", end=" ")
    ll3.display()
    ll2.merge(ll3)
    print("Merged list:", end=" ")
    ll2.display()
    
    # Test cycle detection
    print("\n=== Testing Cycle Detection ===")
    print("Has cycle?", ll.detect_cycle())  # Should be False
    
    # Test deletions
    print("\n=== Testing Deletions ===")
    ll.delete_beginning()
    print("After delete beginning:", end=" ")
    ll.display()
    ll.delete_end()
    print("After delete end:", end=" ")
    ll.display()
    ll.delete_given_node(2)
    print("After delete node 2:", end=" ")
    ll.display()
    
    # Test clearing
    print("\n=== Testing Clear ===")
    ll.clear()
    print("Is empty after clear?", ll.is_empty())  # Should be True

if __name__ == "__main__":
    main()
