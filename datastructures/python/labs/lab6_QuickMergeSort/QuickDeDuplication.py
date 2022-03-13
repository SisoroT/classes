import java.util.*;

public class QuickDeDuplication {
    public static void main(String[] args) {
        // have the user create an array
        int[] arr = makeArray();
        // int[] arr = { 50, 11, 33, 21, 40, 50, 40, 40, 21 };

        // sort the array
        quickSort(arr, 0, arr.length - 1);

        // lastUniqueIndex = the index of the last unique value
        int lastUniqueIndex = removeDuplicatesOptimized(arr, arr.length);

        // print the array up until the index of the last unique value
        for (int i = 0; i < lastUniqueIndex; i++)
            System.out.print(arr[i] + " ");
    }

    public static void quickSort(int arr[], int first, int last) {
        if (first < last) {
            // partIndex is now at right place
            int partIndex = partition(arr, first, last);

            // Separately sort elements before and after partition
            quickSort(arr, first, partIndex - 1);
            quickSort(arr, partIndex + 1, last);
        }
    }

    public static int partition(int[] arr, int first, int last) {
        int pivot = arr[last];
        int i = (first - 1);

        for (int j = first; j < last; j++) {
            // if current element is less than the
            // pivot, increment i and swap i and j
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        // place pivot in correct place and return its index
        swap(arr, i + 1, last);
        return i + 1;
    }

    public static void swap(int[] arr, int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    public static int removeDuplicatesOptimized(int[] arr, int n) {
        // if array has a length of 0 or 1 then it has no duplicates --test case
        if (n == 0 || n == 1) {
            return n;
        }

        int uniques = 0;

        // if i!=i+1 then it is unique so place i at the next unique index of the array
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] != arr[i + 1]) {
                arr[uniques++] = arr[i];
            }
        }

        // add the last unique number
        arr[uniques++] = arr[n - 1];

        return uniques;
    }

    public static int[] makeArray() {
        Scanner scanner = new Scanner(System.in);

        // user decides how long they want the array
        System.out.print("How long would you like to make your array? ");
        int length = scanner.nextInt();

        // if user enters a non positive number, prompt them to enter a positive
        while (length <= 0) {
            System.out.println("Please enter a positive number. ");
            length = scanner.nextInt();
        }

        // create a new array at the length specified by the user
        int[] arr = new int[length];

        // have the user enter all the elements for the array
        for (int i = 0; i < length; i++) {
            System.out.println("Enter element " + i + " or your array. ");
            arr[i] = scanner.nextInt();
        }

        // close the scanner and return the array
        scanner.close();
        return arr;
    }
}
