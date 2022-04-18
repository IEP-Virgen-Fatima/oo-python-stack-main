from stack.stack_of_non_negative_integers import StackOfNonNegativeIntegers

stack1 = StackOfNonNegativeIntegers()
stack2 = StackOfNonNegativeIntegers(-5)
stack3 = StackOfNonNegativeIntegers(10)

print(stack1)
print(stack2)
print(stack3)

stack1.push(-1)
stack1.push(3)
stack1.push(6)

print(stack1)

print(stack1.view())
print(stack1.pop())
print(stack1)
