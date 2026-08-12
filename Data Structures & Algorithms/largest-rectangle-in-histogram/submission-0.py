class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = []
        maxArea = 0

        for i in range(len(heights)):
            if not areas:
                areas.append((i, heights[i]))
                continue

            new_index = -1
            while areas and areas[-1][1] >= heights[i]:
                last_item = areas.pop()
                maxArea = max((i - last_item[0]) * last_item[1], maxArea)
                new_index = last_item[0]

            if new_index == -1:
                areas.append((i, heights[i]))
            else:
                areas.append((new_index, heights[i]))

        for a in areas:
            maxArea = max((len(heights) - a[0]) * a[1], maxArea)

        return maxArea
