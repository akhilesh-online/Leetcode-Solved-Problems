# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        traverse = modify
        
        while traverse:
            sum = 0
            
            # Calculate sum of non-zero value nodes
            while traverse.val != 0:
                sum += traverse.val
                traverse = traverse.next
            
            # Assign sum to the modify node value
            modify.val = sum
            # Move traverse to next non-zero value
            traverse = traverse.next
            
            # Connect modify to above node
            modify.next = traverse
            modify = modify.next
        
        return head.next