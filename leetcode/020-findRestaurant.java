public String[] findRestaurant(String[] list1, String[] list2) {
    Map<String, Integer> first = new HashMap<>();
    for(int i = 0; i < list1.length; i ++) {
      first.put(list1[i], i);
    }

    Map<String, Integer> second = new HashMap<>();
    for(int j = 0; j < list2.length; j ++) {
      second.put(list2[j], j);
    }

    List<String> temp = new ArrayList<>();
    int min = Integer.MAX_VALUE;
    for(Map.Entry<String, Integer> entry: first.entrySet()) {
      if(second.get(entry.getKey()) != null) {
        int check = entry.getValue() + second.get(entry.getKey());
        if(min > check) {
          temp = new ArrayList<String>();
          min = check;
          temp.add(entry.getKey());
        } else if(min == check) {
          temp.add(entry.getKey());
        }
      }
    }

    String[] res = new String[temp.size()];
    res = temp.toArray(res);

    return res;
}
