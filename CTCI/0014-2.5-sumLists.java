//iterative
public static ListNode sumLists(ListNode list1, ListNode list2) {
    ListNode head = list1, prev = null;
    int c = 0;
    while (list1 != null && list2 != null) {
        int sum = list1.val + list2.val + c;
        c = sum / 10;
        list1.val = sum % 10;
        prev = list1;
        list1 = list1.next;
        list2 = list2.next;
    }

    if (list1 != null) {
        list1.val += c;
    }

    if (list2 != null) {
        list2.val += c;
        prev.next = list2;
    }

    return head;
}
