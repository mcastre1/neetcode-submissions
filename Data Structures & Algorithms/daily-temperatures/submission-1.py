class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pastTemperatures = []
        days = [0] * (len(temperatures)) 

        for i in range(len(temperatures)):
            if not pastTemperatures:
                pastTemperatures.append(i)
                continue

            while pastTemperatures and temperatures[i] > temperatures[pastTemperatures[-1]]:
                index = pastTemperatures.pop()
                days[index] = i - index

            pastTemperatures.append(i)

        return days