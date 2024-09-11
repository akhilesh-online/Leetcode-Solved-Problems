# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify_ptr = head.next
        traverse_ptr = modify_ptr
        
        while traverse_ptr:
            sum = 0
            
            # Calculate sum of non-zero value nodes
            while traverse_ptr.val != 0:
                sum += traverse_ptr.val
                traverse_ptr = traverse_ptr.next
            
            # Assign sum to the modify_ptr node value
            modify_ptr.val = sum
            # Move traverse_ptr to next non-zero value
            traverse_ptr = traverse_ptr.next
            
            # Connect modify_ptr to above node
            modify_ptr.next = traverse_ptr
            modify_ptr = modify_ptr.next
        
        return head.next