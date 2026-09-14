from stack import Stack
from queue import Queue


def copy_stack(stack: Stack) -> Stack:
    """
    Create and return a copy of a stack using one queue as auxiliary storage.

    Args:
        stack (Stack): The stack whose values should be copied.

    Returns:
        stack_copy (Stack): A new stack containing the values from stack.
    """
    storage_queue = Queue()
    stack_copy = Stack()

    while not stack.isEmpty():
        storage_queue.enqueue(stack.pop())

    while not storage_queue.isEmpty():
        stack_copy.push(storage_queue.dequeue())

    while not stack.isEmpty():
        stack_copy.push(stack.pop())

    return stack_copy
