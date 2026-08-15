class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        window = (0, len(matrix))
        row = 0
        col = 0

        while True:
            if window[1] - window[0] <= 1:
                row = window[0]
                break

            mid = int((window[1] - window[0])/2)

            if matrix[window[0] + mid][0] <= target:
                window = (window[0] + mid, window[1])
            else:
                window = (window[0], window[1] - mid)
             
        window = (0, len(matrix[row]))
        while True:
            if window[1] - window[0] <= 1:
                col = window[0]
                break

            mid = int((window[1] - window[0])/2)

            if matrix[row][window[0] + mid] <= target:
                window = (window[0] + mid, window[1])
            else:
                window = (window[0], window[1] - mid)

        return matrix[row][col] == target