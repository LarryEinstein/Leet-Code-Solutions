# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Remove the nth node from the end of the list and return the head.
        
        Args:
            head: The head of the linked list
            n: The position from the end to remove (1-indexed)
            
        Returns:
            The head of the modified linked list
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Two pointers: fast and slow
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next

# Helper function to create a linked list from a list
def createLinkedList(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Helper function to convert linked list to list for printing
def linkedListToList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,3,4,5], n=2 -> [1,2,3,5]
    head1 = createLinkedList([1, 2, 3, 4, 5])
    result1 = solution.removeNthFromEnd(head1, 2)
    print(f"Test 1: {linkedListToList(result1)}")  # Expected: [1, 2, 3, 5]
    
    # Test case 2: [1], n=1 -> []
    head2 = createLinkedList([1])
    result2 = solution.removeNthFromEnd(head2, 1)
    print(f"Test 2: {linkedListToList(result2)}")  # Expected: []
    
    # Test case 3: [1,2], n=1 -> [1]
    head3 = createLinkedList([1, 2])
    result3 = solution.removeNthFromEnd(head3, 1)
    print(f"Test 3: {linkedListToList(result3)}")  # Expected: [1]
    
    # Test case 4: [1,2,3,4,5], n=5 -> [2,3,4,5]
    head4 = createLinkedList([1, 2, 3, 4, 5])
    result4 = solution.removeNthFromEnd(head4, 5)
    print(f"Test 4: {linkedListToList(result4)}")  # Expected: [2, 3, 4, 5]
