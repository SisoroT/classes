import java.util.Arrays;

public class Merge {

    // function to merge the subarrays of a[]
    public static void merge(int a[], int beg, int mid, int end) {
        int i, j, k;
        int n1 = mid - beg + 1;
        int n2 = end - mid;

        // temp arrays
        int LeftArray[] = new int[n1];
        int RightArray[] = new int[n2];

        // copy data to temp arrays
        for (i = 0; i < n1; i++)
            LeftArray[i] = a[beg + i];
        for (j = 0; j < n2; j++)
            RightArray[j] = a[mid + 1 + j];

        i = 0;
        j = 0;
        // initial index of merged sub-array
        k = beg;

        while (i < n1 && j < n2) {
            if (LeftArray[i] <= RightArray[j]) {
                a[k] = LeftArray[i];
                i++;
            } else {
                a[k] = RightArray[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            a[k] = LeftArray[i];
            i++;
            k++;
        }

        while (j < n2) {
            a[k] = RightArray[j];
            j++;
            k++;
        }
    }

    public static void mergeSort(int a[], int beg, int end) {
        if (beg < end) {
            int mid = (beg + end) / 2;
            mergeSort(a, beg, mid);
            mergeSort(a, mid + 1, end);
            merge(a, beg, mid, end);
        }
    }

    public static void main(String args[]) {
        int arr[] = { 9, 34, 12, 1, 28, 19, 42, 69 };
        int n = arr.length;

        System.out.println("Before sorting");
        System.out.println(Arrays.toString(arr));

        mergeSort(arr, 0, n - 1);

        System.out.println("\nAfter sorting");
        System.out.println(Arrays.toString(arr));
    }
}
