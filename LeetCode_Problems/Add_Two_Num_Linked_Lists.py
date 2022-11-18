# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def append_to_list(self, head, tail, node):
        if(head == None):
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
        return head, tail
     
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = None
        tail = None
        while(l1!=None and l2!=None):
            #answer.append((l1.val + l2.val + carry)%10)
            head, tail= self.append_to_list(head, tail, ListNode((l1.val + l2.val + carry)%10, None))
            carry = int((l1.val + l2.val + carry) / 10)
            l1 = l1.next
            l2 = l2.next
            
        while(l1!=None):
            #answer.append((l1.val + carry)%10)
            head, tail= self.append_to_list(head, tail, ListNode((l1.val + carry)%10, None))
            carry = int((l1.val + carry) / 10)
            l1 = l1.next
            
        while(l2!=None):
            #answer.append((l2.val + carry)%10)
            head, tail = self.append_to_list(head, tail, ListNode((l2.val + carry)%10, None) )
            carry = int((l2.val + carry) / 10)
            l2 = l2.next
            
            
        if(carry!=0):
            node = ListNode(val = carry, next = None)
            head, tail = self.append_to_list(head, tail, node)
            
        return head
        