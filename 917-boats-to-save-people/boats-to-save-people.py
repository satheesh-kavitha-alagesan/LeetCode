class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        nu = 0
        r = len(people)-1
        while l <= r:
            nu +=1
            if people[l] + people[r] <= limit:
                l+=1
            r-=1
        return nu