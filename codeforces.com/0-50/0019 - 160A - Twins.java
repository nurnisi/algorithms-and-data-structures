import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int i = Integer.parseInt(sc.nextLine());

        Integer[] array = new Integer[i];
        int sum = 0;
        for (int j = 0; j < i; j++) {
            int k = sc.nextInt();
            array[j] = k;
            sum += k;
        }

        Arrays.sort(array, Collections.reverseOrder());

        sum = sum / 2;
        int checkSum = 0;
        int j = 0;
        for (; j < array.length; j++) {
            checkSum += array[j];
            if (checkSum > sum) {
                break;
            }
        }
        System.out.println(j + 1);
    }
}

