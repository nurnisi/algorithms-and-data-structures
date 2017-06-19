// you can also use imports, for example:
import java.util.*;
// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

Task 3
jumping frog and stones
at what iteration frog will jump over the river

class Solution {
    public int solution(int[] A, int D) {
        // write your code in Java SE 8
        if(D > A.length) return 0;

        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        for(int i = 0; i < A.length; i++) {
               if(A[i] != -1) hm.put(A[i], i);
        }
        Arrays.sort(A);
        ArrayList<Integer> b = new ArrayList<Integer>();
        b.add(-1);
        b.add(A.length);
        for(int i = 0; i < A.length; i++) {
            if(A[i] == -1) continue;
            b.add(hm.get(A[i]));
            Collections.sort(b);
            boolean flag = false;
            for(int j = 0; j < b.size() - 1; j++) {
                if (b.get(j + 1) - b.get(j) > D) {
                    flag = true;
                    break;
                }
            }
            if (!flag) return A[i];
        }
        return -1;
    }
}
