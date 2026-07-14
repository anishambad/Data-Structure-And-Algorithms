class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i = 0
        j = n-1

        res = [0]*n
        pos = n-1

        while i <= j :

            if abs(nums[i]) > abs(nums[j]):
                res[pos] = nums[i] * nums[i]
                i+=1

            else :
                res[pos] = nums[j] * nums[j]
                j-=1

            
            pos -=1

        return res

        