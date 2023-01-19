import java.util.Arrays;

public class HW1 {

    public static void main(String[] args) {
        // Q1
        System.out.println("Q1:");
        int testResult1 = findMissing(new int[] { 0, 1, 2, 4, 5 });
        System.out.println(testResult1); // should output 3

        int testResult2 = findMissing(new int[] { 5, 0, 4, 3, 1 });
        System.out.println(testResult2); // should output 2

        int testResult3 = findMissing(new int[] {});
        System.out.println(testResult3); // should output 0

        int testResult4 = findMissing(new int[] { 9, 3, 5, 1, 4, 8, 2, 10, 0, 6 });
        System.out.println(testResult4); // should output 7

        // Q3
        System.out.println("\nQ3:");
        System.out.println(countFives(123467890)); // should output 0
        System.out.println(countFives(555555)); // should output 6
        System.out.println(countFives(15354)); // should output 2

        // Q4
        System.out.println("\nQ4:");
        int testResult5 = pickTrees(new int[] { 1, 2, 3, 4, 5 });
        System.out.println(testResult5); // should output 9

        int testResult6 = pickTrees(new int[] { 1, 3, 4, 3 });
        System.out.println(testResult6); // should output 6

        int testResult7 = pickTrees(new int[] { 5, 1, 4, 9 });
        System.out.println(testResult7); // should output 14
    }

    /**
     * Calculate what the sum should be then subtract the sum of the values in the
     * array.
     */
    public static int findMissing(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }

        int n = arr.length;
        // calculate what the sum should be
        int shouldBeSum = n * (n + 1) / 2;
        int sum = 0;

        // find the sum of the values in the array
        for (int num : arr)
            sum += num;

        // return the remaining number
        return shouldBeSum - sum;
    }

    /**
     * // Q2: TWOSUM PSEUDOCODE ALGORITHM
     *
     * algo twoSum(int array, int target) {
     *
     * create hashmap
     *
     * loop (elements in array){
     *
     * diff = target - arr[i]
     *
     * if (hashmap has key(diff)): return hashmapValue(diff), i
     *
     * else: hashmap.add(arr[i],i)
     *
     * }
     *
     * return -1, -1
     *
     * }
     **/

    /**
     * Loop using modulo to get the current digit, incrementing fives if the current
     * number is a five until num is 0.
     */
    public static int countFives(int num) {
        // when num reaches 0 stop recurring
        if (num == 0) {
            return 0;
        }
        // initialize variable to hold number of fives in num
        int fives = 0;

        // if ones place in num = 5 add 1 to fives
        if (num % 10 == 5)
            fives++;

        // get rid of the ones place of num and call countFives again
        return fives + countFives(num / 10);
    }

    // write a recursive function that calculates the maximum sum in a given array
    // with no adjacent elements considered
    public static int pickTrees(int[] arr) {
        // if array is empty return 0
        if (arr.length == 0) {
            return 0;
        }
        // if array is 1 element return the only element
        if (arr.length == 1) {
            return arr[0];
        }
        // if array has 2 elements return the larger of the two
        if (arr.length == 2) {
            return Math.max(arr[0], arr[1]);
        }

        // create a new array that is one element smaller than the original array
        int[] smallerArray = Arrays.copyOfRange(arr, 1, arr.length);

        // return the larger of the two options
        return Math.max(arr[0] + pickTrees(Arrays.copyOfRange(smallerArray, 1, smallerArray.length)),
                pickTrees(smallerArray));
    }
}
