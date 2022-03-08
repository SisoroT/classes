import java.util.*;

public class DeDuplication {

    public static void main(String[] args) {

        // int arr[] = { 11, 21, 21, 33, 40, 40, 40, 50, 50 };
        // user creates an array
        int arr[] = makeArray();

        int lastUniqueIndex = removeDuplicates(arr, arr.length);

        // print the array up until the index of the last unique element
        for (int i = 0; i < lastUniqueIndex; i++)
            System.out.print(arr[i] + " ");
    }

    public static int removeDuplicates(int[] arr, int n) {
        // if array has a length of 0 or 1 then it is sorted already
        if (n == 0 || n == 1) {
            return n;
        }

        int[] temp = new int[n];
        int uniques = 0;

        for (int i = 0; i < n - 1; i++) {
            // if current number doesnt equal the next then that number is unique and add it
            // to the temp array
            if (arr[i] != arr[i + 1]) {
                temp[uniques++] = arr[i];
            }
        }

        // add the last unique number
        temp[uniques++] = arr[n - 1];

        // copy all the unique elements in order onto the original array
        for (int i = 0; i < uniques; i++) {
            arr[i] = temp[i];
        }

        // return the index of the last unique element
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
