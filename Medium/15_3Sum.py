
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res
    
if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
    print(s.threeSum([]))  # Output: []
    print(s.threeSum([0]))  # Output: []
   
            