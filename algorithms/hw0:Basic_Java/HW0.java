import java.util.*;

public class HW0 {

    public static void main(String[] args) {
        // Q1
        int testResult1 = maxOfArray(new int[] { 1, 3, 4, 5, 2 });
        int testResult2 = maxOfArray(new int[] { -1, -3, -4, -5, -2 });

        System.out.println(testResult1); // should output 5
        System.out.println(testResult2); // should output -1
        boolean emptyCaseCorrect = false;
        try {
            maxOfArray(new int[] {});
        } catch (IllegalArgumentException e) {
            emptyCaseCorrect = true;
        }
        if (emptyCaseCorrect) {
            System.out.println("maxOfArray appears to work for the empty array case");
        } else {
            System.out.println("maxOfArray appears to be incorrect for the empty array case");
        }

        // Q2
        int[] testResult3 = twoSum(new int[] { 0, 2, 3, 4, 5 }, 6);
        int[] testResult4 = twoSum(new int[] { 1, 2, 3, 4, 5 }, 10);

        System.out.println(Arrays.toString(testResult3)); // should output [1, 3]
        System.out.println(Arrays.toString(testResult4)); // should output [-1, -1]

        // Q3
        List<Integer> testResult5 = add(Arrays.asList(1, 2, 3), Arrays.asList(2, 4, 2));
        List<Integer> testResult6 = add(Arrays.asList(9, 9, 9), Arrays.asList(1));

        System.out.println(testResult5); // should output [3, 6, 5]
        System.out.println(testResult6); // should output [1, 0, 0, 0]
    }

    /**
     * Loop through an array and compare the current element with the recorded
     * maximum value. Once through the entire array, return the maximum recorded
     * value.
     */
    public static int maxOfArray(int[] arr) {

        // if array is empty, throw an exception
        if (arr.length < 1) {
            throw new IllegalArgumentException("Array is empty.");
        }

        int currMax = Integer.MIN_VALUE;

        // for each element of the array save greater
        // between current max and current element
        for (int elm : arr) {
            currMax = Math.max(currMax, elm);
        }

        // return max value
        return currMax;
    }

    /**
     * Create a hashmap and loop through the array of elements adding each element
     * to the hashmap until the difference between the target sum and the current
     * element is found in the hashmap. Once found, return the current index and the
     * index of the key found in the hashmap.
     */
    public static int[] twoSum(int[] arr, int targetSum) {
        // hashmap to hold arr elements with instant lookup
        HashMap<Integer, Integer> prevMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < arr.length; i++) {
            // store difference between target and current element as diff
            int diff = targetSum - arr[i];

            // if the hashmap contains the key diff, return the
            // value for that key and the current loop index
            if (prevMap.containsKey(diff)) {
                return new int[] { prevMap.get(diff), i };
            }
            // if the hashmap doesnt contain diff, then add
            // the current element and index to the hashmap
            prevMap.put(arr[i], i);
        }

        // in all other situations, there are no elements in
        // arr that add up to targetSum so return {-1,-1}
        return new int[] { -1, -1 };
    }

    /**
     * Loop through each list to convert the lists to integers, add the integers
     * together, and return the sum in the form of a new integer list.
     */
    public static List<Integer> add(List<Integer> lst1, List<Integer> lst2) {
        // if both lists are empty return a list containing -1
        if (lst1.size() == 0 && lst2.size() == 0) {
            return Arrays.asList(-1);
        }

        // if 1 list is empty return the other
        else if (lst1.size() == 0) {
            return lst2;
        } else if (lst2.size() == 0) {
            return lst1;
        }

        // create an integer list to hold the answer
        List<Integer> sumList = new ArrayList<Integer>();

        // hold the int values of lst1 and lst2
        int num1 = 0;
        int num2 = 0;

        // convert lst1 to an integer num1
        for (int num : lst1) {
            num1 *= 10;
            num1 += num;
        }
        // convert lst2 to an integer num2
        for (int num : lst2) {
            num2 *= 10;
            num2 += num;
        }

        // create a string with the sum of num1 and num2
        String sumAsStr = Integer.toString(num1 + num2);

        // convert each character in 'sumAsStr' to
        // an integer and add it to the sum list
        for (int i = 0; i < sumAsStr.length(); i++) {
            sumList.add(Character.getNumericValue(sumAsStr.charAt(i)));
        }

        return sumList;
    }
}
