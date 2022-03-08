import java.util.Arrays;

public class QuickSorting {
    public static void main(String[] args) {
        int[] arr = { 2, 0, 9, 5, 7, 5, 2, 1 };
        quickSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
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
}
