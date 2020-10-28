nums1 = [1,2]
nums2 = [3,4]

# probably slowest due to sort function - o((m+n) log(m+n)) time, o(m+n) space
nums3 = sorted(nums1+nums2)
if len(nums3) % 2 == 0:
    return (nums3[len(nums3)//2] + nums3[len(nums3)//2+1])/2
else:
    return nums3[len(nums3)//2]


# use two heaps (one min, one max) - o()
"""
pseudocode

- combine two lists as one list
- initialize two heaps, one max heap (for left half) and one min heap (for right half)
    - for max heap, we'll store negative versions of numbers (so technically still min heap)
- iterate through list
    - push negative version of number to max heap
    - if max heap is larger than min heap, push (negated) to max heap, pop from max heap, and push it (negated) to min heap
    - else, push to min heap, pop from min heap and push it (negated) to max heap
- at the end, we should have two heaps with the middle 2 at the tops
- if length of list is odd, then just pop from max heap and return it
- else, pop from both and return the avg
"""
import heapq

nums3 = nums1 + nums2
maxHeap = []
minHeap = []

for i in nums3:
    if len(maxHeap) > len(minHeap):
        heapq.heappush(maxHeap, -1*i)
        heapq.heappush(minHeap, -1*heapq.heappop(maxHeap))
    else:
        heapq.heappush(minHeap, i)
        heapq.heappush(maxHeap, -1*heapq.heappop(minHeap))

if len(nums3) % 2 == 0:
    return (-1*heapq.heappop(maxHeap)+heapq.heappop(minHeap)) / 2
return -1*heapq.heappop(maxHeap)


# optimal solution
# https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
"""
pseudocode

- initiate 2 pointers, lo and hi
- while lo < hi
    - 
"""

len1 = len(nums1)
len2 = len(nums2)

if len1 > len2:
    return self.findMedianSortedArrays(nums2, nums1)

lo = 0
hi = len1
while lo <= hi:
    partitionX = (lo+hi)/2
    partitionY = (len1+len2+1)//2 - partitionX

    maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX-1]
    minRightX = float('inf') if partitionX == len1 else nums1[partitionX]
    maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY-1]
    minRightY =  float('inf') if partitionY == len2 else nums2[partitionY]
    if maxLeftX <= minRightY and maxLeftY <= minRightX:
        if (len1 + len2) % 2 == 0:
            return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
        else:
            return max(maxLeftX, maxLeftY)
    elif maxLeftX > minRightY:
        hi = partitionX - 1 
    else:
        lo = partitionX + 1

