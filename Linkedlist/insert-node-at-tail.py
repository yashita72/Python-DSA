def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)

    if head is None:
        return new_node

    temp = head

    while temp.next:
        temp = temp.next

    temp.next = new_node

    return head