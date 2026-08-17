class TimeMap:

    def __init__(self):
        self.cont = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        temp = self.cont.get(key, [])
        temp.append((value, timestamp))

        self.cont[key] = temp

    def get(self, key: str, timestamp: int) -> str:
        temp = self.cont.get(key)
        if not temp:
            return ""

        index = -1

        l, r = 0, len(temp) - 1
        while l <= r:
            mid = (l + r) // 2

            if temp[mid][1] == timestamp:
                index = mid
                break
            
            if temp[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        if not index == -1:
            return self.cont[key][index][0]
        else:
            if l == 0:
                return ""
            else:
                return self.cont[key][l-1][0]
        
    
        

