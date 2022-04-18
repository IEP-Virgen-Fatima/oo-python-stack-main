from typing import Final

class StackOfNonNegativeIntegers:
    """
    Stack of non negative integers, with given capacity.
    """

    DEFAULT_CAPACITY : Final[int] = 5
    """
    Default capacity.
    """

    SUCCESS: Final[int] = 0
    """
    Return status for success.
    """

    STACK_IS_FULL: Final[int] = -1
    """
    Return status for full stack error.
    """

    STACK_IS_EMPTY: Final[int] = -2
    """
    Return status for empty stack error.
    """

    ELEMENT_IS_NEGATIVE: Final[int] = -3
    """
    Return status for negative element error.
    """

    def __init__(self, capacity=None):
        """
        Creates a new stack instance with given capacity (optional).

        :param capacity: (int) optional capacity

        """
        self._capacity: int = capacity  #: (instance attribute) capacity.
        if capacity is None or capacity < 0:
            self._capacity = StackOfNonNegativeIntegers.DEFAULT_CAPACITY
        self._size: int = 0  #: (instance attribute) element count.
        self._elements: [int] = [0]*self._capacity  #: (instance attribute) elements.

    @property
    def size(self) -> int:
        """
        Returns size.

        :return: (int) size

        """
        return self._size

    @property
    def capacity(self) -> int:
        """
        Returns capacity.

        :return: (int) capacity

        """
        return self._capacity

    def push(self, element: int) -> int:
        """
        Pushes an element on top of stack.

        :param element: (int) element to push

        :return: (int)
        - SUCCESS if element has been pushed
        - NEGATIVE_ELEMENT if element is negative
        - STACK_IS_FULL if stack is full

        """
        if element < 0:
            return StackOfNonNegativeIntegers.ELEMENT_IS_NEGATIVE
        if self._size == self._capacity:
            return StackOfNonNegativeIntegers.STACK_IS_FULL
        self._elements[self._size] = element
        self._size += 1
        return StackOfNonNegativeIntegers.SUCCESS

    def pop(self) -> int:
        """
        Pops (removes and returns) element on top of stack.

        :return: (int)
        - element on top of stack if it exists
        - STACK_IS_EMPTY if stack is empty

        """
        if self._size == 0:
            return StackOfNonNegativeIntegers.STACK_IS_EMPTY
        self._size -= 1
        return self._elements[self._size]

    def view(self) -> int:
        """
        Returns element on top of stack (without removing it).

        :return: (int)
        - element on top of stack if it exists
        - STACK_IS_EMPTY if stack is empty

        """
        if self._size == 0:
            return StackOfNonNegativeIntegers.STACK_IS_EMPTY
        return self._elements[self._size-1]

    def __str__(self) -> str:
        """
        Returns a string representation of the stack like:

        - "stack, capacity=..., size=..." as first line
        - one element per line, top first.

        :return: (str) a string representation of the stack

        """
        result = "stack, capacity=" + str(self._capacity) + ", size=" + str(self._size) + "\n"
        for index in range(1, self._size+1):
            result += "| " + str(self._elements[self._size-index]) + "\n"
        return result + "---"

