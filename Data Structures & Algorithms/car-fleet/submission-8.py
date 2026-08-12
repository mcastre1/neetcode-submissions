class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True) # Make sure to reverse sort
        fleets = []

        for pos, spd in cars:
            currentTime = (target - pos) / spd

            # If current cars takes longer to get to target we append it as a fleet
            if not fleets or currentTime > fleets[-1]:
                fleets.append(currentTime)

        return len(fleets)