public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = { 0, 1, 2, 3, 5, 7, 9, 12, 13 };
        System.out.println("The target is found at index " + binarySearchRecursive(arr, 9, 0, arr.length));
    }

    public static int binarySearchRecursive(int[] arr, int target, int low, int high) {
        int mid = (low + high) / 2;
        if (low <= high) {
            if (arr[mid] == target)
                return mid;
            if (arr[mid] < target)
                return binarySearchRecursive(arr, target, mid + 1, high);
            if (arr[mid] > target)
                return binarySearchRecursive(arr, target, low, mid - 1);
        }
        return -1;
    }
}
