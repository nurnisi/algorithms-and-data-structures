public static ListNode intersection(ListNode list1, ListNode list2) {
  Set<ListNode> set = new HashSet<>();
  while (list1 != null) {
    set.add(list1);
    list1 = list1.next;
  }
  while (list2 != null) {
    if (set.contains(list2)) return list2;
    list2 = list2.next;
  }
  return null;
}
//without buffer CTCI
