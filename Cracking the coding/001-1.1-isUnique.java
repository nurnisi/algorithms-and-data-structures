//set
public static boolean isUnique(String str) {
    Set<Character> set = new HashSet<>();
    for (char ch : str.toCharArray()) {
        if (set.contains(ch)) return false;
        set.add(ch);
    }
    return true;
}

//loop
public static boolean isUnique(String str) {
    for (int i = 0; i < str.length() - 1; i++)
        for (int j = i + 1; j < str.length(); j++)
            if (str.charAt(i) == str.charAt(j)) return false;
    return true;
}

//solution from book

//ask if the string is unicode or ascii
//if it is unicode increase the storage size
//if it is ascii, ask if it is extended ascii or not extended

//ascii with array
public static boolean isUnique(String str) {
  if (str.length() > 128) return false;

  boolean[] check = new boolean[128];
  for (char ch : str.toCharArray()) {
    if (check[ch]) return false;
    check[ch] = true;
  }

  return true;
}

//alphabet with single integer
public static boolean isUnique(String str) {
  if (str.length() > 26) return false;

  int i = 0;
  for (char ch : str.toCharArray()) {
      int val = ch - 'a';
      if ((i >> val & 1) > 0) return false;
      i |= 1 << val;
  }

  return true;
}
