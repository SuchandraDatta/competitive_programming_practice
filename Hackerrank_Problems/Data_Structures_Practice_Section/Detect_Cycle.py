'''
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.

Example
1 -> 2 -> 3 -> NULL refers to the list of nodes 

The numbers shown are the node numbers, not their data values. There is no cycle in this list so return .

1 -> 2 -> 3 -> 1 -> NULL
There is a cycle where node 3 points back to node 1, so return .
'''

def has_cycle(head):
    ptr = head
    temp = []
    answer = 0
    while(ptr!=None):
        temp.append(ptr)
        ptr = ptr.next
        if(ptr in temp):
            answer = 1
            break
    return answer