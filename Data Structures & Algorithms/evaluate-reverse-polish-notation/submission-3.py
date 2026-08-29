class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        nums = []

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                nums.append(int(tokens[i]))

            if tokens[i] in operators:
                num2 = nums.pop()
                num1 = nums.pop()
                if tokens[i] == "+":
                    new_num = num1 + num2
                elif tokens[i] == "-":
                    new_num = num1 - num2
                elif tokens[i] == "*":
                    new_num = num1 * num2
                else:
                    new_num = num1 / num2
                nums.append(int(new_num))
            
        return nums[-1]

