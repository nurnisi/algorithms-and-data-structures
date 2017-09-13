import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int[] start = {10, 12, 20};
        int[] finish = {20, 25, 30};

        activitySelection(start, finish);
    }

//    You are given n activities with their start and finish times. Select the maximum number of activi-
//    ties that can be performed by a single person, assuming that a person can only work on a single
//    activity at a time.

//    Example 1 : Consider the following 3 activities sorted by
//    by finish time.
//            start[]  =  {10, 12, 20};
//    finish[] =  {20, 25, 30};
//    A person can perform at most two activities. The
//    maximum set of activities that can be executed
//    is {0, 2} [ These are indexes in start[] and
//    finish[] ]

//    Example 2 : Consider the following 6 activities
//    sorted by by finish time.
//            start[]  =  {1, 3, 0, 5, 8, 5};
//    finish[] =  {2, 4, 6, 7, 9, 9};
//    A person can perform at most four activities. The
//    maximum set of activities that can be executed
//    is {0, 1, 3, 4} [ These are indexes in start[] and
//    finish[] ]

    public static void activitySelection(int[] start, int[] finish) {
        int[][] activities = new int[start.length][2];

        for (int i = 0; i < start.length; i++) {
            activities[i][0] = start[i];
            activities[i][1] = finish[i];
        }

        Arrays.sort(activities, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                final Integer int1 = o1[1];
                final Integer int2 = o2[1];
                return int1.compareTo(int2);
            }
        });

        int counter = 1;
        for (int i = 0, j = 1; j < activities.length; j++) {
            if (activities[i][1] <= activities[j][0]) {
                counter++;
                i = j;
            }
        }

        System.out.println(counter);
    }
}

