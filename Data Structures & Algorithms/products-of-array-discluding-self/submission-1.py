class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCounter = 0
        zeroFound = False
        for i in nums:
            if i!=0:
                product *= i
            else: 
                zeroFound = True
                zeroCounter += 1
        n = len(nums)
        if zeroCounter>1:
            return [0]*n
        if zeroFound:
            res = [0]*n
        else:
            res = [product]*n
        for i in range(n):
            if nums[i]!=0:
                res[i] //= nums[i]
            else:
                res[i] = product
                break
            
        return res

        