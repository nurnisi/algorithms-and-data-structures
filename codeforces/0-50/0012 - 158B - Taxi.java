import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int i = Integer.parseInt(sc.nextLine());
        int[] arr = new int[5];

        for (int j = 0; j < i; j++) {
            int k = sc.nextInt();
            arr[k]++;
        }

        //4
        int cars = arr[4];

        //3 + 1
        int more1 = arr[1] > arr[3] ? arr[3] : arr[1];
        cars += more1;
        arr[1] -= more1;
        arr[3] -= more1;

        //1 + 1 + 1 + 1
        cars += arr[1]/4;
        arr[1] %= 4;

        //2 + 2
        cars += arr[2]/2;
        arr[2] %= 2;

        //2 + 1 + 1
        int more3 = arr[1]/2;
        more3 = more3 < arr[2] ? more3 : arr[2];
        cars += more3;
        arr[2] -= more3;
        arr[1] -= more3*2;

        //2 + 1
        int more2 = arr[1] > arr[2] ? arr[2] : arr[1];
        cars += more2;
        arr[1] -= more2;
        arr[2] -= more2;

        //rest
        if (arr[1] > 0 && arr[1] < 4) cars++;
        cars += arr[2];
        cars += arr[3];

        System.out.println(cars);
    }
}