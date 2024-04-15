"""
File: new_head.py
Name: Anna
------------------------
TODO: Find the nodes that smaller than variable x and move nodes to the head
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def new_head(head: ListNode, x: int) -> ListNode:
    #######################
    # Find the nodes that smaller than variable x and move nodes to the head
    #######################
    large_head, large_cur ,small_head, small_cur= None, None, None, None
    cur = head
    while cur is not None:
        if cur.val < x:
            small_node = ListNode(cur.val, None)
            if not small_head:
                # First data
                small_head = small_node
                small_cur = small_head
            else:
                # append
                small_cur.next = small_node
                small_cur = small_cur.next
        else:
            large_node = ListNode(cur.val, None)
            if not large_head:
                # First data
                large_head = large_node
                large_cur = large_head
            else:
                # append
                large_cur.next = large_node
                large_cur = large_cur.next
        cur = cur.next
    small_cur.next = large_head
    return small_head


####### DO NOT EDIT CODE BELOW THIS LINE ########

def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 new_head.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(9, None)
            l1.next = ListNode(6, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(8, None)
            ans = new_head(l1,8)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(1, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(2, None)
            l1.next.next.next.next = ListNode(5, None)
            l1.next.next.next.next.next = ListNode(1, None)
            ans = new_head(l1, 3)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 new_head.py test1"')


if __name__ == '__main__':
    main()
