import java.util.Scanner;

public class CommonElements {
    public static void main(String[] args) {
        int n, m, k = 0;
        // int[] arr1 = { 1, 5, 6, 6, 9, 9, 9, 11, 11, 21 };
        // int[] arr2 = { 6, 6, 9, 11, 21, 21, 21 };
        System.out.println("Array 1:");
        int[] arr1 = makeArray();
        System.out.println("Array 2:");
        int[] arr2 = makeArray();
        int[] array = new int[15];
        n = removeDuplicatesOptimized(arr1, arr1.length);
        m = removeDuplicatesOptimized(arr2, arr2.length);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr1[i] == arr2[j]) {
                    array[k] = arr1[i];
                    k++;
                }
            }
        }
        System.out.println("elements of the array are: ");
        for (int i = 0; i < k; i++)
            System.out.print(array[i] + " ");
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
        return arr;
    }
}
