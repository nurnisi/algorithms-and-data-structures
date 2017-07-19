//with creating new linked list
public static ListNode partition(ListNode n, int partition) {
    if (n == null || n.next == null) return n;

    ListNode head = new ListNode(n.val), tail = head;
    while (n.next != null) {
        int val = n.next.val;
        if (val >= partition) {
            tail.next = new ListNode(val);
            tail = tail.next;
        }
        else {
            ListNode newHead = new ListNode(val);
            newHead.next = head;
            head = newHead;
        }
        n = n.next;
    }
    tail.next = null;

    return head;
}
