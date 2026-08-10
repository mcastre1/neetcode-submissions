class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        resultStack = []
        operators = {}
        operators['+'], operators['-'], operators['*'], operators['/'] = 1,1,1,1


        for t in tokens:
            if t not in operators:
                resultStack.append(int(t))
            else:
                right = resultStack.pop()
                left = resultStack.pop()

                match t:
                    case '+':
                        resultStack.append(left+right)    
                    case '-':
                        resultStack.append(left-right)
                    case '*':
                        resultStack.append(left*right)
                    case '/':
                        resultStack.append(int(left/right))
        
        return resultStack[-1]