import java.util.*;

public class CommonElementsOptimized {
    public static void main(String[] args) {
        int[] firstArr = { 1, 5, 6, 6, 9, 9, 9, 11, 11, 21 };
        int[] secondArr = { 6, 6, 9, 11, 21, 21, 21 };
        ArrayList<Integer> newarr = new ArrayList<Integer>(10);
        for (int i = 0; i < firstArr.length; i++) {
            if (i < firstArr.length - 1 && firstArr[i] == firstArr[i + 1]) {
                continue;
            } else {
                boolean found = binarySearch(secondArr, 0, secondArr.length, firstArr[i]);
                if (found == true)
                    newarr.add(firstArr[i]);

            }
        }
        for (int i = 0; i < newarr.size(); i++) {
            System.out.print(newarr.get(i) + " ");
        }

    }

    private static boolean binarySearch(int arr[], int left, int right, int x) {
        if (right >= left) {
            int mid = left + (right - left) / 2;

            // If the element is present at the middle itself
            if (arr[mid] == x)
                return true;

            // If element is smaller than mid, then it can only be present in left subarray
            if (arr[mid] > x)
                return binarySearch(arr, left, mid - 1, x);

            // Else the element can only be present in right subarray
            return binarySearch(arr, mid + 1, right, x);
        }

        // We reach here when element is not present in array
        return false;
    }

}
