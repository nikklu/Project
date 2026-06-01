# 1. Define the Linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Your MergeList Function
def MergeList(list1, list2):
    dummy = ListNode(0)  # Use a dummy node to simplify head handling
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    # Attach remaining elements from either list
    tail.next = list1 if list1 else list2
    return dummy.next

# Helper: Convert standard list to Linked List
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper: Convert Linked List back to standard list for printing
def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

# Sample Usage
a = create_linked_list([1, 2, 3])
b = create_linked_list([1, 3, 4])
merged_head = MergeList(a, b)

print(to_list(merged_head)) # Output: [1, 1, 2, 3, 3, 4]
