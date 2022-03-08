import java.util.*;

public class Rotation {
    public static void main(String[] args) {
        int[][] arr = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 }, { 13, 14, 15, 16 } };

        System.out.println("Before Rotation: " + Arrays.deepToString(arr));
        ClockwiseRotation(arr);
        System.out.println("After Rotation: " + Arrays.deepToString(arr));
    }

    public static void ClockwiseRotation(int[][] arr) {
        int[][] newArr = new int[arr.length][arr[0].length];

        // rewrite the rows of newArr as the columns of arr
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                newArr[i][j] = arr[arr[0].length - 1 - j][i];
                // System.out.print(newArr[i][j] + " ");
            }
            // System.out.println();
        }

        // overwrite arr with the contents of newArr
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                arr[i][j] = newArr[i][j];
            }
        }
    }
}
