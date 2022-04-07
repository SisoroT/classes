from collections import deque as dq


class MaxQueue:
    def __init__(self):
        # queue to store the element to maintain the order of insertion
        self.main_q = dq([])
        # doubly ended queue to get the maximum element in the O(1) time
        self.max_q = dq([])

    def enque_element(self, element):
        """Function to push a element into the queue"""
        # If there is no element
        # in the queue
        if len(self.main_q) == 0:
            self.main_q.append(element)
            self.max_q.append(element)

        else:
            self.main_q.append(element)

            # Pop the elements out
            # until the element at
            # back is greater than
            # current element
            while self.max_q and self.max_q[-1] > element:
                self.max_q.pop()

            self.max_q.append(element)

    def deque_element(self):
        """Function to pop the element out from the queue"""
        # condition when the minimum
        # element is the element at
        # the front of the deque
        if self.main_q[0] == self.max_q[0]:
            self.main_q.popleft()
            self.max_q.popleft()

        else:
            self.main_q.popleft()

    def get_max(self):
        """function to get the maximum element from the queue"""
        return self.max_q[0]


if __name__ == "__main__":
    deque = MaxQueue()
    example = [1, 2, 4]

    # loop to enqueue element
    for i in range(3):
        deque.enque_element(example[i])

    print(deque.get_max())
    deque.deque_element()
    print(deque.get_max())
