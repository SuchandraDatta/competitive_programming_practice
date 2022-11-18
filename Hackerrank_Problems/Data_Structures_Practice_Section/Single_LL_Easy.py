def getNode(head, positionFromTail):
    temp = []
    ptr = head
    while(ptr!=None):
        temp.append(ptr.data)
        ptr = ptr.next
    print(temp)
    print(len(temp))
    print(positionFromTail)
    return temp[len(temp)-positionFromTail-1]


def removeDuplicates(head):
	'''
	Remove duplicates from a sorted list
	'''
    new_list = None
    ptr = head
    while(ptr!=None):
        node = SinglyLinkedList()
        node.next = None
        node.data = ptr.data
        if(new_list == None):
            new_list = node
        else:
            trav_ptr = new_list
            while(trav_ptr.next!=None):
                trav_ptr = trav_ptr.next
            if(trav_ptr.data!=ptr.data):
                trav_ptr.next = node
        ptr = ptr.next
    return new_list

def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    node.next = None
    node.prev = None
    if(head == None):
        head = node
    elif(head.data > data):
        node.next = head
        node.prev = None
        head.prev = node
        head = node
    else:
        trav_ptr = head
        while(trav_ptr!=None and trav_ptr.data <= data):
            prev = trav_ptr
            trav_ptr = trav_ptr.next
        if(trav_ptr == None):
            prev.next = node
            node.prev = prev
        else:
            prev = trav_ptr.prev
            node.next = trav_ptr
            trav_ptr.prev = node
            if(prev!=None):
                prev.next = node
            node.prev = prev
    return head
            