import java.util.*;

public class Insertion {
    public static void main(String[] args) {
        int[] arr = { 8, 3, 4, 1, 2 };
        insertionSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public static void insertionSort(int arr[]) {

        for (int i = 1; i < arr.length; i++) {
            // save the value that we're looking at
            int current = arr[i];
            int prev = i - 1;

            // make each number equal the number before it
            while (prev >= 0 && arr[prev] > current) {
                arr[prev + 1] = arr[prev];
                prev = prev - 1;
            }
            // set first number equal to the current number
            arr[prev + 1] = current;
        }
    }
}
