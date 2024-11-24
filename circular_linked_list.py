import os # wala rani apil

def clear():
    os.system("cls" if os.name == "nt" else "clear")

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

class CircularLinkedList():
    def __init__(self):
        # Initialize the head and tail of the circular linked list
        self._head = None
        self._tail = None

    def len(self):
        count = 0 # Set count to 0
        current = self._head
        
        while current:
            count += 1 # Increment count by 1
            current = current.next

            # If current is equal to self._head, break the loop
            if current == self._head:
                break
            
        return count

    def insert_beginning(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        if not self._head:
            # If the list is empty, the new node becomes the head and tail, and points to itself
            self._head = self._tail = new_node
            self._tail.next = self._head
        else:
            # Insert the new node at the beginning and adjust head and tail pointers
            new_node.next = self._head
            self._head = new_node
            self._tail.next = self._head

    def insert_end(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        if not self._head:
            # If the list is empty, the new node becomes the head and tail
            self._head = self._tail = new_node
            self._tail.next = self._head
        else:
            # Insert the new node at the end and adjust the tail pointer
            self._tail.next = new_node
            self._tail = new_node
            self._tail.next = self._head

    def insert_before_given_node(self, key, data):
        if not self._head:
            # If the list is empty, do nothing
            return

        # Special case: if the head contains the key
        if self._head.data == key:
            self.insert_beginning(data)
            return

        current = self._head

        while current.next != self._head:
            if current.next.data == key:
                # Insert the new node before the node with the given key
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return

            current = current.next

    def insert_after_given_node(self, key, data):
        if not self._head:
            # If the list is empty, do nothing
            return

        current = self._head

        while True:
            if current.data == key:
                # Insert the new node after the node with the given key
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node

                if current == self._tail:
                    # Adjust the tail pointer if the node was inserted at the end
                    self._tail = new_node
                    
                return

            current = current.next

            if current == self._head:
                # Stop if we have traversed the entire list
                break

    def insert_position(self, position, data):
        if position <= 0:
            # Invalid position
            return

        if position == 1:
            # Insert at the beginning
            self.insert_beginning(data)
            return

        current = self._head
        index = 1

        while current.next != self._head and index < position - 1:
            # Traverse to the position before where the new node will be inserted
            current = current.next
            index += 1

        # Insert the new node at the specified position
        new_node = Node(data)

        new_node.next = current.next
        current.next = new_node

        if current == self._tail:
            # Adjust the tail pointer if the node was inserted at the end
            self._tail = new_node

    def delete_beginning(self):
        if not self._head:
            # If the list is empty, do nothing
            return

        if self._head == self._tail:
            # If there is only one node, delete it
            self._head = self._tail = None
        else:
            # Remove the head node and adjust the pointers
            self._head = self._head.next
            self._tail.next = self._head

    def delete_end(self):
        if not self._head:
            # If the list is empty, do nothing
            return

        if self._head == self._tail:
            # If there is only one node, delete it
            self._head = self._tail = None
        else:
            # Traverse to the second-to-last node
            current = self._head

            while current.next != self._tail:
                current = current.next

            # Remove the tail node and adjust the pointers
            current.next = self._head
            self._tail = current

    def delete_given_data(self, key):
        if not self._head:
            # If the list is empty, do nothing
            return

        if self._head.data == key:
            # If the head contains the key, delete it
            self.delete_beginning()
            return

        current = self._head

        while current.next != self._head:
            if current.next.data == key:
                # Remove the node with the given key
                current.next = current.next.next
                if current.next == self._head:
                    # Adjust the tail pointer if the node was the tail
                    self._tail = current
                return

            current = current.next

    def delete_node(self, node):
        if not self._head:
            return

        if self._head == node:
            self.delete_beginning()
            return

        current = self._head

        while current.next != self._head:
            if current.next == node: 

                current.next = current.next.next

                if current.next == self._head:
                    self._tail = current

                return

            current = current.next

    def split(self):
        if not self._head or self._head == self._tail:
            return self, None

        slow = self._head
        fast = self._head

        while fast.next != self._head and fast.next.next != self._head:
            slow = slow.next
            fast = fast.next.next

        second_list = CircularLinkedList()
        second_list._head = slow.next
        second_list._tail = self._tail

        self._tail = slow
        self._tail.next = self._head
        second_list._tail.next = second_list._head

        return self, second_list 

    def merge(self, new_list):
        if not new_list._head:
            # If the new list is empty, do nothing
            return

        if not self._head:
            # If the current list is empty, set it to the new list
            self._head = new_list._head
            self._tail = new_list._tail
            self._tail.next = self._head
            return

        # Merge the new list at the end of the current list
        self._tail.next = new_list._head
        new_list._tail.next = self._head
        self._tail = new_list._tail

    def highlight_red(self, text):
        # Use ANSI escape codes to color the text red
        return f"\033[91m{text}\033[0m"


    def joseph_circle(self, step):
        current = self._head

        while self.len() > 1:
            count = 1

            while count != step:
                current = current.next
                count += 1

            print("Kill: " + self.highlight_red(current.data))
            next_person = current.next
            self.delete_node(current)
            current = next_person
    def display(self):
        if not self._head:
            # If the list is empty, print nothing
            print("The list is empty.")
            return

        current = self._head

        while True:
            print(f"{current.data}", end=" -> ")
            current = current.next

            if current == self._head:
                break

        print("(head)")


def main():
    clear()

    # Create an instance of the CircularLinkedList class
    cll = CircularLinkedList()

    # Insert elements at the end of the circular linked list
    print("Inserting elements at the end of the list:")
    cll.insert_end(1)  # Add 1 to the list
    cll.insert_end(2)  # Add 2 to the list
    cll.insert_end(3)  # Add 3 to the list
    print("Current list:")
    cll.display()  # Display the list: 1 -> 2 -> 3

    # Insert an element at the beginning of the list
    print("\nInserting an element at the beginning of the list:")
    cll.insert_beginning(0)  # Add 0 at the start
    print("Current list:")
    cll.display()  # Display the list: 0 -> 1 -> 2 -> 3

    # Delete the first element of the list
    print("\nDeleting the first element of the list:")
    cll.delete_beginning()  # Remove 0 from the start
    print("Current list:")
    cll.display()  # Display the list: 1 -> 2 -> 3

    # Delete the last element of the list
    print("\nDeleting the last element of the list:")
    cll.delete_end()  # Remove 3 from the end
    print("Current list:")
    cll.display()  # Display the list: 1 -> 2

    # Insert an element at a specific position in the list
    print("\nInserting an element at position 2 in the list:")
    cll.insert_position(2, 99)  # Add 99 at position 2
    print("Current list:")
    cll.display()  # Display the list: 1 -> 99 -> 2

    # Create a new circular linked list for merging
    print("\nCreating another circular linked list to merge:")
    new_cll = CircularLinkedList()
    new_cll.insert_end(10)  # Add 10 to the new list
    new_cll.insert_end(20)  # Add 20 to the new list
    print("New list:")
    new_cll.display()  # Display the new list: 10 -> 20

    # Merge the two lists
    print("\nMerging the new list into the current list:")
    cll.merge(new_cll)  # Merge new_cll into cll
    print("Merged list:")
    cll.display()  # Display the merged list: 1 -> 99 -> 2 -> 10 -> 20

    print("\nSplit list:")
    cll1 = CircularLinkedList()
    cll2 = CircularLinkedList()
    print("Split current list :", end="")
    cll.display()
    cll1, cll2 = cll.split()
    print("First half         :", end="")
    cll1.display()
    print("Second half        :", end="")
    cll2.display()
    

    print("\nJosephus Problem:")
    print("Current list:", end=" ")
    cll.display()
    cll.joseph_circle(2)
    print("Last:", end=" ")
    cll.display()

if __name__ == "__main__":
    main()

