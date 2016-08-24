//by me
public static String longestString(String str1, String str2) {
  String maxStr = "", temp = "";
  int runnerStr1, runnerStr2;
  for(int i = 0; i < str1.length(); i++) {
    runnerStr1 = i;
    runnerStr2 = 0;
    while(runnerStr1 < str1.length() && runnerStr2 < str2.length()) {
      if(str1.charAt(runnerStr1) != str2.charAt(runnerStr2)) {
        temp = str1.substring(i, runnerStr1);
        runnerStr1 = i;
        runnerStr2++;
      } else if(runnerStr1 == str1.length() - 1 || runnerStr2 == str2.length() - 1){
        temp = str1.substring(i, runnerStr1+1);
        runnerStr1 = i;
        runnerStr2++;
      } else {
        runnerStr1++;
        runnerStr2++;
      }

      if(temp.length() > maxStr.length()) maxStr = temp;
      System.out.println(i + ": " + maxStr);
    }

    if(maxStr.length() >= str1.length() - i) break;
  }

  return maxStr;
}
//by sam - dynamic programming
public static String longestSubstring(String a, String b) {
  String out = "";
  if(a.length() == 0 || b.length() == 0) return out;

  int[][] cache = new int[a.length()][b.length()];
  for(int i = 0; i < a.length(); i++) {
    for(int j = 0; j < b.length(); j++) {
      if(a.charAt(i) == b.charAt(j)) {
        if(i == 0 || j == 0) {
          cache[i][j] = 1;
        } else {
          cache[i][j] = cache[i-1][j-1] + 1;
        }
        if(cache[i][j] > out.length()) {
          out = a.substring(i - cache[i][j] + 1, i + 1);
        }
      }
    }
  }

  return out;
}
