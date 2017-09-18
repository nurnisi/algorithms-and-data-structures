// Given a 4×4 board with 15 tiles(every tile has one number from 1 to 15) 
// and one empty space.The objective is to place the numbers on tiles in order
// using the empty space.We can slide four adjacent(left, right, above and below) 
// tiles into the empty space.

// http://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/

import java.io.*;
import java.util.*;

public class main {
    public static void main(String[] args) {

    }

    public static int countInversions() {

    }
}

// Given a 3×3 board with 8 tiles (every tile has one number from 1 to 8) and one 
// empty space. The objective is to place the numbers on tiles in order using the 
// empty space. We can slide four adjacent (left, right, above and below) tiles 
// into the empty space.

// http://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/

import java.io.*;
import java.util.*;

public class main {
    public static void main(String[] args) {
        int[][] matrix = {
                {1, 8, 2},
                {0, 4, 3},
                {7, 6, 5}
        };

        System.out.println(isSolvable(matrix));
    }

    private static int countInversions(int[][] matrix) {
        int[] rowArray = new int[matrix.length * matrix[0].length];
        int k = 0;
        for (int i = 0; i < matrix.length; i++)
            for (int j = 0; j < matrix[0].length; j++)
                rowArray[k++] = matrix[i][j];

        int inversions = 0;
        for (int i = 0; i < rowArray.length; i++)
            for (int j = i + 1; j < rowArray.length; j++)
                if (rowArray[j] != 0 && rowArray[i] > rowArray[j])
                    inversions++;

        return inversions;
    }

    public static boolean isSolvable(int[][] matrix) {
        return countInversions(matrix) % 2 == 0 ? true : false;
    }
}