public ListNode removeElements(ListNode head, int val) {
    while(head != null && head.val == val) head = head.next;
    ListNode runner = head;
    while(runner != null && runner.next != null) {
        if(runner.next.val == val) runner.next = runner.next.next;
        else runner = runner.next;
    }
    return head;
}
