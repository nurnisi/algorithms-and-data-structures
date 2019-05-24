//stack
public static ListNode reverseList(ListNode head) {
    if (head == null) return head;
    Deque<ListNode> stack = new LinkedList<>();
    while (head != null) {
        stack.push(head);
        head = head.next;
    }
    ListNode newHead = stack.pop(), runner = newHead;
    while (!stack.isEmpty()) {
        runner.next = stack.pop();
        runner = runner.next;
    }
    runner.next = null;

    return newHead;
}

//iterative without stack
public static ListNode reverseList(ListNode head) {
    ListNode newHead = null;
    while(head != null) {
        ListNode next = head.next;
        head.next = newHead;
        newHead = head;
        head = next;
    }
    return newHead;
}

//recursion
public static ListNode reverseList(ListNode head) {
    return helper(head, null);
}

private static ListNode helper(ListNode head, ListNode newHead) {
    if (head == null) return newHead;
    ListNode next = head.next;
    head.next = newHead;
    return helper(next, head);
}
