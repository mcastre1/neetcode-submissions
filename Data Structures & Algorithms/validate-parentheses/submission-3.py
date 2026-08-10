class Solution:
    def isValid(self, s: str) -> bool:
        container = []
        
        closing = {}
        closing[')'], closing['}'], closing[']'] = '(','{','['

        for c in s:
            if c not in closing:
                container.append(c)
            else:
                if len(container) > 0 and container[-1] == closing[c]:
                    container.pop()
                else:
                    return False

        if len(container) == 0:
            return True
        else:
            return False