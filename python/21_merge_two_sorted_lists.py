# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy head node
        dummy = ListNode(0)
        current = dummy
        
        # Compare and merge nodes from both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes from list1 or list2
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    current = head
    values = []
    while current:
        values.append(current.val)
        current = current.next
    print(values)
    return values

# Test the solution
if __name__ == "__main__":
    # Create test linked lists
    l1 = createLinkedList([1, 2, 4])
    l2 = createLinkedList([1, 3, 4])
    
    print("List 1:")
    printLinkedList(l1)
    print("List 2:")
    printLinkedList(l2)
    
    # Merge the lists
    solution = Solution()
    merged = solution.mergeTwoLists(l1, l2)
    
    print("Merged list:")
    result = printLinkedList(merged)
    print(f"Final result: {result}")