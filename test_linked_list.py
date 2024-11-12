from linked_list import Linked_List

new_sll = Linked_List()

new_sll.insert_end(20)
new_sll.insert_end(10)
new_sll.insert_end(40)
new_sll.insert_end(30)
new_sll.insert_end(50)
new_sll.insert_end(10)
new_sll.insert_end(30)

new_sll.sort()
print(f"Contains duplicates: ", new_sll.has_duplicates())
print(f"Mode: {new_sll.mode()}")
new_sll.remove_duplicates()
print(f"Contains duplicates: ", new_sll.has_duplicates())
new_sll.display()
