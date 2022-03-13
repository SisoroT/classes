import java.util.*;

public class MergeDeDuplication {
    public static void main(String[] args) {
        // have the user create an array
        int[] arr = makeArray();
        // int[] arr = { 50, 11, 33, 21, 40, 50, 40, 40, 21 };

        // sort the array
        mergeSort(arr, arr.length);

        // lastUniqueIndex = the index of the last unique value
        int lastUniqueIndex = removeDuplicatesOptimized(arr, arr.length);

        // print the array up until the index of the last unique value
        for (int i = 0; i < lastUniqueIndex; i++)
            System.out.print(arr[i] + " ");
    }

    public static void mergeSort(int[] arr, int n) {
        // if the arrays length is less
        // than 2 it is already sorted
        if (n < 2) {
            return;
        }
        int mid = n / 2;
        // create new arrays for both halves of the array
        int[] left = new int[mid];
        int[] right = new int[n - mid];

        // fill left and right arrays
        for (int i = 0; i < mid; i++) {
            left[i] = arr[i];
        }
        for (int i = mid; i < n; i++) {
            right[i - mid] = arr[i];
        }

        // continue until base case is reached
        mergeSort(left, mid);
        mergeSort(right, n - mid);

        sort(arr, left, right, mid, n - mid);
    }

    public static void sort(int[] arr, int[] l, int[] r, int left, int right) {

        int i = 0, j = 0, k = 0;
        while (i < left && j < right) {
            if (l[i] <= r[j]) {
                arr[k++] = l[i++];
            } else {
                arr[k++] = r[j++];
            }
        }
        while (i < left) {
            arr[k++] = l[i++];
        }
        while (j < right) {
            arr[k++] = r[j++];
        }
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
