class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        cur_num = 0
        operation = '+'
        
        for i in range(len(s)):
            cur_char = s[i]
            if cur_char.isdigit():
                cur_num = (cur_num * 10) + int(cur_char)
            if cur_char in ['+', '-', '*', '/'] or i == len(s) - 1:
                if operation == '-':
                    stack.append(-cur_num)
                elif operation == '+':
                    stack.append(cur_num)
                elif operation == '*':
                    stack.append(stack.pop() * cur_num)
                elif operation == '/':
                    stack.append(int(stack.pop() / cur_num))
                
                operation = cur_char
                cur_num = 0

        answer = 0
        while stack:
            answer += stack.pop()
        
        return answer
        
    #68ms 59.8mb
    # def calculate(self, s: str) -> int:
    #     s = s.replace(' ', '')
    #     s = s.replace('/', '//')
    #     return eval(s)