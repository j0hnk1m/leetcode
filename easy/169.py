class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
        
        if len(nums) == 1:
            return nums[0]
        
        hashmap = {}
        maj = None
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
                
                if hashmap[i] > len(nums) // 2:
                    maj = i     
            else:
                hashmap[i] = 1
        return maj
        