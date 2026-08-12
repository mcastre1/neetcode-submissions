class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        carPositions = [] # Array of tuples for each car (position, speed)
        fleets = []

        for i in range(len(position)):
            carPositions.append((position[i], speed[i]))

        # Sort array of tuples
        carPositions.sort(reverse=True)

        for i in range(len(carPositions)):
            currentTime = (target - carPositions[i][0]) / carPositions[i][1]
            if not fleets:
                fleets.append(currentTime)
            
            if  fleets[-1] < currentTime:
                fleets.append(currentTime)

        return len(fleets)
