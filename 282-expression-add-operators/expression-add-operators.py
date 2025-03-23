class Solution:
    def addOperators(self,num, target):
        result = []
        
        def backtrack(index, expr, curr_val, prev_operand):
            if index == len(num):
                if curr_val == target:
                    result.append(expr)
                return
            
            for i in range(index, len(num)):
                # Prevent numbers with leading zeros
                if i > index and num[index] == '0':
                    break
                
                # Get the current partitioned number
                part = num[index:i+1]
                part_val = int(part)
                
                # If this is the first number, we don't use an operator
                if index == 0:
                    backtrack(i + 1, expr + part, part_val, part_val)
                else:
                    # Addition
                    backtrack(i + 1, expr + '+' + part, curr_val + part_val, part_val)
                    
                    # Subtraction
                    backtrack(i + 1, expr + '-' + part, curr_val - part_val, -part_val)
                    
                    # Multiplication (Maintain precedence)
                    backtrack(i + 1, expr + '*' + part, 
                            curr_val - prev_operand + (prev_operand * part_val), 
                            prev_operand * part_val)
        
        backtrack(0, "", 0, 0)
        return result
