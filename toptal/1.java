// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

Task 1
if array can be sorted by one swap
example: [1,5,3,3,7]
if we swap A[1] with A[3]
we get [1,3,3,5,7]
it is sorted now

class Solution {
    public boolean solution2(int[] A) {
        int index = -1;
        int value = 0;
        for(int i = 0; i < A.length - 1; i++) {
            if(A[i] > A[i + 1]) {
                index = i + 1;
                value = A[i + 1];
                break;
            }
        }

        if(index == -1) return true;

        int runner = index - 1;

        while (index < A.length - 1 && A[index] == A[index + 1]) index++;

        while(runner >= 0) {
            if(A[runner] < value) {
                int temp = A[runner + 1];
                A[runner + 1] = A[index];
                A[index] = temp;
                break;
            }
            runner--;
        }

        for(int i = 0; i < A.length - 1; i++) {
            if(A[i] > A[i + 1]) {
                return false;
            }
        }

        return true;
    }

    public boolean solution(int[] A) {
        // write your code in Java SE 8
        //int[] B = Arrays.copyOf(A, A.length);

        if (solution2(A)) return true;

        int index = -1;
        int value = 0;
        for(int i = 0; i < A.length - 1; i++) {
            if(A[i] > A[i + 1]) {
                index = i;
                value = A[i];
                break;
            }
        }

        if(index == -1) return true;

        int runner = index + 1;
        while(runner < A.length) {
            if(A[runner] > value) {
                int temp = A[runner - 1];
                A[runner - 1] = A[index];
                A[index] = temp;
                break;
            }
            runner++;
        }

        for(int i = 0; i < A.length - 1; i++) {
            if(A[i] > A[i + 1]) {
                return false;
            }
        }

        return true;
    }
}
