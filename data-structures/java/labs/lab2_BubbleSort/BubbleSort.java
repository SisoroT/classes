import java.util.*;

public class BubbleSort {
    public static void main(String[] args) {
        // create the array
        int[] arr = { 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 };
        int temp;

        // continuously check to see if the number at j is > j+1 and swap if true
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;

                }
            }
        }

        // print the array
        System.out.println(Arrays.toString(arr));
    }
}
