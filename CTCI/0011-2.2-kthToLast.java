public static ListNode kthToLast(ListNode head, int k) {
    ListNode runner = head;
    while (runner != null && k > 0) {
        runner = runner.next;
        k--;
    }

    if (k > 0) return null;

    ListNode current = head;
    while (runner != null) {
        current = current.next;
        runner = runner.next;
    }

    return current;
}

//recursive
static int index = 0;
public static ListNode kthToLastRecursive(ListNode head, int k) {
    if (head == null) return head;

    ListNode n = kthToLastRecursive(head.next, k);

    index += 1;
    if(index == k) return head;
    return n;
}
