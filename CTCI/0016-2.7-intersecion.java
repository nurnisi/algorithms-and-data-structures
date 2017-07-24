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
public static ListNode intersectionWithoutBuffer(ListNode list1, ListNode list2) {
  if(list1 == null || list2 == null) return null;

  ListNode temp1 = list1, temp2 = list2;
  int size1 = 1, size2 = 1;
  while (temp1.next != null) {
    temp1 = temp.next;
    size1++;
  }
  while (temp2.next != null) {
    temp2 = temp2.next;
    size2++;
  }
  if (temp1 != temp2) return null;

  ListNode longer = size1 > size2 ? list1 : list2;
  ListNode shorter = size1 > size2 ? list2 : list1;

  int diff = Math.abs(size1 - size2);
  while (diff > 0 && longer != null) {
    longer = longer.next;
    diff--;
  }

  while (longer != shorter) {
    longer = longer.next;
    shorter = shorter.next;
  }

  return longer;
}
