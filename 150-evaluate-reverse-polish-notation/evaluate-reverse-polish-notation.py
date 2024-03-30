class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def is_number(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        while tokens:
            cur = tokens.pop(0)
            if is_number(cur):
                stack.append(int(cur))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if cur == '+':
                    stack.append(val1+val2)
                elif cur == '-':
                    stack.append(val2-val1)
                elif cur == '*':
                    stack.append(val2*val1)
                elif cur == '/':
                    stack.append(int(val2/val1))
        return stack[0]