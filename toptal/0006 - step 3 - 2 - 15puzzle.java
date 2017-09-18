// Given a 4×4 board with 15 tiles(every tile has one number from 1 to 15) 
// and one empty space.The objective is to place the numbers on tiles in order
// using the empty space.We can slide four adjacent(left, right, above and below) 
// tiles into the empty space.

// http://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/

import java.io.*;
import java.util.*;

public class main {

    public static void main(String[] args) {
        int[][] matrix3x3 = {
                {1, 8, 2},
                {0, 4, 3},
                {7, 6, 5}
        };

        int[][] matrix4x4 = {
                {12, 1, 10, 2},
                {7, 11, 4, 14},
                {5, 9, 0, 15},
                {8, 13, 6, 3}
        };

        System.out.println(isSolvable(matrix4x4));
    }

    public static class InvAndZero {
        public boolean isInversionsEven;
        public boolean isZeroEven;

        public InvAndZero() {
            isInversionsEven = false;
            isZeroEven = false;
        }
    }

    private static InvAndZero countInversions(int[][] matrix) {
        int[] rowArray = new int[matrix.length * matrix[0].length];
        int k = 0;
        InvAndZero result = new InvAndZero();
        for (int i = 0; i < matrix.length; i++)
            for (int j = 0; j < matrix[0].length; j++) {
                rowArray[k++] = matrix[i][j];
                if (matrix[i][j] == 0) result.isZeroEven = i % 2 == 0;
            }


        int inversions = 0;
        for (int i = 0; i < rowArray.length; i++)
            for (int j = i + 1; j < rowArray.length; j++)
                if (rowArray[j] != 0 && rowArray[i] > rowArray[j])
                    inversions++;
        result.isInversionsEven = inversions % 2 == 0;
        return result;
    }

    public static boolean isSolvable(int[][] matrix) {
        InvAndZero result = countInversions(matrix);

        // If the width is odd, then every solvable state has an even number of inversions.
        if (matrix.length % 2 != 0 && result.isInversionsEven) return true;

            // If the width is even, then every solvable state has
            // an even number of inversions if the blank is on an odd numbered row counting from the bottom;
            // an odd number of inversions if the blank is on an even numbered row counting from the bottom;
        else if (matrix.length % 2 == 0 && (!result.isZeroEven == result.isInversionsEven)) return true;

        // unsolvable
        return false;
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