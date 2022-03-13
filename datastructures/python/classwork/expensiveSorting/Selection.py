import java.util.*;

public class Selection {
    public static void main(String[] args) {
        int[] arr = { 8, 3, 4, 1, 2 };
        selectionSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public static void selectionSort(int arr[]) {
        int temp;

        for (int i = 0; i < arr.length - 1; i++) {
            int minLocation = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minLocation])
                    minLocation = j;
            }

            // put i in the correct location
            temp = arr[i];
            arr[i] = arr[minLocation];
            arr[minLocation] = temp;
        }
    }
}
