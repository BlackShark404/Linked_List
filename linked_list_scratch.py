from node import Node

class Linked_List:
    def __init__(self):
        self._head = None

    def insert_beginning(self, data):
        assert data is not None, "Cannot insert None value"

        node = Node(data)

        node.next = self._head
        self._head = node

    def insert_end(self, data):
        assert data is not None, "Cannot insert None value"

        node = Node(data)

        if not self._head:
            self._head = node
        else:
            current = self._head

            while current.next:
                current = current.next

            current.next = node

    def insert_before_given_node(self, key, data):
        assert key is not None and data is not None, "Cannot use None as key or data"
        assert self._head, "Cannot insert before key in empty list"    

        node = Node(data)

        if self._head.data == key:
            node.next = self._head
            self._head = node
            return
        
        current = self._head
        pre_current = None

        while current and current.data != key:
            pre_current = current
            current = current.next
        
        assert current, f"Key {key} not found in list"

        pre_current.next = node
        node.next = current

    def insert_after_given_node(self, key, data):
        assert key is not None and data is not None, "Cannot use None as key or data"
        assert self._head, "Cannot insert after a given node in empty list"

        node = Node(data)

        current = self._head

        while current and current.data != key:
            current = current.next

        assert current, f"Key {key} not found in list"

        node.next = current.next
        current.next = node

    def delete_beginning(self):
        assert self._head, "Cannot delete from empty list"

        self._head = self._head.next


    def delete_end(self):
        assert self._head, "Cannot delete from empty list"

        if not self._head.next:
            self._head = None
        else:
            current = self._head

            while current.next.next:
                current = current.next

            current.next = None

    def delete_given_node(self, key):
        assert key is not None, "Cannot use None as a key to delete given node"

        if self._head.data == key:
            self._head = self._head.next
            return

        current = self._head
        pre_current = None

        while current and current.data != key:
            pre_current = current
            current = current.next
        
        assert current, f"Key {key} not found in list"

        pre_current.next = current.next
    
    def len(self):
        count = 0
        current = self._head

        while current:
            count += 1
            current = current.next

        return count

    def sum(self):
        if not self._head:
            return 0

        total_sum = 0

        current = self._head

        try:
            while current:
                total_sum += current.data
                current = current.next
        except:
            raise TypeError("Cannot calculate sum of non-numeric data")

        return total_sum

    def mean(self):
        assert self._head, "Cannot calculate mean of empty list"

        try:
            return self.sum() / self.len() 
        

    def display(self):
        current = self._head

        print("Linked List: ", end="")
        
        if not self._head:
            print("empty")
        else:
            while current:
                print(f"{current.data}", end=" ")
                current = current.next

        print()
