nums = [1,1,1,2,2,3]
k = 2

# using hashmap and heap - o(n + nlogk) runtime, o(n) space
import heapq
import collections as c
counter = c.Counter(nums)
res = heapq.nlargest(k, counter.keys(), key=counter.get)
return res
