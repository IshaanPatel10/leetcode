class Solution:
    def findClosestNumber(nums):
        
        closest = float('inf')

        for i in nums:
            if abs(i) < abs(closest):
                closest = i
        
        if abs(closest) in nums and closest < 0:
            return abs(closest)
        
        return closest

    findClosestNumber([-4,-2,1,4,8])