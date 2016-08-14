public class compress {

  public String compress(String s) {
    if(s.length == 0 || s.length == 1) return s;

    String result = "";

    int i = 0, j = 1;

    while(j < s.length()) {
      while(s.charAt(i) == s.charAt(j))
        j++;

      result += (s.charAt(i) + (j - i));
      i = j++;
    }
  }

}
