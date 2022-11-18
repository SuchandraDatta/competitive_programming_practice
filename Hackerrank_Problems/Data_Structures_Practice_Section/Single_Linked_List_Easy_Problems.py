# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
	'''
	My own recursive implementation haha this just reverse prints it not actually reverses anything
	'''
    if(head.next == None):
        print(head.data)
    else:
        reversePrint(head.next)
        print(head.data)

def insertNodeAtTail(head, data):
    if(head == None):
        head = SinglyLinkedList()
        head.data = data
        head.next = None
        #print(head.data)
    else:
        ptr = head
        while(ptr.next != None):
            ptr = ptr.next
        node = SinglyLinkedList()
        node.data = data
        node.next = None
        ptr.next = node
    return head

def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedList()
    node.data = data
    node.next = None
    if(llist == None):
        llist = node
    else:
        node.next = llist
        llist = node        
    return llist

def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedList()
    node.data = data
    node.next = None
    if(position == 0):
        node.next = head
        head = node
    else:
        ptr = head
        for i in range(0,position):
            prev = ptr
            ptr = ptr.next
        prev.next = node
        node.next = ptr
    return head

def deleteNode(head, position):
    if(position == 0):
        head = head.next
    else:
        ptr = head
        for i in range(0, position):
            prev = ptr
            ptr = ptr.next
        prev.next = ptr.next
        ptr.next = None
    return head


def actually_reverse(head):
    ptr = head
    prev = head
    copy = head.next
    pos = 0
    while(copy!=None):
        pos = pos + 1
        ptr = copy
        copy = ptr.next
        ptr.next = prev
        if(pos == 1):
            prev.next = None
        prev = ptr
    head = prev
    return head   

def compare_lists(llist1, llist2):
	'''
	Returns 1 if the lists are equal, else 0
	'''
    ptr1 = llist1
    ptr2 = llist2
    answer = 0
    while(ptr1!=None and ptr2!=None):
        if(ptr1.data != ptr2.data):
            answer = -1
            break
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    if(answer == -1):
        return 0
    elif(ptr1==None and ptr2!=None):
        return 0
    elif(ptr1!=None and ptr2 == None):
        return 0
    else:
        return 1


def mergeLists(head1, head2):
    ptr1 = head1
    ptr2 = head2
    new_list = None
    while(ptr1!=None and ptr2!=None):
        node = SinglyLinkedList()
        node.next = None
        print("Ptr1", ptr1.data)
        if(ptr1.data <= ptr2.data):
            node.data = ptr1.data
            ptr1 = ptr1.next
        else:
            node.data = ptr2.data
            ptr2 = ptr2.next
        if(new_list == None):
            new_list = node
        else:
            trav_ptr = new_list
            while(trav_ptr.next!=None):
                trav_ptr = trav_ptr.next
            trav_ptr.next = node
        trav_ptr = new_list
        while(trav_ptr!=None):
                print(trav_ptr.data)
                trav_ptr = trav_ptr.next
        print("\n")
        
    while(ptr1!=None):
        leftover = SinglyLinkedList()
        leftover.data = ptr1.data
        leftover.next = None
        node.next = leftover
        ptr1 = ptr1.next
        node = leftover
    while(ptr2!=None):
        leftover = SinglyLinkedList()
        leftover.data = ptr2.data
        print("Adding: ", leftover.data, " after ", node.data)
        leftover.next = None
        node.next = leftover
        ptr2 = ptr2.next
        node = leftover
    trav_ptr = new_list
    while(trav_ptr!=None):
                print(trav_ptr.data)
                trav_ptr = trav_ptr.next
    return new_list
    