
public class FindKthSmallest {
    public static int kthSmallest(int A[], int startA, int endA, int B[], int startB, int endB, int k) {
        int n = endA - startA;
        int m = endB - startB;

        if (n <= 0)
            return B[startB + k - 1];
        if (m <= 0)
            return A[startA + k - 1];
        if (k == 1)
            return A[startA] < B[startB] ? A[startA] : B[startB];

        int midA = (startA + endA) / 2;
        int midB = (startB + endB) / 2;

        if (A[midA] <= B[midB]) {
            if (n / 2 + m / 2 + 1 >= k)
                return kthSmallest(A, startA, endA, B, startB, midB, k);
            else
                return kthSmallest(A, midA + 1, endA, B, startB, endB, k - n / 2 - 1);
        } else {
            if (n / 2 + m / 2 + 1 >= k)
                return kthSmallest(A, startA, midA, B, startB, endB, k);
            else
                return kthSmallest(A, startA, endA, B, midB + 1, endB, k - m / 2 - 1);

        }
    }
}
