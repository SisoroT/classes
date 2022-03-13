import java.util.Scanner;
import java.util.Queue;
import java.util.ArrayDeque;
import java.util.LinkedList;

public class Dequeue {

    // creating the attribute for queue and dequeue
    Queue<Integer> mainQ;
    ArrayDeque<Integer> maxQ;

    // constructor for the class
    Dequeue() {
        mainQ = new LinkedList<>();
        maxQ = new ArrayDeque<>();
    }

    public static void main(String[] args) throws Exception {
        Dequeue dq = new Dequeue();
        while (true) {
            System.out.println("Menu Options ");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Get Max");
            System.out.println("4. Show Queues");
            System.out.println("5. Quit");

            Scanner sc = new Scanner(System.in);
            int choice = sc.nextInt();
            // allow user to enqueue, dequeue, find max, and show the queues
            switch (choice) {
                case 1:
                    System.out.println("Enter the element");
                    int n = sc.nextInt();
                    dq.enqueue(n);
                    break;
                case 2:
                    System.out.println("Element is removed");
                    dq.dequeue();
                    break;
                case 3:
                    System.out.println("The max-element is " + dq.getMax());
                    break;
                case 4:
                    dq.showQueues();
                    break;
                case 5:
                    return;
                default:
                    System.out.println("Please enter one of the options.");
                    break;
            }
        }
    } // main

    public void enqueue(int data) {
        // find the correct position of the element in the deque and insert it there
        while (!maxQ.isEmpty() && maxQ.getLast() < data) {
            // remove the last element from deque
            maxQ.removeLast();
        }
        // add the element at the end
        maxQ.addLast(data);
        mainQ.add(data);
    } // enqueue

    public void dequeue() {
        // if the element being dequeued matches the current max, remove the current max
        if (maxQ.getFirst() == mainQ.peek()) {
            maxQ.removeFirst();
        }
        mainQ.remove();
    } // dequeue

    // get the maximum element from the queue
    public int getMax() throws Exception {
        // check if the element is empty
        if (mainQ.isEmpty())
            throw new Exception("Queue is Empty");
        else
            return maxQ.getFirst();
    } // getMax

    // print the main and max queue
    public void showQueues() {
        System.out.println("Main: front--> " + mainQ);
        System.out.println("Max: front--> " + maxQ);
    } // showQueues
}
