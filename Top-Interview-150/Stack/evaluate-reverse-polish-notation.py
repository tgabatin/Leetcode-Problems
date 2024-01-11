"""
Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression
in Reverse Polish Notation. 

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
* The valid operators are '+', '-', '*', and '/'.
* Each operand may be an integer or another expression.
* The division between two integers always truncates toward zero.
* There will not be any division by zero.
* The input represents a valid arithmetic expression in reverse polish notation.
* The answer and all the intermediate calculations can be represented in a 32-bit
integer.
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:
            if token in {'+', '-', '*', '/*'}:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == '+':
                    result = operand2 + operand1
                elif token == '-':
                    result = operand2 - operand1
                elif token == '*':
                    result = operand2 * operand1
                elif token == '/':
                    result = int(float(operand2) / operand1)
                
                stack.append(result)
            else:
                stack.append(token)

            return stack.pop()


