import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        sort();
    }

    static void sort() {
        int n = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int[] sorted = countingSort(arr, 10);

        for (int i : sorted) System.out.print(i + " ");
    }

    static int[] countingSort(int[] arr, int n) {
        int[] countArr = new int[n + 1];

        for (int i = 0; i < arr.length; i++) {
            countArr[arr[i]]++;
        }

        for (int i = 1; i < countArr.length; i++) {
            countArr[i] += countArr[i - 1];
        }

        int[] resArr = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            resArr[countArr[arr[i]] - 1] = arr[i];
            countArr[arr[i]]--;
        }

        return resArr;
    }
}