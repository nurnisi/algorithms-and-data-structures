public class anagrams {

  public boolean isAnagrams(String str1, String str2) {
    if(str1.length() != str2.length()) return false;

    int[] container = new int[26];
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();

    for(int i = 0; i < str1.length(); i++) {
      char char1 = str1.charAt(i);
      char char2 = str2.charAt(i);

      container[char1 - 97] += 1;
      contaienr[char2 - 97] -= 1;
    }

    for(int i : container)
      if(i != 0) return false;

    return true;
  }

}
