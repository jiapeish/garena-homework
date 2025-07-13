class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeReverse:
    def merge(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1 is not None:
            tail.next = head1

        if head2 is not None:
            tail.next = head2

        return dummy.next

    def reverse(self, head):
        tail = None
        p = head
        while p is not None:
            tmp = p.next
            p.next = tail
            tail = p
            p = tmp
        return tail


def main():
    head1 = ListNode(1)
    cur = head1
    for val in [3, 5, 7, 9]:
        cur.next = ListNode(val)
        cur = cur.next

    values = []
    cur = head1
    while cur is not None:
        values.append(str(cur.val))
        cur = cur.next
    print("list1:", "->".join(values))

    head2 = ListNode(2)
    cur = head2
    for val in [4, 6, 8, 10]:
        cur.next = ListNode(val)
        cur = cur.next

    values = []
    cur = head2
    while cur is not None:
        values.append(str(cur.val))
        cur = cur.next
    print("list2:", "->".join(values))

    mr = MergeReverse()
    head = mr.merge(head1, head2)
    result = mr.reverse(head)

    values = []
    cur = result
    while cur is not None:
        values.append(str(cur.val))
        cur = cur.next
    print("list:", "->".join(values))



if __name__ == "__main__":
    main()