class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        waterSum = 0

        # Finding the max height to the left.
        for i, h in enumerate(height):
            if i == 0:
                maxLeft.append(0) 
                continue
            
            maxH = 0
            j = 0

            while j < i:
                maxH = max(height[j], maxH)
                j += 1

            maxLeft.append(maxH)

        # Finding the max height to the right.
        for i in range(len(height)-1,-1,-1):
            if i == len(height) - 1:
                maxRight.insert(0,0)
                continue

            maxH = 0
            j = len(height) - 1

            while j > i:
                maxH = max(height[j], maxH)
                j -= 1
            
            maxRight.insert(0, maxH)

        for i, h in enumerate(height):
            water = min(maxLeft[i], maxRight[i]) - height[i]

            if water >= 0:
                waterSum += water

        
        return waterSum
            