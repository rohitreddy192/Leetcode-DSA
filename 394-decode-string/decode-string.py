class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i=="]":
                lis = list()
                while stack[-1] !="[":
                    lis.append(stack.pop())
                
                lis = lis[::-1]
                combine_str = "".join(lis)
                stack.pop()
                num_str = ""
                while stack and stack[-1].isdigit():
                    num_str += stack.pop()
                int_var = int(num_str[::-1])
                combine_str = int_var * combine_str
                stack.append(combine_str)
            else:
                stack.append(i)
        return "".join(stack)