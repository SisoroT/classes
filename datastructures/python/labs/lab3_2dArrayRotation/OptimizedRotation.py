import java.util.*;

public class OptimizedRotation {
    public static void main(String[] args) {
        int[][] arr = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 }, { 13, 14, 15, 16 } };

        System.out.println("Before Rotation: " + Arrays.deepToString(arr));
        OptimizedClockwiseRotation(arr);
        System.out.println("After Rotation: " + Arrays.deepToString(arr));
    }

    public static int[][] OptimizedClockwiseRotation(int[][] arr) {
        int temp;
        int n = arr[0].length;

        // rotate a group of n elements at a time in a clockwise direction collapsing
        // towards the middle of the array until the whole array has been rotated
        for (int i = 0; i < n - 1; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                temp = arr[i][j];
                arr[i][j] = arr[n - 1 - j][i];
                arr[n - 1 - j][i] = arr[n - 1 - i][n - 1 - j];
                arr[n - 1 - i][n - 1 - j] = arr[j][n - 1 - i];
                arr[j][n - 1 - i] = temp;
            }
        }
        return arr;
    }
}

// although this both solutions have the same time complexity (quadratic or n^2)
// this solution has a better space complexity. Since it doesn't initialize
// another 2d array, its space complexity is constant while the first solution
// has a space complexity of n^2 because it created another 2d array.
