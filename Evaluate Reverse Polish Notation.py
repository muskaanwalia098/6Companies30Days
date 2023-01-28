class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Creating a Stack
        stack = []
        # tok = ['+', '-', '*', '/']
        for i in tokens:
            # if i not in tok:
            #     stack.append(int(i))
    
            # else:
                # if len(stack) >= 2:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]
