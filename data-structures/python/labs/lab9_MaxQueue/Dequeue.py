from collections import deque as dq


class MaxQueue:
    def __init__(self):
        # queue to store the element to maintain the order of insertion
        self.main_q = dq([])
        # doubly ended queue to get the maximum element in the O(1) time
        self.max_q = dq([])

    def enqueue(self, data: int) -> None:
        """Function to push a element into the queue."""
        # if there is no element in the queue
        if len(self.main_q) == 0:
            self.main_q.append(data)
            self.max_q.append(data)

        else:
            self.main_q.append(data)

            # pop the elements out until the element at
            # back is greater than current element
            while self.max_q and self.max_q[-1] < data:
                self.max_q.pop()

            # add the element at the end of queue
            self.max_q.append(data)

    def dequeue(self) -> None:
        """Function to pop the element out from the queue."""
        # if the element being dequeued matches
        # the current max, remove the current max
        if self.main_q[0] == self.max_q[0]:
            self.max_q.popleft()
        self.main_q.popleft()

    def get_max(self) -> int:
        """Function to get the maximum element from the queue."""
        if len(self.main_q) == 0:
            raise Exception("Queue is empty")
        return self.max_q[0]

    def show_queues(self) -> None:
        """print the main and max queue"""
        print(f"Main: front--> {self.main_q}")
        print(f"Max: front--> {self.max_q}")


if __name__ == "__main__":
    """Driver function that creates a menu of options
    allowing the user to push numbers of their choice,
    pop, get the max and show both the main and max queue.
    """
    deque = MaxQueue()
    while True:
        print("Menu Options ")
        print("1. Push")
        print("2. Pop")
        print("3. Get Max")
        print("4. Show Queues")
        print("5. Quit")

        choice = input()
        # allow user to enqueue, dequeue, find max, and show the queues
        match choice:
            case "1":
                print("Enter the element")
                num = int(input())
                deque.enqueue(num)
            case "2":
                print("Element is removed")
                deque.dequeue()
            case "3":
                print(f"The max-element is {deque.get_max()}")
            case "4":
                deque.show_queues()
            case "5":
                break
            case _:
                print("Please enter one of the options.")
