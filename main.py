from linked_list import Linked_List

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
    ll.insert_after(1, 2)
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
    
    # Test copying and merging
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
    ll.delete_node(2)
    print("After delete node 2:", end=" ")
    ll.display()
    
    # Test clearing
    print("\n=== Testing Clear ===")
    ll.clear()
    print("Is empty after clear?", ll.is_empty())  # Should be True

if __name__ == "__main__":
    main()
