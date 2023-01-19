import java.util.*;

public class SelectionDeDuplication {
    public static void main(String[] args) {
        // have the user create an array
        int[] arr = makeArray();

        // sort the array
        selectionSort(arr);

        // lastUniqueIndex = the index of the last unique value
        int lastUniqueIndex = removeDuplicatesOptimized(arr, arr.length);

        // print the array up until the index of the last unique value
        for (int i = 0; i < lastUniqueIndex; i++)
            System.out.print(arr[i] + " ");
    }

    public static void selectionSort(int arr[]) {
        int temp;

        // if the array length is 1 there is no need to sort --test case
        if (arr.length == 1) {
            System.out.println("This array is already sorted.");
        } else {

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
