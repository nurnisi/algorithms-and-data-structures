public class kthMostFrequent {

  kthMostFrequent({"a","b","c","a","b","a"}, 0) = "a"
  kthMostFrequent({"a","b","c","a","b","a"}, 1) = "b"
  kthMostFrequent({"a","b","c","a","b","a"}, 2) = "c"
  kthMostFrequent({"a","b","c","a","b","a"}, 3) = null

    list = (
      0 => (a -> 3),
      1 => (b -> 2),
      2 => (c -> 1)
    )

  public String kthMostFrequent(String[] strArray, int k) {
    HashMap<String, Integer> map = new HashMap<String, Integer>();

    for(string s : strArray) {
      Integer x = map.get(s);
      if(x == null) x = 0;
      map.put(s, ++x);
    }

    List<Map.Entry> list = new Arraylist(map.entrySet());

    Collections.sort(list, new Comparator() {
      public int compare(Object o1, Object o2) {
        Integer v1 = (Integer) ((Map.Entry) o1).getValue();
        Integer v2 = (Integer) ((Map.Entry) o2).getValue();
        return v1.compareTo(v2);
      }
    });

    if(list.size() > k) return (String) (list.get(k)).getKey();
    return null;
  }

}
