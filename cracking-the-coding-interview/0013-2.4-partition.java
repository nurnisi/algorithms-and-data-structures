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


//without buffer - in place
public static void partitionWithoutBuffer(ListNode n, int partition) {
    while (n != null && n.next != null) {
        if (n.val >= partition) {
            ListNode runner = n.next;
            while (runner != null) {
                if (runner.val < partition) {
                    int temp = runner.val;
                    runner.val = n.val;
                    n.val = temp;
                    break;
                }
                runner = runner.next;
            }
            if (runner == null) return;
        }
        n = n.next;
    }
}
