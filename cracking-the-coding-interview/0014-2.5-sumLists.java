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

//recursive
public static ListNode sumListsRecursive(ListNode list1, ListNode list2, int c) {
    if (list1 == null && list2 == null && c == 0) return null;

    int sum = c;
    if (list1 != null) sum += list1.val;
    if (list2 != null) sum += list2.val;
    ListNode res = new ListNode(sum % 10);

    if (list1 != null || list2 != null) {
        res.next = sumListsRecursive(
                            list1 != null ? list1.next : null,
                            list2 != null ? list2.next : null,
                            sum / 10);

    }

    return res;
}

//forward order: recursive
public static ListNode sumListsForward(ListNode list1, ListNode list2) {
    int i1 = 0, i2 = 0;
    ListNode temp1 = list1, temp2 = list2;
    while (temp1 != null) {
        i1++;
        temp1 = temp1.next;
    }

    while (temp2 != null) {
        i2++;
        temp2 = temp2.next;
    }

    return sumListsForward(list1, list2, i1, i2);
}

static int carry = 0;
public static ListNode sumListsForward(ListNode list1, ListNode list2, int i1, int i2) {
    if (list1 == null && list2 == null) return null;

    ListNode n;
    int sum;
    if (i1 > i2) {
        n = sumListsForward(list1.next, list2, --i1, i2);
        sum = list1.val + carry;
    } else if (i1 < i2) {
        n = sumListsForward(list1, list2.next, i1, --i2);
        sum = list2.val + carry;
    } else {
        n = sumListsForward(list1.next, list2.next, --i1, --i2);
        sum = list1.val + list2.val + carry;
    }

    carry = sum / 10;
    ListNode head = new ListNode(sum % 10);
    head.next = n;
    return head;
}
