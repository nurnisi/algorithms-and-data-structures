public static void deleteMiddleNode(ListNode middle) {
    if (middle == null || middle.next == null) return;

    middle.val = middle.next.val;
    middle.next = middle.next.next;
}
