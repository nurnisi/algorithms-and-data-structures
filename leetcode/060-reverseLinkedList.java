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

//recursion
